from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate


app = Flask(__name__)  # Створюємо веб–додаток Flask
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

app.config["SECRET_KEY"] = "reve ta stohne dnipr"

db = SQLAlchemy(app)
migrate = Migrate(app, db)
from models import Teacher,Subject,ClassGroup,Lesson,Mark

@app.route("/")  # Вказуємо url-адресу для виклику функції
def index():
    teachers = Teacher.query.all()
    # subject = Subject(name = "PE")
    # classgroup = ClassGroup()
    # lesson = Lesson()
    # mark = Mark()
    # db.session.add(subject)
    # db.session.add(classgroup)
    # db.session.add(lesson)
    # db.session.add(mark)

    # db.session.commit()

    return render_template("index.html",teachers = teachers)  # html-сторінка, що повертається у браузер

    

@app.route("/add_teacher")  # Вказуємо url-адресу для виклику функції
def add_teacher():
    teacher = Teacher(full_name = "Ivan", birth_day = "1999/03/05",email_adress = "gvcvhg@gdhg",phone_num = "872646334",subject_id = 0)
    db.session.add(teacher)
    db.session.commit()

    return render_template("index.html",teachers = teacher)  # html-сторінка, що повертається у браузер


@app.route("/add_subject")  # Вказуємо url-адресу для виклику функції
def add_subject():
    subject = Subject(name = "IT")
    db.session.add(subject)
    db.session.commit()

    return render_template("index.html",teachers = subject)  # html-сторінка, що повертається у браузер



if __name__ == "__main__":
    app.config['TEMPLATES_AUTO_RELOAD'] = True  # автоматичне оновлення шаблонів
    app.run(debug=True)  # Запускаємо веб-сервер з цього файлу в режимі налагодження
