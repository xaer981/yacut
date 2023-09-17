import random
import re
import string

from .constants import URL_PATTERN
from .models import URLMap


def gen_unique_random_uri():
    pool = tuple(string.ascii_letters + string.digits)

    random_short = ''.join(str(char) for char in random.sample(pool, 6))

    if URLMap.query.filter_by(short=random_short).first():

        return gen_unique_random_uri()

    return random_short


def url_is_valid(url):

    return re.compile(URL_PATTERN).match(url)
