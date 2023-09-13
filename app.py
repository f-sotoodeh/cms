from flask import flask
from api.user import bp as user

app = Flask(__name__)

app.register_blueprint(user, url_prefix='/user')

app.run(debug=True)