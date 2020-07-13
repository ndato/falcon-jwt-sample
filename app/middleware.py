# Setup Middlewares for Falcon API
from falcon_auth import FalconAuthMiddleware, JWTAuthBackend
from app.controllers.cred_checker import cred_checker
from app.settings import (
    jwt_secret_key,
    jwt_algorithm,
    jwt_auth_header_prefix,
    jwt_leeway,
    jwt_expiration_delta
)

# Setup falcon-auth JWT Authentication based Middleware
jwt_auth = JWTAuthBackend(
                user_loader=cred_checker,
                secret_key=jwt_secret_key,
                algorithm=jwt_algorithm,
                auth_header_prefix=jwt_auth_header_prefix,
                leeway=jwt_leeway,
                expiration_delta=jwt_expiration_delta,
            )

middleware = [
    FalconAuthMiddleware(jwt_auth)
]
