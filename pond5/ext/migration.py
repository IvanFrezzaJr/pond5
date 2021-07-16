
  
from flask_migrate import Migrate
from pond5.ext.database import db

from pond5.ext.database import models
migrate = Migrate()


def init_app(app, _db=None):
    if _db:
        migrate.init_app(app, _db)
    migrate.init_app(app, db)

