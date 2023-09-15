from flask import Flask, render_template # импортируем класс Flask из библиотеки flask

app = Flask(__name__) # создаем класс приложения, __name__ - имя приложения

@app.route("/index") # декоратор
@app.route("/") # еще один декоратор
def index():
    return render_template("index.html")

@app.route("/about")
def about():
    return render_template("about.html")

if __name__ == '__main__': # точка входа
    app.run(debug=True) # запустить приложение (в режиме отладки)
