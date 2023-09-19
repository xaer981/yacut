import random
import re
import string
from typing import Optional

from . import db
from .constants import URL_PATTERN, RANDOM_SHORT_MAX_LENGTH
from .error_handlers import ValidationError
from .models import URLMap
from .validators import validate_links


def add_urlmap(original: str, short: str, index_view: bool = False) -> URLMap:
    if error := validate_links(original=original,
                               short=short,
                               index_view=index_view):

        raise ValidationError(error)

    if existing_object := URLMap.query(original=original).first():

        return existing_object

    url_map = URLMap(original=original,
                     short=short or gen_unique_random_uri())
    db.session.add(url_map)
    db.session.commit()

    return url_map


def gen_unique_random_uri() -> str:
    pool = tuple(string.ascii_letters + string.digits)

    random_short = ''.join(str(char)
                           for char in random.sample(pool,
                                                     RANDOM_SHORT_MAX_LENGTH))

    if URLMap.query.filter_by(short=random_short).first():

        return gen_unique_random_uri()

    return random_short


def url_is_valid(url) -> Optional[re.Match]:

    return re.compile(URL_PATTERN).match(url)
