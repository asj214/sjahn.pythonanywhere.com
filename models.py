from app import db
from orator import Model, SoftDeletes
from orator.orm import belongs_to, has_one, has_many


Model.set_connection_resolver(db)

class User(SoftDeletes, Model):
    __table__ = 'users'
    __fillable__ = ['email', 'name', 'last_login_at']
    __dates__ = ['deleted_at']

    # @has_many
    # def posts(self):
    #     return Post