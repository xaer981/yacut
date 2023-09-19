import re
from typing import Optional

from .constants import SHORT_PATTERN, CUSTOM_ID_MAX_LENGTH
from .models import URLMap
from .utils import url_is_valid


def validate_links(original: str,
                   short: str,
                   index_view: bool) -> Optional[str]:
    if not original:

        return '"url" является обязательным полем!'

    if not url_is_valid(original):

        return 'Данный текст не является ссылкой'

    if short:
        if URLMap.query.filter_by(short=short).first():
            # Костыль из-за разных требований
            # к сообщению об ошибке в тестах к проекту.

            return (f'Имя {short} уже занято!' if index_view
                    else f'Имя "{short}" уже занято.')

        if (len(short) > CUSTOM_ID_MAX_LENGTH or
           not re.compile(SHORT_PATTERN).match(short)):

            return 'Указано недопустимое имя для короткой ссылки'

    if URLMap.query.filter_by(original=original).first():

        return 'Данная ссылка уже добавлена в базу'