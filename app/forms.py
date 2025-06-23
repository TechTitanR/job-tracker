from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, SelectField, TextAreaField, DateField
from wtforms.validators import DataRequired, Email, EqualTo, Length, URL, Optional

class RegistrationForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired(), Length(min=4, max=150)])
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired(), Length(min=6)])
    confirm_password = PasswordField('Confirm Password', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Register')

class LoginForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Login')

class ApplicationForm(FlaskForm):
    company_name = StringField('Company Name', validators=[DataRequired()])
    job_title = StringField('Job Title', validators=[DataRequired()])
    application_date = DateField('Application Date', format='%Y-%m-%d')
    status = SelectField('Status', choices=[('Applied', 'Applied'), ('Interview', 'Interview'), ('Offer', 'Offer'), ('Rejected', 'Rejected')])
    notes = TextAreaField('Notes', validators=[Optional()])
    application_link = StringField('Application Link', validators=[Optional(), URL()])
    submit = SubmitField('Save')