from flask import jsonify

def IndexResource():
    return jsonify({"routes": [
        {
            "route": "/api/v1/media",
            "method": "POST",
            "data":  {
                "file_name": "some file name",
                "media_type": "mov"
            }
        },

         {
            "route": "/api/v1/media<id>",
            "method": "DELETE",
        },
        {
            "route": "/api/v1/media<id>",
            "method": "GET",
        },
        {
            "route": "/api/v1/media",
            "method": "GET",
        },
        {
            "route": "/api/v1/media/<id>",
            "method": "PUT",
        }

    ]})


