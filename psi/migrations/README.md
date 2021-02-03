This folder contains all alembic migration for DB schema changes.

Run the flask utility script in app root directory to operate on migrations.

- Show current migration level

  flask db current

- After creating a migration, either manually or as --autogenerate, you must apply it with alembic upgrade head. If you
  used db.create_all() from a shell, you can use alembic stamp head to indicate that the current state of the database
  represents the application of all migrations.

  flask db stamp head

- Generate a migration from current model definition to current DB schema:

  flask db migrate

- Apply migration

  flask db upgrade

- Revert to a previous version

  flask db downgrade

