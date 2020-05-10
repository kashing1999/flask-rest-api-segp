from app.models import Student

def authenticate(username, password):
    user = Student.query.filter(Student.Email == username)
    if user != None and user.first() != None and user.first().check_password(password):
        return user.first()

def identity(payload):
    user_id = payload['identity']
    return Student.query.filter(Student.id == user_id).first()
