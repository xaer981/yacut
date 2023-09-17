import re

from flask import jsonify, request

from . import app, db
from .constants import SHORT_PATTERN
from .error_handlers import InvalidAPIUsage
from .models import URLMap
from .utils import gen_unique_random_uri, url_is_valid


@app.route('/api/id/', methods=['POST'])
def add_url():
    data = request.get_json()

    if not data:

        raise InvalidAPIUsage('Отсутствует тело запроса')

    original = data.get('url')
    short = data.get('custom_id')

    if not original:

        raise InvalidAPIUsage('"url" является обязательным полем!')

    if not url_is_valid(original):

        raise InvalidAPIUsage('Данный текст не является ссылкой')

    if short:
        if URLMap.query.filter_by(short=short).first():

            raise InvalidAPIUsage(f'Имя "{short}" уже занято.')

        if len(short) > 16 or not re.compile(SHORT_PATTERN).match(short):

            raise InvalidAPIUsage(
                'Указано недопустимое имя для короткой ссылки')

    if URLMap.query.filter_by(original=original).first():

        raise InvalidAPIUsage('Данная ссылка уже добавлена в базу')

    object = URLMap(original=original,
                    short=short or gen_unique_random_uri())

    db.session.add(object)
    db.session.commit()

    return jsonify(object.to_dict()), 201


@app.route('/api/id/<short_id>/')
def get_full_from_short(short_id):
    object = URLMap.query.filter_by(short=short_id).first()
    if not object:

        raise InvalidAPIUsage('Указанный id не найден', 404)

    return jsonify({'url': object.original}), 200