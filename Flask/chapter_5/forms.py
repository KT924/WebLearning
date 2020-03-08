from flask_wtf import FlaskForm
from wtforms import TextAreaField,SubmitField
from wtforms.validators import DataRequired,Length

class NoteForm(FlaskForm):
    body=TextAreaField('Body',validators=[DataRequired()])
    submit=SubmitField('Save')