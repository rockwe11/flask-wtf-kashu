from flask_wtf import FlaskForm
from flask_wtf.file import FileRequired
from wtforms import SubmitField, FileField
from wtforms.validators import DataRequired


class LoadIMGForm(FlaskForm):
    file = FileField('Выберите файл', validators=[FileRequired()])
    submit = SubmitField('Отправить')
