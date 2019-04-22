from flask import Flask, request, redirect, render_template, flash
from flask_sqlalchemy import SQLAlchemy
app = Flask(__name__)
app.config['DEBUG'] = True
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://build-ablog:mypassword@localhost:8889/build-ablog'
app.config['SQLALCHEMY_ECHO'] = True
db = SQLAlchemy(app)


class Blog(db.Model):
   
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(120))
    body = db.Column(db.String(500))
     
    def __init__(self,tiltle,body):
        self.title = title
        self.body = body
    def is_valid(self):
        if self.title and self.body:
            return True
        else:
            return False


      
    