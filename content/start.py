"""Prepare the upstream native auth format, then exec the original application."""
import base64
import hashlib
import os


def make_native_hash(secret: str, seed: str) -> str:
    salt = hashlib.sha256(seed.encode('utf-8')).digest()
    key = hashlib.pbkdf2_hmac('sha256', secret.encode('utf-8'), salt, 100000)
    return base64.b64encode(salt + key).decode('ascii')


def main() -> None:
    secret = os.environ.pop('CD_LOGIN_SECRET', '')
    seed = os.environ.pop('CD_AUTH_SALT', '')
    if not secret or not seed:
        raise SystemExit('Missing deployment authentication settings; startup aborted.')
    os.environ['SALTED_PASS'] = make_native_hash(secret, seed)
    del secret, seed
    os.chdir('/app')
    os.execvp('python', ['python', './changedetection.py', '-d', '/datastore'])


if __name__ == '__main__':
    main()
