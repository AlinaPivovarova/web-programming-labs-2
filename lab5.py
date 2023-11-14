from flask import redirect, Blueprint, render_template, request
import psycopg2

lab5 =Blueprint('lab5',__name__)

def dBConnect():
    conn = psycopg2.connect(
        host="127.0.0.1",
        database = "knowledge_base",
        user = "pivovarova_alina_base",
        password = "12345",
        port = 5433
    )

    return conn;

def dBClose(cursor,connection):
    cursor.close()
    connection.close()


@lab5.route("/lab5/")
def main():
    visibleUser = 'Anon'
    # Прописываем параметры подключения к БД
    conn = psycopg2.connect(
        host="127.0.0.1",
        database="knowledge_base",
        user="pivovarova_alina_base",
        password="12345",
        port = 5433
    )
    # Получаем курсор. С помощью него мы можем выполнять SQL-запросы
    cur = conn.cursor()
    # Пишем запрос, который курсор должен выполнить
    cur.execute("SELECT * FROM users;")
    # fetchall - получить все строки, которые получились в результате выполнения SQL-запроса в execute
    # Сохраняем эти строки в переменную result
    result = cur.fetchall()

    # Закрываем соединение с БД
    cur.close()
    conn.close()

    print(result)

    return render_template('lab5.html', username=visibleUser)


@lab5.route('/lab5/users')
def user():
    conn = psycopg2.connect(
        host="127.0.0.1",
        database = "knowledge_base",
        user = "pivovarova_alina_base",
        password = "12345",
        port = 5433
    )
    cur = conn.cursor()
    cur.execute("SELECT * FROM users;")
    result = cur.fetchall()
    return render_template('lab5users.html', users=result)


@lab5.route('/lab5/register', methods=['GET', 'POST'])
def registerPage():
    errors = []

    if request.method == 'GET':
        return render_template('register.html', errors=errors)

    username = request.form.get('username')
    password = request.form.get('password')

    if not (username and password):
        errors.append("Пожалуйста, заполните все поля")
        print(errors)
        return render_template('register.html', errors=errors)

    conn = dBConnect()
    cur = conn.cursor()
    cur.execute(f"SELECT username FROM users WHERE username = '{username}';")

    if cur.fetchone() is not None:
        errors.append("Пользователь с данным именем уже существует")
        dBClose(cur, conn)
        return render_template('register.html', errors=errors)
    
    cur.execute(f"INSERT INTO users (username, password) VALUES ('{username}','{password}');")
    conn.commit()
    dBClose(cur, conn)

    return redirect("/lab5/login")