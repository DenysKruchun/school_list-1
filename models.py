from  app import db

class Student(db.Model):
    id  = db.Column(db.Integer, primary_key=True)
    full_name = db.Column(db.String(150),nullable = False)
    phone_number = db.Column(db.String(20),nullable = False)
    email = db.Column(db.String(100), unique = True)  
    birth_day = db.Column(db.Date,nullable = False)
    created = db.Column(db.DateTime, default = db.func.now())

    def __repr__(self):
        return f'Student {self.full_name}'

# створити класи Teacher, Subject, Grade, Group
