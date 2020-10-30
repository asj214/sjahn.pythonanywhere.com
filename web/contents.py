import os
import uuid
from datetime import datetime
from werkzeug.utils import secure_filename
from flask import Blueprint, session, request, redirect, render_template, url_for, jsonify
from models import Banner, Attachment
from forms import BannerForm


blueprint = Blueprint('contents', __name__)
UPLOAD_DIR = os.getenv('UPLOAD_DIR')

@blueprint.route('/banners/create', methods=['GET', 'POST'])
def banner_create():

    if not 'auth' in session:
        return redirect(url_for('auth.login', redirect_url=request.url))

    form = BannerForm()
    if form.validate_on_submit():

        banner = Banner.create(
            category_id=form.category_id.data,
            user_id=session['auth']['id'],
            subject=form.subject.data,
            link=form.link.data,
            description=form.description.data
        )

        if form.attachment.data:
            now = datetime.now().strftime('%Y%m')
            filename = secure_filename(form.attachment.data.filename)

            # upload directory create
            directory = '{0}/static/attachments/{1}'.format(UPLOAD_DIR, now)
            if not os.path.exists(directory):
                os.makedirs(directory)

            save_filename = uuid.uuid4().hex + '.' + filename.rsplit('.', 1)[1].lower()

            path = os.path.join(directory, save_filename)
            form.attachment.data.save(path)

            Attachment.create(
                attachment_id=banner.id,
                attachment_type='banners',
                url=path.replace(UPLOAD_DIR, ''),
                user_id=session['auth']['id'],
                filename=form.attachment.data.filename
            )
        
        return redirect(url_for('contents.banner_index'))

    return render_template('banners/form.html', form=form)


@blueprint.route('/banners', methods=['GET'])
def banner_index():

    if not 'auth' in session:
        return redirect(url_for('auth.login', redirect_url=request.url))

    page = int(request.args.get('page', 1))
    per_page = request.args.get('per_page', 20)

    banners = Banner.with_('user', 'attachment').order_by('id', 'desc').paginate(per_page, page)

    return render_template('banners/index.html', banners=banners)


@blueprint.route('/banners/<int:pk>', methods=['GET'])
def banner_show(pk):

    if not 'auth' in session:
        return redirect(url_for('auth.login', redirect_url=request.url))

    banner = Banner.with_('user', 'attachment').find_or_fail(pk)

    return render_template('banners/show.html', banner=banner)


@blueprint.route('/banners/<int:pk>/edit', methods=['GET', 'POST'])
def banner_edit(pk):

    if not 'auth' in session:
        return redirect(url_for('auth.login', redirect_url=request.url))

    banner = Banner.with_('user', 'attachment').find_or_fail(pk)
    form = BannerForm(obj=banner)

    if request.method == 'POST' and form.validate_on_submit():
        banner.category_id = form.category_id.data
        banner.user_id = session['auth']['id']
        banner.subject = form.subject.data
        banner.link = form.link.data
        banner.description = form.description.data
        banner.save()

        if form.attachment.data:
            now = datetime.now().strftime('%Y%m')
            filename = secure_filename(form.attachment.data.filename)

            # upload directory create
            directory = '{0}/static/attachments/{1}'.format(UPLOAD_DIR, now)
            if not os.path.exists(directory):
                os.makedirs(directory)

            save_filename = uuid.uuid4().hex + '.' + filename.rsplit('.', 1)[1].lower()

            path = os.path.join(directory, save_filename)
            form.attachment.data.save(path)

            attachment = Attachment()
            attachment.attachment_type = 'banners'
            attachment.attachment_id = banner.id
            attachment.url = path.replace(UPLOAD_DIR, '')
            attachment.user_id = session['auth']['id']
            attachment.filename = form.attachment.data.filename
            attachment.save()

        return redirect(url_for('contents.banner_show', pk=banner.id))

    return render_template('banners/form.html', form=form)


@blueprint.route('/banners/<int:pk>', methods=['DELETE'])
def banner_destroy(pk):

    if not 'auth' in session:
        return redirect(url_for('auth.login', redirect_url=request.url))

    banner = Banner.find_or_fail(pk)
    attachments = Attachment.where('attachment_id', banner.id).where('attachment_type', 'banners').update(deleted_at=datetime.now())
    banner.delete()

    return jsonify({'status': 200, 'msg': 'ok'})