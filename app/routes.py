from app import app, jsonify, abort, request, db#, Image, transforms
from app.models import Student, House
from base64 import b64decode

# TODO: Session cookie

# Get student by student ID
# TODO: get student by email?
@app.route('/student/<string:student_id>', methods=['GET'])
def get_student(student_id):
    s = Student.query.filter(Student.StudentID == student_id)
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
    s = Student(StudentID=StudentID, StudentName=StudentName, HouseID=HouseID)

    db.session.add(s)
    db.session.commit()

    return jsonify(s.as_dict()), 201


# Get house
@app.route('/house/<int:house_id>', methods=['GET'])
def get_house(house_id):
    h = House.query.get(house_id)
    if h != None:
        return jsonify(h.as_dict())
    abort(404)


@app.route('/predict', methods=['POST'])
def make_prediction():
    if request.json != None and 'recycable_image' in request.json:
        b64 = request.json['recycable_image']
        img = b64decode(b64)
        with open('/tmp/test-out.jpg', 'wb') as f:
            f.write(img)
        return jsonify({'prediction': 'cardboard'}), 200
    else:
        abort(400)