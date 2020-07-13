import falcon

from app.middleware import middleware
from app.resources.jwt_resources import JWTAuthenticateResource
from app.resources.joke_resources import JokeResource


def create():
    # Create the Falcon API Object
    api = falcon.API(middleware=middleware)

    # Setup the URL Routing for each Resource Class
    api.add_route('/api/authenticate', JWTAuthenticateResource())
    api.add_route('/api/joke', JokeResource())

    return api


# Create Falcon App
api = create()
