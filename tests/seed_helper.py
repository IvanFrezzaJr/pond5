from pond5.ext.database.models import Media
from pond5.ext.database import db

seed_medias_data = [
    {
      "file_name": "file name 1",
      "media_type": "mov",
    },
    {
      "file_name": "file name 2",
      "media_type": "mov",
    },
    {
      "file_name": "file name 3",
      "media_type": "mov",
    },
    {
      "file_name": "file name 4",
      "media_type": "mov",
    },
    {
      "file_name": "file name 5",
      "media_type": "mov",
    }
]

def seed(count=False):
    if count is False:
        count = len(seed_medias_data)
    medias = []
    for i in range(0, count):
        data = seed_medias_data[i]
        category = Media(**data)
        db.session.add(category)
        medias.append(category)
    db.session.commit()

    return medias