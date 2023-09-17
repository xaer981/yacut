from flask import abort, flash, redirect, render_template

from . import app, db
from .constants import INDEX_TEMPLATE
from .forms import URLForm
from .models import URLMap
from .utils import gen_unique_random_uri


@app.route('/', methods=['GET', 'POST'])
def index_view():
    form = URLForm()
    if form.validate_on_submit():
        short = form.custom_id.data
        original = form.original_link.data

        if short:
            if URLMap.query.filter_by(short=short).first():
                flash(f'Имя {short} уже занято!')

                return render_template(INDEX_TEMPLATE, form=form)

        if URLMap.query.filter_by(original=original).first():
            flash('Данная ссылка уже добавлена в базу')

            return render_template(INDEX_TEMPLATE, form=form)

        object = URLMap(original=original,
                        short=short or gen_unique_random_uri())
        db.session.add(object)
        db.session.commit()

        return render_template(INDEX_TEMPLATE,
                               form=form,
                               short=object.get_absolute_short())

    return render_template(INDEX_TEMPLATE, form=form)


@app.route('/<short>')
def short_to_full_view(short):
    object = URLMap.query.filter_by(short=short).first()
    if not object:
        abort(404)

    return redirect(object.original)
