import re
from typing import Optional

from .constants import CUSTOM_ID_MAX_LENGTH, SHORT_PATTERN, URL_PATTERN
from .models import URLMap


def url_is_valid(original: str = None,
                 short: str = None) -> Optional[re.Match]:
    if original:

        return re.compile(URL_PATTERN).match(original)

    if short:

        return re.compile(SHORT_PATTERN).match(short)

    return None


def validate_links(original: str,
                   short: str,
                   index_view: bool) -> Optional[str]:
    if not original:

        return '"url" является обязательным полем!'

    if not url_is_valid(original=original):

        return 'Данный текст не является ссылкой'

    if short:
        if URLMap.get_object_or_none(short=short):
            # Костыль из-за разных требований
            # к сообщению об ошибке в тестах к проекту.

            return (f'Имя {short} уже занято!' if index_view
                    else f'Имя "{short}" уже занято.')

        if (len(short) > CUSTOM_ID_MAX_LENGTH or
           not url_is_valid(short=short)):

            return 'Указано недопустимое имя для короткой ссылки'

    return None