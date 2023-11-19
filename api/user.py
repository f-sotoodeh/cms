from flask import Blueprint, jsonify

bp = Blueprint('user', __name__)


@bp.get('/test/')
def test():
    data = [1,2,3,4,5]
    return jsonify(success=True, message='abc', data=data), 200

