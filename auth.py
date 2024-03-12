"""
    File for authentication
"""

import os
import json

from flask import request
from functools import wraps
from jose import jwt
from urllib.request import urlopen


AUTH0_DOMAIN = os.environ["AUTH0_DOMAIN"]
ALGORITHMS = [os.environ["ALGORITHMS"]]
API_AUDIENCE = os.environ["API_AUDIENCE"]


class AuthError(Exception):
    """
        AuthError Exception
    """
    def __init__(self, error, status_code):
        """
            Constructor for AuthError

            Args:
                error: The error
                status_code: The status code

            Returns:
                None
        """
        self.error = error
        self.status_code = status_code


def get_token_auth_header():
    """
        Get the token from the authorization header

        Args:
            None

        Returns:
            token: The token
    """
    auth_header = request.headers.get("Authorization", None)

    if not auth_header:
        raise AuthError({
            "code": "authorization_header_missing",
            "description": "Authorization header is expected."
        }, 401)

    header_parts = auth_header.split(" ")

    if len(header_parts) != 2 or header_parts[0].lower() != "bearer":
        raise AuthError({
            "code": "invalid_header",
            "description": "Authorization header must be bearer token."
        }, 401)

    token = header_parts[1]

    return token

def check_permissions(permission, payload):
    if "permissions" not in payload:
        raise AuthError({
            "code": "invalid_claims",
            "description": "Permissions not included in JWT."
        }, 400)

    if permission not in payload["permissions"]:
        raise AuthError({
            "code": "unauthorized",
            "description": "Permission not found."
        }, 403)

    return True

def verify_decode_jwt(token):
    jsonurl = urlopen(f"https://{AUTH0_DOMAIN}/.well-known/jwks.json")
    jwks = json.loads(jsonurl.read())
    unverified_header = jwt.get_unverified_header(token)
    rsa_key = {}

    if "kid" not in unverified_header:
        raise AuthError({
            "code": "invalid_header",
            "description": "Authorization malformed."
        }, 401)

    for key in jwks["keys"]:
        if key["kid"] == unverified_header["kid"]:
            rsa_key = {
                "kty": key["kty"],
                "kid": key["kid"],
                "use": key["use"],
                "n": key["n"],
                "e": key["e"]
            }

    if rsa_key:
        print(jwt.decode(token, rsa_key, algorithms=ALGORITHMS, audience=API_AUDIENCE, issuer=f"https://{AUTH0_DOMAIN}/"))
        try:
            payload = jwt.decode(
                token,
                rsa_key,
                algorithms=ALGORITHMS,
                audience=API_AUDIENCE,
                issuer=f"https://{AUTH0_DOMAIN}/"
            )

            return payload

        except jwt.ExpiredSignatureError:
            message = "Token expired."

            raise AuthError({
                "code": "token_expired",
                "description": message
            }, 401)

        except jwt.JWTClaimsError:
            message = "Incorrect claims. Please, check the audience and issuer."

            raise AuthError({
                "code": "invalid_claims",
                "description": message
            }, 401)

        except Exception:
            message = "Unable to parse authentication token."

            raise AuthError({
                "code": "invalid_header",
                "description": message
            }, 400)

    message = "Unable to find the appropriate key."

    raise AuthError({
        "code": "invalid_header",
        "description": message
    }, 400)

def requires_auth(permission=""):
    def requires_auth_decorator(f):
        @wraps(f)
        def wrapper(*args, **kwargs):
            token = get_token_auth_header()

            try:
                payload = verify_decode_jwt(token)
            except:
                raise AuthError({
                    "code": "invalid_token",
                    "description": "Invalid token."
                }, 401)

            check_permissions(permission, payload)

            return f(payload, *args, **kwargs)
        return wrapper
    return requires_auth_decorator
