from app import app, jsonify, abort, request, inference#, Image, transforms
from app.database import db
from app.models import Student, House, Recycable
from base64 import b64decode
from hashlib import md5
from datetime import datetime
from flask_jwt import jwt_required, current_identity
import socket


recycable_classes = {
    'Paper': 'Blue',
    'Glass': 'Brown',
    'Plastic': 'Orange'
}

bin_code_numbers = {
    'Blue': 1,
    'Orange': 2,
    'Brown': 3
}


# Get student by student ID
@app.route('/student', methods=['GET'])
@jwt_required()
def get_student():
    s = current_identity
    if s != None:
        return jsonify(s.as_dict())
    abort(404)


# Register new student
@app.route('/student', methods=['POST'])
def register_student():
    if not request.json:
        abort(400)

    StudentName = None
    HouseID = None
    email = None
    password = None
    try:
        StudentName = request.json['StudentName']
        HouseID = request.json['HouseID']
        email = request.json['Email']
        password = request.json['Password']
    except:
        abort(400)

    if Student.query.filter(Student.Email == email).first() != None:
        abort(403)

    avatar = None
    if request.json['Avatar']:
        avatar = request.json['Avatar']
        avatar = b64decode(avatar)


    s = Student(StudentName=StudentName, HouseID=HouseID, Email=email, BrownRecycled=0, BlueRecycled=0, OrangeRecycled=0, TotalRecycled=0, Avatar=avatar)
    s.set_password(password)

    db.session.add(s)
    db.session.commit()

    return jsonify(s.as_dict()), 201

# Change Profile Pic
@app.route('/profile_pic', methods=['POST'])
@jwt_required()
def change_profile_pic():
    s = current_identity
    if s == None:
        abort(404)
    avatar = b64decode(request.json['Avatar'])
    s.Avatar = avatar
    db.session.commit()
    return jsonify({'status': 'successful'}), 201



# Get house
@app.route('/house/<int:house_id>', methods=['GET'])
def get_house(house_id):
    h = House.query.get(house_id)
    if h != None:
        return jsonify(h.as_dict())
    abort(404)


# Leaderboards
@app.route('/leaderboards', methods=['GET'])
def get_leaderboard():
    leaderboard = {}

    houses = House.query.order_by(House.HousePoints).all()
    leaderboard['Houses'] = [h.as_dict() for h in houses]

    students = Student.query.order_by(Student.TotalRecycled).limit(10).all()
    leaderboard['Students'] = [s.as_dict() for s in students]

    recycables = Recycable.query.order_by(Recycable.TotalRecycled).all()
    leaderboard['Recycables'] = [r.as_dict() for r in recycables]

    return jsonify(leaderboard)


# Make prediction
@app.route('/predict', methods=['POST'])
def make_prediction():
    if request.json != None and 'recycable_image' in request.json:
        img = b64decode(request.json['recycable_image'])

        prediction = inference.make_inference(img)

        # file format: prediction_md5sum_date_time.jpg
        # TODO: when deploying the webapp, place data folder outside of web root directory to prevent remote code execution
        filename = prediction + "_" + md5(img).hexdigest() + "_" + datetime.now().strftime("%Y-%m-%d_%H-%M") + '.jpg'
        filepath = "data/" + filename

        with open(filepath, 'wb') as f:
            f.write(img)
        return jsonify({'prediction': prediction}), 200

    else:
        abort(400)

# Student submits recycables
@app.route('/recycle', methods=['POST'])
@jwt_required()
def recycling():
    s = current_identity
    if not request.json or s == None:
        abort(400)

    if request.json['recycable']:
        recycable = request.json['recycable']

    bin_colour = recycable_classes[recycable]

    # Make request to server
    ## --------------------- ##

    HOST = '127.0.0.1'  # The server's hostname or IP address
    PORT = 5000        # The port used by the server

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
        sock.connect((HOST, PORT))
        bin_number = bin_code_numbers[bin_colour]
        sock.sendall( (bin_number.encode()))
        data = s.recv(1024)

        print('Received', data.decode())
        sock.close()

    if bin_colour == "Blue":
        s.BlueRecycled += 1
    if bin_colour == "Orange":
        s.OrangeRecycled += 1
    if bin_colour == "Brown":
        s.BrownRecycled += 1

    house_id = s.HouseID
    house = House.query.filter(id == house_id).first()
    if house != None:
        if bin_colour == "Blue":
            house.BlueRecycled += 1
        if bin_colour == "Orange":
            house.OrangeRecycled += 2
        if bin_colour == "Brown":
            house.BrownRecycled += 1

    recycable = Recycable.query.filter(Recycable.Name==recycable).first()
    recycable.TotalRecycled += 1

    db.session.commit()

    return jsonify({'status': 'submitted', 'points': 1}), 200
