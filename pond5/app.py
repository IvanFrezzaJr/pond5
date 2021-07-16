
import os
from flask import Flask
from pond5.ext import database
from pond5.ext import config
from pond5.ext import cors
from pond5.ext import cli
from pond5.ext import migration
from pond5.ext import schema
from pond5.blueprints import resapi
from pond5.blueprints import webui


def minimal_app(env=None):
    app = Flask(__name__)
       
    config.init_app(app, env)
    
    return app


def create_app(env):
    app = minimal_app(env)
    database.init_app(app)
    schema.init_app(app)
    migration.init_app(app)
    cors.init_app(app)
    cli.init_app(app)
    resapi.init_app(app)
    webui.init_app(app)
    return app

