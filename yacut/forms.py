from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, URLField
from wtforms.validators import DataRequired, Length, Optional, Regexp

from .constants import URL_PATTERN


class URLForm(FlaskForm):
    original_link = URLField('Добавьте ссылку, которую нужно сократить',
                             validators=[
                                 DataRequired(
                                     message='Обязательное поле'),
                                 Length(
                                     1,
                                     256,
                                     message=('Длина должна быть '
                                              'от 1 до 256 символов')),
                                 Regexp(
                                     URL_PATTERN,
                                     message=('Данный текст '
                                              'не является ссылкой'))])
    custom_id = StringField('Ваш вариант короткой ссылки',
                            validators=[Optional(),
                                        Length(1, 16)])
    submit = SubmitField('Создать')