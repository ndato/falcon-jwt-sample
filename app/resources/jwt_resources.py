# API Resources for implementing JWT Authentication
import falcon
from app.middleware import jwt_auth
from app.controllers.cred_checker import cred_checker
from app.settings import jwt_expiration_delta


# Handle JWT Authentication, then granting them Access tokens
class JWTAuthenticateResource:
    # Exempt POST requests from Authentication processes
    auth = {
        'exempt_methods': ['POST']
    }

    def on_post(self, req, resp):
        # Get the Credentials payload by getting the POST request
        # body as a JSON file
        cred_payload = req.media

        # Check Credentials from Request Body if it is a Valid User
        cred = cred_checker(cred_payload)

        if cred is None:
            # If it is not a Valid User, return a 401 Error Response
            raise falcon.HTTPUnauthorized
        else:
            # If it is a valid user, generate and send Access token
            # to the user.
            resp.media = {
                "access_token": jwt_auth.get_auth_token(cred),
                "token_type": "JWT",
                "expires_in": jwt_expiration_delta
            }
