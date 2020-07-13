# All Configurations will be here
from dotenv import load_dotenv
from pathlib import Path
from os import getenv

env_path = Path('.') / '.env'
load_dotenv(dotenv_path=env_path)

# Configuration files for JWT Authentication
jwt_secret_key = getenv('APP_JWT_SECRET_KEY')
jwt_algorithm = getenv('APP_JWT_ALGORITHM')
jwt_auth_header_prefix = getenv('APP_JWT_AUTH_HEADER_PREFIX')
jwt_leeway = int(getenv('APP_JWT_LEEWAY'))
jwt_expiration_delta = int(getenv('APP_JWT_EXPIRATION_DELTA'))
