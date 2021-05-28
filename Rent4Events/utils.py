from django.contrib.auth import authenticate
import json

import jwt
import requests


def jwt_get_username_from_payload_handler(payload):
    username = payload.get('sub').replace('|', '.')
    authenticate(remote_user=username)
    print('user', username)
    return username


def jwt_decode_token(token):
    header = jwt.get_unverified_header(token)
    print(header)
    jwks = requests.get('https://{}/.well-known/jwks.json'.format('ztw-kl.eu.auth0.com')).json()
    print(jwks)
    public_key = None
    for jwk in jwks['keys']:
        if jwk['kid'] == header['kid']:
            public_key = jwt.algorithms.RSAAlgorithm.from_jwk(json.dumps(jwk))
    if public_key is None:
        raise Exception('Public key not found.')

    issuer = 'https://{}/'.format('ztw-kl.eu.auth0.com')
    print("DECODED", jwt.decode(token, public_key, audience='https://rent-4-events', issuer=issuer, algorithms=['RS256']))
    return jwt.decode(token, public_key, audience='https://rent-4-events', issuer=issuer, algorithms=['RS256'])
