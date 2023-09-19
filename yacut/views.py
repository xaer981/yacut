from http import HTTPStatus

from flask import abort, flash, redirect, render_template

from . import app
from .constants import INDEX_TEMPLATE
from .error_handlers import ValidationError
from .forms import URLForm
from .models import URLMap
from .utils import add_urlmap


@app.route('/', methods=['GET', 'POST'])
def index_view():
    form = URLForm()
    if form.validate_on_submit():
        short = form.custom_id.data
        original = form.original_link.data

        try:
            url_map = add_urlmap(original=original,
                                 short=short,
                                 index_view=True)

            return render_template(INDEX_TEMPLATE,
                                   form=form,
                                   short=url_map.get_absolute_short())

        except ValidationError as error:
            flash(error)

    return render_template(INDEX_TEMPLATE, form=form)


@app.route('/<short>')
def short_to_full_view(short):
    object = URLMap.query.filter_by(short=short).first()
    if not object:
        abort(HTTPStatus.NOT_FOUND)

    return redirect(object.original)
