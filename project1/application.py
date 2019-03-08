# @Author: shadabKhan
# @Date:   Tuesday, February 19th 2019, 10:03:07 am
# @Last modified by:   shadabKhan
# @Last modified time: Saturday, March 9th 2019, 12:54:41 am



import os

from flask import Flask, session,render_template,request
from flask_session import Session
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker

app = Flask(__name__)

# Check for environment variable
if not os.getenv("DATABASE_URL"):
    raise RuntimeError("DATABASE_URL is not set")

# Configure session to use filesystem
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

# Set up database
engine = create_engine(os.getenv("DATABASE_URL"))
db = scoped_session(sessionmaker(bind=engine))


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login' ,methods=['post'])
def login():
    try:
        username = request.form['username']
        password = request.form['password']
        result = db.execute("SELECT * FROM users WHERE username = :username",{"username":username})
        result = result.first()
        if result is None:
                raise ValueError
        return render_template('home.html',username=username)
    except ValueError as ve:
        return render_template('error.html',errorDefinition="invalid credentials")


@app.route('/register',methods=['post'])
def register():
    username = request.form['username']
    password = request.form['password']
    email = request.form['email']
    db.execute("insert into users(username,email,password) values(:username,:email,:password);",{"username":username,"email":email,"password":password})
    db.commit()
    result = db.execute('select * FROM users;')
    return render_template('registered.html',username=result)
