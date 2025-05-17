from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate


app = Flask(__name__)  # Створюємо веб–додаток Flask
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

app.config["SECRET_KEY"] = "reve ta stohne dnipr"

db = SQLAlchemy(app)
migrate = Migrate(app, db)
from models import Student,Teacher,Subject

@app.route("/")  # Вказуємо url-адресу для виклику функції
def index():
    teachers = Teacher.query.filter_by(full_name = "Ann").first()
    subject = Subject(name = "PE")
    db.session.add(subject)
    db.session.commit()
    return render_template("index.html",teachers = teachers)  # html-сторінка, що повертається у браузер


if __name__ == "__main__":
    app.config['TEMPLATES_AUTO_RELOAD'] = True  # автоматичне оновлення шаблонів
    app.run(debug=True)  # Запускаємо веб-сервер з цього файлу в режимі налагодження
