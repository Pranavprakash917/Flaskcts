from flask import Flask,render_template,request,redirect,url_for
app = Flask(__name__)

@app.route('/<int:name>')
def home(name):
    return render_template('new.html',name=name)

@app.route('/<int:n>')
def mul(n):
    return render_template('second.html',name=n)

@app.route('/home')
def img():
    return render_template('image.html')

@app.route('/link')
def ho():
    return render_template('base.html')
@app.route('/')
def home2():
    return render_template('index.html')
@app.route('/register',methods=['POST'])
def register():
    name=request.form['name']
    place=request.form['place']
    email=request.form['email']
    return render_template('register.html',name=name,place=place,email=email)

import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  database='PRANflask'
)

mycursor = mydb.cursor()

@app.route('/link2')
def home3():
    return render_template('insert.html')

@app.route('/insert',methods=['POST'])
def insert():
    if request.method=='POST':
        name=request.form['name']
        address=request.form['address']
        insert_query="INSERT INTO customer(name,address) VALUES (%s,%s)"
        user_data=(name,address)
        mycursor.execute(insert_query,user_data)
        mydb.commit()
        return "inserted"

@app.route("/retrieve")
def read():
    insert_query="select * from customer"
    mycursor.execute(insert_query)
    data=mycursor.fetchall()
    return render_template("read.html",data=data)

@app.route("/delete/<int:id>",methods=['POST','GET'])
def delete(id):
    query = "DELETE FROM customer WHERE id=%s"
    d=(id,)
    mycursor.execute(query,d)
    mydb.commit()
    # mycursor.close()
    return redirect(url_for('read'))

@app.route("/update/<int:id>",methods=['POST','GET'])
def update(id):
    mycursor=mydb.cursor()
    if request.method=='GET':
        select_query="SELECT * FROM customer WHERE id=%s"
        data=(id,)
        mycursor.execute(select_query,data)
        user=mycursor.fetchone()
        return render_template('update.html',user=user)
    elif request.method=='POST':
        name=request.form['name']
        address=request.form['address']
        query="UPDATE customer SET name=%s,address=%s WHERE id=%s"
        data=(name,address,id)
        mycursor.execute(query,data)
        mydb.commit()
        mycursor.close()
        return redirect(url_for('read'))
if __name__=='__main__':
   app.run(debug=True)