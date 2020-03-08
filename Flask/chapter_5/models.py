
import os
import config
import click
from app import db

class Note(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    body=db.Column(db.Text)

