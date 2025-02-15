from flask_wtf import FlaskForm
from wtforms import StringField, SelectField, SubmitField, IntegerField, TextAreaField
from wtforms.validators import DataRequired, Length, Optional


class PrescriptionForm(FlaskForm):

    patient_name = StringField('patient_name', validators=[DataRequired(), Length(min=5,max=120 )])
    patient_age = IntegerField('patient_age', validators=[DataRequired()])
    patient_sex = SelectField('patient_sex', choices=[
        ('male', 'Male'),
        ('female', 'Female'),
        ('other', 'Other')
    ])
    cc = StringField('cc',validators=[Optional()])
    bp = StringField('bp',validators=[Optional()])
    pulse = StringField('pulse',validators=[Optional()])
    temp = StringField('temp',validators=[Optional()])
    spo = StringField('spo',validators=[Optional()])
    inv = StringField('inv',validators=[Optional()])
    rx = TextAreaField('rx',validators=[DataRequired()])
    advice = StringField('advice',validators=[Optional()])

    submit = SubmitField('Prescribe')