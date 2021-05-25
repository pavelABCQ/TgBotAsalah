from flask_wtf import FlaskForm
from wtforms import PasswordField, SubmitField, StringField
from wtforms.validators import DataRequired



class RegForm(FlaskForm):
    password = PasswordField("Ваш пароль:", validators= [DataRequired()])
    username = StringField("Имя:", validators= [DataRequired()])
    submit = SubmitField("Зарегистрироваться")