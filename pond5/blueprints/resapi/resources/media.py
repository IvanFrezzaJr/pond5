from flask import request, make_response, jsonify
from pond5.ext.database.models import Media, MediaSchema
from marshmallow.exceptions import ValidationError

def create_media():
   data = request.get_json()
   media_schema = MediaSchema()
   try:
      media = media_schema.load(data)
      created_media = Media.create(media)
      result =  media_schema.dump(created_media) 
      return make_response(jsonify({"media": result}), 201)

   except ValidationError as e:
      return make_response(jsonify({"error": str(e)}))


def list_media():
    get_medias = Media.get_all()
    media_schema = MediaSchema(many=True)
    medias = media_schema.dump(get_medias)
    return make_response(jsonify({"medias": medias}))


def get_media_by_id(id):
   get_media = Media.get_by_id(id)
   media_schema = MediaSchema()
   media = media_schema.dump(get_media)
   return make_response(jsonify({"media": media}))


def delete_media_by_id(id):
   Media.delete_by_id(id)
   return make_response("", 204)


def update_media_by_id(id):
   data = request.get_json()
   get_media = Media.update_by_id(id, data)
   media_schema = MediaSchema()
   media = media_schema.dump(get_media)

   return make_response(jsonify({"media": media}))


