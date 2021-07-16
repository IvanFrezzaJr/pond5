from pond5.ext.database import db
from pond5.ext.database.base import Base
from marshmallow import Schema
from marshmallow.fields import  String, DateTime, Int
class Media(Base):
    __tablename__ = 'media'
    file_name = db.Column(db.String(128))
    media_type  = db.Column(db.String(128))


class MediaSchema(Schema):
    class Meta:
        ordered = True
        model = Media
    id = Int(dump_only=True, metadata={"description":"table unique identifier", "example":123})
    file_name = String(metadata={"description": "file desription", "example":"Pond5 Digital Watermark"})
    media_type = String(metadata={"description": "file extension", "example":"mov"})
    created_at = DateTime(dump_only=True, metadata={"description": "Datetime was created", "example":"2021-07-15T19:45:22"})
    updated_at = DateTime(dump_only=True, metadata={"description": "Last time was updated", "example":"2021-07-15T19:45:22"})
