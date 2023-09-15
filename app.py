from flask import Flask # импортируем класс Flask из библиотеки flask

app = Flask(__name__) # создаем класс приложения, __name__ - имя приложения

@app.route("/")
def index():
    return "<h1>Index</h1>"

if __name__ == '__main__': # точка входа
    app.run(debug=True) # запустить в режиме отладки