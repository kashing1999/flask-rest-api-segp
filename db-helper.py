from app.database import db
from app.models import Student, House, Recycable

students = [
        ("Lee Ka Shing", 1, "kashing@gmail.com", 1, 2, 3),
        ("Chloe San", 2, "chloe@gmail.com", 4, 5 ,6)
]

for StudentName, HouseID, email, Brown, Blue, Orange in students:
    total = Brown + Blue + Orange
    s = Student(StudentName=StudentName, HouseID=HouseID, Email=email, BrownRecycled=Brown, BlueRecycled=Blue, OrangeRecycled=Orange, TotalRecycled=total)
    db.session.add(s)

houses = [
        ("Red", 6, 1, 2, 3),
        ("Blue", 15, 4, 5, 6)
]

for HouseName, Points, Brown, Blue, Orange in houses:
    total = Brown + Blue + Orange
    h = House(HouseName=HouseName, HousePoints=Points, BrownRecycled=Brown, BlueRecycled=Blue, OrangeRecycled=Orange, TotalRecycled=total)
    db.session.add(h)

recycables = [
        ("Paper", 1, 10),
        ("Plastic", 1, 5)
]

for name, points, total in recycables:
    r = Recycable(Name=name, Value=points, TotalRecycled=total)
    db.session.add(r)

db.session.commit()
