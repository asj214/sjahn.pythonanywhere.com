from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, DateTimeField, IntegerField, RadioField, SelectField, HiddenField, TextAreaField, FileField, DateField

from wtforms.fields.html5 import EmailField
from wtforms.validators import DataRequired, Email, EqualTo
from constants import BANNER_CATEGORYS


class UserForm(FlaskForm):
    email = EmailField('이메일', validators=[DataRequired(), Email()])
    password = PasswordField('비밀번호', validators=[DataRequired(), EqualTo('password_chk')])
    password_chk = PasswordField('비밀번호 확인', validators=[DataRequired()])
    name = StringField('이름', validators=[DataRequired()])


class LoginForm(FlaskForm):
    email = EmailField('이메일', validators=[DataRequired(), Email()])
    password = PasswordField('비밀번호', validators=[DataRequired()])
    redirect_url = HiddenField('리다이렉트 URL', validators=[])


class BannerForm(FlaskForm):

    # language = SelectField(u'Programming Language', choices=[('cpp', 'C++'), ('py', 'Python'), ('text', 'Plain Text')])
    category_id = SelectField(
        '배너 카테고리',
        coerce=int,
        choices=BANNER_CATEGORYS
    )
    subject = StringField('배너명', validators=[DataRequired()])
    attachment = FileField('배너 이미지')
    link = StringField('링크', validators=[])
    description = TextAreaField('추가 설명', validators=[])