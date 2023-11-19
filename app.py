from flask import Flask
from api.admin import bp as admin
from api.user import bp as user
from extensions import db

app = Flask(__name__)
app.config.from_pyfile('settings.py')
db.init_app(app)

app.register_blueprint(admin, url_prefix='/admin')
app.register_blueprint(user, url_prefix='/u')

app.run(debug=True)