from flask_wtf import Form
from wtforms import StringField, DateField, IntegerField, SelectField
from wtforms.validators import DataRequired


class AddTaskForm(Form):
    task_id = IntegerField()
    name = StringField('Task Name', validators=[DataRequired()])
    due_date = DateField('Due Date (mm/dd/yyyy)', validators=[DataRequired()], format='%m/%d/%Y')
    priority = SelectField(
        "Priority",
        validators=[DataRequired()],
        choices=[
            ('1', '1'), ('2', '2'), ('3', '3')
        ]
    )
    status = IntegerField('Status')

class RegistrationForm(Form):
    name = StringField('Username', validators=[DataRequired(), Length(min=6, max=25)])
    email = StringField('Email', validators=[DataRequired(), Length(min=6, max=25)])
    password = PasswordField('Password', validators=[DataRequired(), Length(min=6, max=25)])
    confirm = PasswordField('Repeat Password', validators=[DataRequired(), EqualTo('password',
                                                                                   message='Passwords must match')])

class LoginForm(Form):
    name = StringField('Username', validators = [DataRequired()])
    password = PasswordField('Password', validators = [DataRequired()])
