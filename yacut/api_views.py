from http import HTTPStatus

from flask import jsonify, request

from . import app
from .error_handlers import InvalidAPIUsage
from .models import URLMap
from .utils import add_urlmap
from .validators import validate_links


@app.route('/api/id/', methods=['POST'])
def add_url():
    data = request.get_json()

    if not data:

        raise InvalidAPIUsage('Отсутствует тело запроса')

    original = data.get('url')
    short = data.get('custom_id')

    if error := validate_links(original=original,
                               short=short):

        raise InvalidAPIUsage(error)

    url_map = add_urlmap(original=original,
                         short=short)

    return jsonify(url_map.to_dict()), HTTPStatus.CREATED


@app.route('/api/id/<short_id>/')
def get_full_from_short(short_id):
    object = URLMap.query.filter_by(short=short_id).first()
    if not object:

        raise InvalidAPIUsage('Указанный id не найден', HTTPStatus.NOT_FOUND)

    return jsonify({'url': object.original}), HTTPStatus.OK