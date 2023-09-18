from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, URLField
from wtforms.validators import DataRequired, Length, Optional, Regexp

from .constants import (CUSTOM_ID_MAX_LENGTH, CUSTOM_ID_MIN_LENGTH,
                        LENGHT_ERROR, LINK_MAX_LENGTH, LINK_MIN_LENGTH,
                        URL_PATTERN)


class URLForm(FlaskForm):
    original_link = URLField('Добавьте ссылку, которую нужно сократить',
                             validators=[
                                 DataRequired(
                                     message='Обязательное поле'),
                                 Length(
                                     LINK_MIN_LENGTH,
                                     LINK_MAX_LENGTH,
                                     message=(
                                         LENGHT_ERROR.format(
                                             min=LINK_MIN_LENGTH,
                                             max=LINK_MAX_LENGTH
                                         )
                                     )
                                 ),
                                 Regexp(
                                     URL_PATTERN,
                                     message=('Данный текст '
                                              'не является ссылкой'))])
    custom_id = StringField('Ваш вариант короткой ссылки',
                            validators=[Optional(),
                                        Length(
                                            CUSTOM_ID_MIN_LENGTH,
                                            CUSTOM_ID_MAX_LENGTH,
                                            message=(
                                                LENGHT_ERROR.format(
                                                    min=CUSTOM_ID_MIN_LENGTH,
                                                    max=CUSTOM_ID_MAX_LENGTH
                                                )
                                            ))])
    submit = SubmitField('Создать')