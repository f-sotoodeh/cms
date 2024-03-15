from extensions import db
from string import ascii_letters, digits
from random import choices
from uuid import uuid4
from werkzeug.security import generate_password_hash, check_password_hash


class User(db.Document):
    username = db.StringField()
    password = db.StringField()
    token = db.StringField()
    meta = dict(indexes=['username', 'token'])

    def set_token(self):
        chars = ascii_letters + digits
        token = ''.join(choices(chars, k=40)) + uuid4().hex
        self.update(token=token)
        return token
   
    def set_password(self, password):
        self.update(password=generate_password_hash(password, method='scrypt'))

    def check_password(self , password):
        return check_password_hash(self.password, password)

    def as_dict(self):
        return dict(
            id=str(self.id),
            username=self.test_name,
        )


class Test(db.Document):
    test_name = db.StringField()
    test_data = db.StringField()

    def as_dict(self):
        return dict(
            id=str(self.id),
            test_name=self.test_name,
            test_data=self.test_data,
        )


class Article(db.Document):
    title = db.StringField()
    slug = db.StringField()
    datetime = db.DatetimeField()
    author = db.StringField()
    summary = db.StringField()
    keywords = db.ListField(db.StringField())
    tags = db.ListField(db.StringField())
    thumbnail = db.StringField()
    cover = db.StringField()
    text = db.StringField()

    meta = dict(
        indexes=['slug', 'datetime']
    )

    def as_dict(self, mode):
        if mode == 'short':
            return dict(
                id=str(self.id),
                title=self.title,
                datetime=self.datetime,
                author=self.author,
                summary=self.summary,
                keywords=self.keywords,
                thumbnail=self.thumbnail,
            )
        elif mode == 'full':
            return dict(
                id=str(self.id),
                title=self.title,
                datetime=self.datetime,
                author=self.author,
                summary=self.summary,
                keywords=self.keywords,
                tags=self.tags,
                cover=self.cover,
                text=self.text,
            )