from datetime import datetime

from flask import url_for

from . import db


class URLMap(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    original = db.Column(db.String, nullable=False, unique=True)
    short = db.Column(db.String, nullable=False, unique=True)
    timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow)

    def get_absolute_short(self):

        return url_for('index_view', _external=True) + self.short

    def to_dict(self):

        return dict(url=self.original,
                    short_link=self.get_absolute_short())

    @staticmethod
    def get_object_or_none(original: str = None,
                           short: str = None):
        if original:

            return URLMap.query.filter_by(original=original).first()

        if short:

            return URLMap.query.filter_by(short=short).first()

        return None
