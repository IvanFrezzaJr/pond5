from flask import Blueprint

from .resources import IndexResource
from .resources.media import (
    create_media, 
    list_media, 
    get_media_by_id,
    delete_media_by_id,
    update_media_by_id
)

bp = Blueprint("restapi", __name__, url_prefix="/api/v1")

def init_app(app):
    bp.add_url_rule('/', 'index', IndexResource)
    bp.add_url_rule('/media', 'create_media', create_media, methods=['POST'])
    bp.add_url_rule('/media', 'list_media', list_media, methods=['GET'])
    bp.add_url_rule('/media/<id>', 'get_media_by_id', get_media_by_id, methods=['GET'])
    bp.add_url_rule('/media/<id>', 'delete_media_by_id', delete_media_by_id, methods=['DELETE'])
    bp.add_url_rule('/media/<id>', 'update_media_by_id', update_media_by_id, methods=['PUT'])

    app.register_blueprint(bp)
    
   


