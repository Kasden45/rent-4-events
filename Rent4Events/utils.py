from django.contrib.auth import authenticate
import json

import jwt
import requests


def jwt_get_username_from_payload_handler(payload):
    from django.contrib.auth.models import Group
    print(payload)
    username = payload.get('sub').replace('|', '.')
    permissions = payload.get('permissions')
    user = authenticate(remote_user=username)
    if len(user.groups.all()) == 0:
        # for permission in permissions:
        my_group = Group.objects.get(name='Klient')
        user.groups.add(my_group)
        user.save()
    elif user.groups.filter(name='Klient'):
        print('Is a client', user.groups.all())
    print('user', user.username)
    print('new_user groups')
    for group in user.groups.all():
        print(str(group))
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
