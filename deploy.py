"""Initial database configuration.

Note:
    This file does roughly the same as running ``python cli.py db_create``, but
    does't require reconfiguring the connection credentials for alembic
"""
from pybossa.core import create_app, db
from pybossa.model.category import Category


with create_app(run_as_server=False).app_context():
    category = Category(
        name="Main",
        short_name="main",
        description=""
    )
    db.create_all()
    if not db.session.query(Category).count():
        db.session.add(category)
    db.session.commit()
