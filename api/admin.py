from flask import Blueprint, request, jsonify

from models import Test, User

bp = Blueprint('admin', __name__)


@bp.post('/login/')
def login():
    try:
        username = request.json.get('username')
        password = request.json.get('password')
        user = User.objects.get(username=username)
        if user.check_password(password):
            token = user.set_token()
            success = True
            message = 'You are logged in.'
            data = dict(token=token)
            status = 200
        else:
            raise Exception('Invalid username or password!')
    except Exception as e:
        success = False
        message = str(e)
        data = dict()
        status = 500
    return jsonify(success=success, message=message, data=data), status


@bp.post('/test/')
def test_post():
    try:
        Test(**request.json).save()
        success = True
        message = ''
        data = dict()
        status = 200
    except Exception as e:
        success = False
        message = str(e)
        data = dict()
        status = 500
    return jsonify(success=success, message=message, data=data), status

@bp.get('/test/')
@bp.get('/test/<id>/')
def test_get(id=None):
    try:
        if id==None:
            data = dict(
                items=[obj.as_dict() for obj in Test.objects],
                count=Test.objects.count(),
            )
        else:
            data = Test.objects.get(id=id).as_dict()
        success = True
        message = ''
        data = data
        status = 200
    except Exception as e:
        success = False
        message = str(e)
        data = dict()
        status = 500
    return jsonify(success=success, message=message, data=data), status

@bp.put('/test/<id>/')
def test_put(id):
    try:
        obj = Test.objects.get(id=id)
        obj.update(**request.json)
        success = True
        message = 'Object has been updated successfully.'
        data = dict()
        status = 200
    except Exception as e:
        success = False
        message = str(e)
        data = dict()
        status = 500
    return jsonify(success=success, message=message, data=data), status

@bp.delete('/test/<id>/')
def test_delete(id):
    try:
        token = request.headers['Authorization'][7:]
        if token != 'qwertyuiop':
            raise Exception('You are not authorized.')

        Test.objects.get(id=id).delete()
        success = True
        message = 'Object has been deleted successfully.'
        data = dict()
        status = 200
    except Exception as e:
        success = False
        message = str(e)
        data = dict()
        status = 500
    return jsonify(success=success, message=message, data=data), status