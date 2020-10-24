from app import db
from orator import Model, SoftDeletes
from orator.orm import belongs_to, has_one, has_many


Model.set_connection_resolver(db)

class User(SoftDeletes, Model):
    __table__ = 'users'
    __fillable__ = ['email', 'name', 'last_login_at']
    __dates__ = ['deleted_at']


class Banner(SoftDeletes, Model):
    __table__ = 'banners'
    __fillable__ = ['subject', 'url', 'link', 'description']
    __dates__ = ['deleted_at']

    @belongs_to('user_id', 'id')
    def user(self):
        return User

    @has_one('attachment_id', 'id')
    def attachment(self):
        return Attachment.where('attachment_type', 'banners').order_by('id', 'desc')


class Attachment(SoftDeletes, Model):
    __table__ = 'attachments'
    __dates__ = ['deleted_at']

    @belongs_to('user_id', 'id')
    def user(self):
        return User