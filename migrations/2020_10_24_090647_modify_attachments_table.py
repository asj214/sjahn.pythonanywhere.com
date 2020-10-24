from orator.migrations import Migration


class ModifyAttachmentsTable(Migration):

    def up(self):
        """
        Run the migrations.
        """
        with self.schema.table('attachments') as table:
            table.string('filename').nullable().after('user_id')
            pass

    def down(self):
        """
        Revert the migrations.
        """
        with self.schema.table('attachments') as table:
            table.drop_column('filename')
            pass
