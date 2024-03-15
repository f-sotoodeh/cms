from functools import wraps

from flask import g, jsonify, request

from models import User


def auth(f):
    @wraps(f)
    def fn(*args, **kw):
        try:
            token = request.headers.get('Authorization', '')
            if token.startswith('Bearer '):
                token = token[7:]
            else:
                raise Exception('Invalid token')
            user = User.objects(token=token).first()
            if not user:
                raise Exception('Invalid token')
            g.user = user
            return f(*args, **kw)
        except Exception as e:
            return jsonify(
                success = False,
                message = str(e),
                data = None,
            ), 401
    return fn

