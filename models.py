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
    full_name = db.Column(db.String(150), nullable=False)
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
    
class ClassGroup(db.Model):
    id = db.Column(db.Integer,primary_key = True)
    name = db.Column(db.String(50),nullable=False)
    class_teacher = db.Column(db.String(150),db.ForeignKey("teacher.full_name"))
    grade = db.Column(db.Integer,nullable = False)
    students = db.Column(db.String(150),db.ForeignKey("student.full_name"))
    main_student = db.Column(db.String(150),db.ForeignKey("student.id")) 
    students_number = db.Column(db.Integer,nullable = False)
    # timetable

    def __repr__(self):
        return f'Class {self.name}'
    
class Lesson(db.Model):
    id = db.Column(db.Integer,primary_key = True)
    name = db.Column(db.String(50),nullable=False)
    hours_per_week = db.Column(db.Integer,nullable = False)
    teacher = db.Column(db.String(150),db.ForeignKey("teacher/.full_name"))

    def __repr__(self):
        return f'Lesson {self.name}'
    
class Mark(db.Model):
    id = db.Column(db.Integer,primary_key = True)

    def __repr__(self):
        return f'Lesson {self.id}'

    

    
    
    






    



# створити класи ClassGroup, Lesson(урок) Grade (оцінка), 
 