from orator.migrations import Migration


class CreateBannersTable(Migration):

    def up(self):
        """
        Run the migrations.
        """
        with self.schema.create('banners') as table:
            table.increments('id')
            table.integer('category_id').default(1)
            table.big_integer('user_id')
            table.string('subject')
            table.string('url')
            table.string('link').nullable()
            table.text('description').nullable()
            table.timestamps()
            table.soft_deletes()

    def down(self):
        """
        Revert the migrations.
        """
        self.schema.drop('banners')
