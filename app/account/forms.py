from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, SelectField
from wtforms.validators import DataRequired, Email, EqualTo, Length, Optional

class RegistrationForm(FlaskForm):

    username = StringField('username', validators=[DataRequired(), Length(min=2, max=60)])
    email = StringField('email', validators=[DataRequired(), Email()])
    password = PasswordField('password', validators=[DataRequired(), Length(min=6)])
    confirm_password = PasswordField('confirm_password', validators=[DataRequired(), EqualTo('password',  message='Passwords must match')]) # checking both password matched
    gender = SelectField('gender', choices=[
        ('male', 'Male'),
        ('female', 'Female'),
        ('other', 'Other')
    ])
    validators=[DataRequired(message="Please select your gender.")]

    submit = SubmitField('Register')










class LoginForm(FlaskForm):

    username = StringField('username', validators=[DataRequired()])
    password = PasswordField('password', validators=[DataRequired()])

    login = SubmitField('Login')









class UpdateRegistrationForm(FlaskForm):

    username = StringField('username', validators=[DataRequired(), Length(min=2, max=60)])
    email = StringField('email', validators=[DataRequired(), Email()])
    
    new_password = PasswordField('new_password', validators=[Optional(), Length(min=6)])
    confirm_password = PasswordField('confirm_password', validators=[Optional(), EqualTo('new_password',  message='Passwords must match')]) # checking both password matched
    gender = SelectField('gender', choices=[
        ('male', 'Male'),
        ('female', 'Female'),
        ('other', 'Other')
    ])
    validators=[DataRequired(message="Please select your gender.")]

    update = SubmitField('Update')