
from flask import Flask, render_template
import flask
import pymysql as mysql
from datetime import datetime
from flask import redirect, url_for,json, request
import mysql.connector
import cgi, cgitb


app=Flask(__name__)

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  passwd="abc123",
  database="employees"
)




@app.route("/")
def index():
    return render_template('index.html')


@app.route('/add', methods=['GET', 'POST'])
def add():
    error = None
    if request.method == 'POST':
        _name = request.form['name'].strip()
        _surname = request.form['surname'].strip()
        if len(_name) > 0:
            mycursor= mydb.cursor()
            print(_name)
            mycursor.execute("INSERT INTO `employees`.`pracownicy` ( `Imie`, `Nazwisko`) VALUES ( %s, %s);",[_name,_surname])
            mydb.commit()
            return redirect(url_for('add'))

        error = 'Nie możesz dodać pustego zadania!'  # komunikat o błędzie

    mycursor = mydb.cursor()
    mycursor.execute("SELECT * FROM pracownicy;")
    workesr = mycursor.fetchall()
    return render_template('add.html', workers=workesr, error=error)



@app.route("/remove", methods=['GET', 'POST'])
def remove():
    error = None
    if request.method == 'POST':
        _id = request.form['id'].strip()
        if len(_id) > 0:
            mycursor= mydb.cursor()
            print(_id)
            mycursor.execute("DELETE FROM `employees`.`pracownicy` WHERE (`id`=%s);",[_id])
            mydb.commit()
            return redirect(url_for('remove'))

        error = 'Nie możesz dodać pustego zadania!'  # komunikat o błędzie

    mycursor = mydb.cursor()
    mycursor.execute("SELECT * FROM pracownicy;")
    workesr = mycursor.fetchall()
    return render_template('remove.html', workers=workesr, error=error)

@app.route("/display")
def display():
    mycursor = mydb.cursor()
    mycursor.execute("SELECT * FROM pracownicy")
    myresult = mycursor.fetchall()
    return render_template('display.html',myresult=myresult)

if __name__=="__main__":
    app.run()