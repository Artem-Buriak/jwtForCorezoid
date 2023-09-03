import jwt
from cryptography.hazmat.primitives import serialization

payload_data = {
    "iat": 1696083454,
    "exp": 1696083454,
    "jti": "d793ccbb",
    "application_id": "ba6a8954-46aa-4f7e-beda-7c77ed718285"
}

key = open('private.key').read()

token = jwt.encode(
    payload=payload_data,
    key=key,
    algorithm='RS256'
)


def handle(data):
    data["token"] = token
    return data
