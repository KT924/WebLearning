from flask import Flask
import config
import click
from flask_sqlalchemy import SQLAlchemy
from forms import NoteForm
from flask import flash,redirect,url_for,render_template

app=Flask(__name__)
app.secret_key="DEV"
app.config.from_object(config)
db=SQLAlchemy(app)
from models import Note


@app.cli.command()
def initdb():
    db.create_all()
    click.echo('Initialized database.')


@app.route('/new',methods=['GET','POST'])
def new_note():
    form = NoteForm()
    if form.validate_on_submit():
        body=form.body.data
        note= Note(body=body)
        db.session.add(note)
        db.session.commit()
        flash('Your note is saved')
        return redirect(url_for('index'))
    return render_template('new_note.html',form=form)


@app.route('/index')
def index():
    notes=Note.query.all()
    return render_template('index.html',notes=notes)