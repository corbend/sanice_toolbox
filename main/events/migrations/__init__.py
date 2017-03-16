from main.core.models import db

migrator = PostgresqlMigrator(db)

# title_field = CharField(default='')
# status_field = IntegerField(null=True)

# migrate(
#     migrator.add_column('some_table', 'title', title_field),
#     migrator.add_column('some_table', 'status', status_field),
#     migrator.drop_column('some_table', 'old_column'),
# )