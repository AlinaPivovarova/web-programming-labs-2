from flask import Flask
app = Flask(__name__)

@app.route("/")
def start():
    return """
<!doctype html>
<html>
     <head>
           <title>Пивоварова Алина Евгеньевна, лабораторная 1</title>
     </head>
     <body>
            <header>
            НГТУ, ФБ, Лабораторная работа 1
            </header>

            <h1>web-сервер на flask</h1>

            <footer>
            &copy; Алина Евгеньевна, ФБИ-14, 3 курс, 2023
            </footer>
        </body>
</html>
"""
            