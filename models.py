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


class Teacher(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    full_name = db.Column(db.String(70), nullable=False)
    birth_day = db.Column(db.Date,nullable = False)
    email_adress = db.Column(db.String(100), nullable=False)
    phone_num = db.Column(db.String(20), nullable=False)
    subject_id = db.Column(db.Integer, db.ForeignKey("subject.id"))

    def __repr__(self):
        return f'Teacher {self.full_name}'


class Subject(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50),nullable=False)
    teachers = db.relationship("Teacher", backref="subject")

    def __repr__(self):
        return f'Subject {self.name}'


# створити класи ClassGroup, Lesson(урок) Grade (оцінка), 
 