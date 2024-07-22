from flask import Flask
app = Flask(__name__)


import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
    database="PRANflask",
)

mycursor = mydb.cursor()

# mycursor.execute("CREATE DATABASE PRANflask")
# mycursor.execute("CREATE TABLE customers (name VARCHAR(255), address VARCHAR(255))")
mycursor.execute("CREATE TABLE student (id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(255), address VARCHAR(255))")

if __name__=='__main__':
   app.run(debug=True)