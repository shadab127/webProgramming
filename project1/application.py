# @Author: shadabKhan
# @Date:   Tuesday, February 19th 2019, 10:03:07 am
# @Last modified by:   shadabKhan
# @Last modified time: Monday, March 4th 2019, 12:22:05 pm



import os

from flask import Flask, session
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


@app.route("/layout/index.html")
def index():
    return "Project 1: TODO"
