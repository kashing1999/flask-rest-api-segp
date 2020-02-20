from app import db

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

    def __repr__(self):
        return f'<House {self.HouseName}>'

    def as_dict(self):
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}

class Student(db.Model):
    # TODO:password
    id              =  db.Column(db.Integer, primary_key=True)
    StudentID       =  db.Column(db.String(64), index=True, unique=True, nullable=False)
    StudentName     =  db.Column(db.String(64), index=True, nullable=False)
    Email           =  db.Column(db.String(64), index=True, unique=True, nullable=False)
    HouseID         =  db.Column(db.Integer , db.ForeignKey('house.id'))

    BlueRecycled    =  db.Column(db.Integer)
    BrownRecycled   =  db.Column(db.Integer)
    OrangeRecycled  =  db.Column(db.Integer)

    def __repr__(self):
        return f'<Student {self.StudentID}:{self.StudentName}>'

    def as_dict(self):
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}