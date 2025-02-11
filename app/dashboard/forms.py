from flask_wtf import FlaskForm
from wtforms import StringField, DateField, SelectField, SubmitField, FileField
from wtforms.validators import DataRequired, Length, Optional
from flask_wtf.file import FileField, FileAllowed, FileRequired


class ProfileSetUpForm(FlaskForm):

    full_name = StringField('full_name', validators=[DataRequired(), Length(min=5,max=120 )])
    birth_date = DateField('birth_date', validators=[DataRequired()])
    sex = SelectField('gender', choices=[
        ('male', 'Male'),
        ('female', 'Female'),
        ('other', 'Other')
    ])
    achievement = StringField('achieve',validators=[DataRequired()])
    college = StringField('college', validators=[DataRequired()])
    higher_degree = StringField('higher_degree', validators=[Optional()])
    course = StringField('course', validators=[Optional()])
    extra = StringField('extra', validators=[Optional()])
    current_position = StringField('current_position', validators=[DataRequired()])
    govt_reg = StringField('reg_no', validators=[DataRequired()])
    office = StringField('address', validators=[Optional()])
    signature = FileField('sign', validators=[FileAllowed(['jpg', 'jpeg', 'png', 'svg'], 'Images only!'), FileRequired()])

    submit = SubmitField('Submit')










class UpdateProfileSetUpForm(FlaskForm):

    full_name = StringField('full_name', validators=[DataRequired(), Length(min=5,max=120 )])
    birth_date = DateField('birth_date', validators=[DataRequired()])
    sex = SelectField('gender', choices=[
        ('male', 'Male'),
        ('female', 'Female'),
        ('other', 'Other')
    ])
    achievement = StringField('achieve',validators=[DataRequired()])
    college = StringField('college', validators=[DataRequired()])
    higher_degree = StringField('higher_degree', validators=[Optional()])
    course = StringField('course', validators=[Optional()])
    extra = StringField('extra', validators=[Optional()])
    current_position = StringField('current_position', validators=[DataRequired()])
    govt_reg = StringField('reg_no', validators=[DataRequired()])
    office = StringField('address', validators=[Optional()])
    signature = FileField('sign', validators=[FileAllowed(['jpg', 'jpeg', 'png', 'svg'], 'Images only!'), FileRequired()])

    submit = SubmitField('Update Info')