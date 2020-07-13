# API Resources for Sending Joke Requests
from dadjokes import Dadjoke


# Handle Sending Joke Requests
class JokeResource:
    # Method mapped on POST requests
    def on_get(self, req, resp):
        dadjoke = Dadjoke()
        resp.media = dadjoke.joke
