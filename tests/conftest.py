
import pytest
import os

from dotenv import load_dotenv
dotenv_path = os.path.abspath(__file__ + "/../../.env")
load_dotenv(dotenv_path=dotenv_path)  # take environment variables from .flaskenv

from pond5.app import create_app
from pond5.ext.database import db as _db
@pytest.fixture(scope="session")
def app(request):
    """Test session-wide test `Flask` application."""

    app = create_app("test")
    return app


@pytest.fixture(scope="session")
def db(app, request):
    """Returns session-wide initialized database"""
    with app.app_context():
        _db.create_all()
        yield _db
        _db.drop_all()


@pytest.fixture(scope="function")
def session(app, db, request):
    """Creates a new database session for each test, rolling back changes afterwards"""
    connection = _db.engine.connect()
    transaction = connection.begin()

    options = dict(bind=connection, binds={})
    session = _db.create_scoped_session(options=options)

    _db.session = session

    yield session

    transaction.rollback()
    connection.close()
    session.remove()


@pytest.fixture(scope="function")
def client(app, session, monkeypatch):
    return app.test_client()


