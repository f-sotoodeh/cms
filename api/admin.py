from datetime import datetime

from flask import Blueprint, g, request, jsonify

from models import Article, User
from mods.auth import auth
from mods.image import make_thumbnail, optimize
from mods.slug import make_slug


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


@bp.post('/a/')
@auth
def article_post():
    try:
        Article(
            title=request.title,
            slug=make_slug(request.title),
            datetime=datetime.now(),
            author=request.author,
            summary=request.summary,
            keywords=request.keywords,
            tags=request.tags,
            cover=optimize(request.cover),
            thumbnail=make_thumbnail(request.cover),
            text=request.text,
        ).save()
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

@bp.get('/a/')
@bp.get('/a/<id>/')
def article_get(id=None):
    try:
        if id==None:
            data = dict(
                items=[obj.as_dict(mode='short') for obj in Article.objects],
                count=Article.objects.count(),
            )
        else:
            data = Article.objects.get(id=id).as_dict(mode='full')
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

@bp.put('/a/<id>/')
@auth
def article_put(id):
    try:
        obj = Article.objects.get(id=id)
        obj.update(**request.json)
        success = True
        message = 'Article has been updated successfully.'
        data = dict()
        status = 200
    except Exception as e:
        success = False
        message = str(e)
        data = dict()
        status = 500
    return jsonify(success=success, message=message, data=data), status

@bp.delete('/a/<id>/')
@auth
def article_delete(id):
    try:
        Article.objects.get(id=id).delete()
        success = True
        message = 'Article has been deleted successfully.'
        data = dict()
        status = 200
    except Exception as e:
        success = False
        message = str(e)
        data = dict()
        status = 500
    return jsonify(success=success, message=message, data=data), status