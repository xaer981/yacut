from http import HTTPStatus

from flask import jsonify, render_template

from . import app, db
from .constants import INTERNAL_SERVER_ERROR_TEMPLATE, NOT_FOUND_TEMPLATE


class InvalidAPIUsage(Exception):
    status_code = HTTPStatus.BAD_REQUEST

    def __init__(self, message, status_code=None):
        super().__init__()
        self.message = message
        if status_code is not None:
            self.status_code = status_code

    def to_dict(self):

        return dict(message=self.message)


class ValidationError(Exception):
    def __init__(self, message: str):
        super().__init__()
        self.message = message


@app.errorhandler(InvalidAPIUsage)
def invalid_api_usage(error):

    return jsonify(error.to_dict()), error.status_code


@app.errorhandler(HTTPStatus.NOT_FOUND)
def page_not_found(error):

    return render_template(NOT_FOUND_TEMPLATE), HTTPStatus.NOT_FOUND


@app.errorhandler(HTTPStatus.INTERNAL_SERVER_ERROR)
def internal_error(error):
    db.session.rollback()

    return (render_template(INTERNAL_SERVER_ERROR_TEMPLATE),
            HTTPStatus.INTERNAL_SERVER_ERROR)
