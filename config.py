## Description: This file acts like an ORM(Object Relational Mapping) basically normal python code use karke databse ko modify ya update kiya jaa sakta hai
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
import os

app = Flask(__name__)
CORS(app) # lets us initialise cross-origin requests now pehle error hota tha
app.config["SQLALCHEMY_DATABASE_URI"] = f"sqlite:///{os.path.abspath('mydatabase.db')}" # storing the database file essentially
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False # agar database modify kiya toh uska track nahi rakega
 
db = SQLAlchemy(app) #instance of database taaki databsae access kar sake