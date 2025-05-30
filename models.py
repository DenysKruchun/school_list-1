from app import db


class Teacher(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    full_name = db.Column(db.String(70), nullable=False)
    birth_day = db.Column(db.String(70), nullable=False)
    email_adress = db.Column(db.String(100), nullable=False)
    phone_num = db.Column(db.String(20), nullable=False)
    subject_id = db.Column(db.Integer, db.ForeignKey("subject.id"))

    def __repr__(self):
        return f'Teacher {self.full_name}'


class Subject(db.Model):
    
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    teachers = db.relationship("Teacher", backref="subject")

    def __repr__(self):
        return f'Subject {self.name}'


class ClassGroup(db.Model):
    __tablename__ = 'class_group'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    class_teacher = db.Column(db.String(150), db.ForeignKey("teacher.id"))
    grade = db.Column(db.Integer, nullable=False)

    students = db.relationship("Student", backref="classgroup")

    def __repr__(self):
        return f'Class {self.name}'


class Student(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    full_name = db.Column(db.String(150), nullable=False)
    phone_number = db.Column(db.String(20), nullable=False)
    email = db.Column(db.String(100), unique=True)
    birth_day = db.Column(db.Date, nullable=False)
    created = db.Column(db.DateTime, default=db.func.now())
    class_group_id = db.Column(db.Integer, db.ForeignKey("class_group.id"))
    is_starosta = db.Column(db.Boolean, default = False)

    # classgroup = db.relationship("ClassGroup", backref="students")

    def __repr__(self):
        return f'Student {self.full_name}'


class Lesson(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    week_day = db.Column(db.String(20),nullable=False)
    number_lesson = db.Column(db.Integer)

    teacher_id = db.Column(db.Integer, db.ForeignKey("teacher.id"))
    subject_id = db.Column(db.Integer, db.ForeignKey("subject.id"))
    class_group_id = db.Column(db.Integer, db.ForeignKey("class_group.id"))

    def __repr__(self):
        return f'Lesson {self.week_day}, {self.number_lesson}'


class Mark(db.Model):
    id = db.Column(db.Integer, primary_key=True)

    def __repr__(self):
        return f'Lesson {self.id}'

    


# створити класи ClassGroup, Lesson(урок) Grade (оцінка),
