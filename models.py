from extensions import db


class User(db.Document):
    username = db.StringField()
    password = db.StringField

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
