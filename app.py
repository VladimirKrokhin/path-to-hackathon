from flask import Flask, render_template, request, redirect # импортируем класс Flask из библиотеки flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__) # создаем класс приложения, __name__ - имя приложения
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///hackathon.db' # конфигурация бд
db = SQLAlchemy(app) # подключение бд


class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(300), nullable=False)
    text = db.Column(db.Text, nullable=False)


@app.route("/index") # декоратор
@app.route("/") # еще один декоратор
def index():
    return render_template("index.html")

@app.route("/posts")
def posts():
    posts = Post.query.all()
    return render_template("posts.html", posts=posts)

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/create", methods=["POST", "GET"])
def create():
    if request.method == "POST":
        title = request.form["title"]
        text = request.form["text"]

        post = Post(title=title, text=text)

        try:
            db.session.add(post)
            db.session.commit()
            return redirect('/')
        except: 
            return 'При добавлении статьи произошла ошибка'

    else:
        return render_template("create.html")

if __name__ == '__main__': # точка входа
    app.run(debug=True) # запустить приложение (в режиме отладки)
