# REQUIREMENTS
* Windows 10
* Docker + Docker compose

# SETUP
run docker-compose up and acces localhost:5000

# USAGE
``` json
{
    "routes": [
        {
            "method": "POST",
            "route": "/api/v1/media",
            "data": {
                "file_name": "some file name",
                "media_type": "mov"
            },
        },
        {
            "method": "DELETE",
            "route": "/api/v1/media<id>"
        },
        {
            "method": "GET",
            "route": "/api/v1/media<id>"
        },
        {
            "method": "GET",
            "route": "/api/v1/media"
        },
        {
            "method": "PUT",
            "route": "/api/v1/media/<id>"
        }
    ]
}
```

In the docs folder there is a [Isomnia json](https://insomnia.rest/). 