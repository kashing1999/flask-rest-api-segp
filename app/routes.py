from app import app, jsonify, abort, request, db, inference#, Image, transforms
from app.models import Student, House
from base64 import b64decode
from hashlib import md5
from datetime import datetime

# TODO: Session cookie

# Get student by student ID
# TODO: get student by email?
@app.route('/student/<string:StudentID>', methods=['GET'])
def get_student(StudentID):
    s = Student.query.filter(Student.StudentID == StudentID)
    if s != None:
        return jsonify(s[0].as_dict())
    abort(404)


# Register new student
@app.route('/student', methods=['POST'])
def register_student():
    if not request.json:
        abort(400)
    StudentID = request.json['StudentID']
    StudentName = request.json['StudentName']
    HouseID = request.json['HouseID']
    email = request.json['Email']
    s = Student(StudentID=StudentID, StudentName=StudentName, HouseID=HouseID)
    s.set_password(request.json['Password'])

    db.session.add(s)
    db.session.commit()

    return jsonify(s.as_dict()), 201


# Student submits recycables
@app.route('/recycle', methods=['POST'])
def recycling():
    if not request.json:
        abort(400)
    StudentID = request.json['StudentID']
    HouseID = request.json['HouseID']
    s = Student.query.filter(Student.StudentID == StudentID)
    h = House.query.filter(House.HouseID == HouseID)
    pass


# Get house
@app.route('/house/<int:house_id>', methods=['GET'])
def get_house(house_id):
    h = House.query.get(house_id)
    if h != None:
        return jsonify(h.as_dict())
    abort(404)


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
