from orator.migrations import Migration


class ModifyBannersTable(Migration):

    def up(self):
        """
        Run the migrations.
        """
        with self.schema.table('banners') as table:
            table.drop_column('url')
            pass

    def down(self):
        """
        Revert the migrations.
        """
        with self.schema.table('banners') as table:
            table.string('url')
            pass
