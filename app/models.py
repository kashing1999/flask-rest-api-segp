from app.database import db
from werkzeug.security import generate_password_hash, check_password_hash


class Recycable(db.Model):
    id              =  db.Column(db.Integer, primary_key=True)
    Name            =  db.Column(db.String(64))
    Value           =  db.Column(db.Integer)

    TotalRecycled   =  db.Column(db.Integer)

    def __repr__(self):
        return f'Recycable {self.Name}'

    def as_dict(self):
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}

class House(db.Model):
    id              =  db.Column(db.Integer, primary_key=True)
    HouseName       =  db.Column(db.String(64), index=True, unique=True, nullable=False)
    HousePoints     =  db.Column(db.Integer)
    Students        =  db.relationship('Student', backref='house', lazy=True)

    BlueRecycled    =  db.Column(db.Integer)
    BrownRecycled   =  db.Column(db.Integer)
    OrangeRecycled  =  db.Column(db.Integer)

    TotalRecycled   =  db.Column(db.Integer)

    def __repr__(self):
        return f'<House {self.HouseName}>'

    def as_dict(self):
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}

class Student(db.Model):
    id              =  db.Column(db.Integer, primary_key=True)
    StudentName     =  db.Column(db.String(64), index=True, nullable=False)
    Email           =  db.Column(db.String(64), index=True, unique=True, nullable=False)
    password_hash   = db.Column(db.String(128))

    points    =  db.Column(db.Integer)
    HouseID         =  db.Column(db.Integer , db.ForeignKey('house.id'))

    BlueRecycled    =  db.Column(db.Integer)
    BrownRecycled   =  db.Column(db.Integer)
    OrangeRecycled  =  db.Column(db.Integer)

    TotalRecycled   =  db.Column(db.Integer)

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

    def __repr__(self):
        return f'<Student {self.id}:{self.StudentName}>'

    def as_dict(self):
        return {c.name: getattr(self, c.name) for c in self.__table__.columns if c.name != "password_hash"}
