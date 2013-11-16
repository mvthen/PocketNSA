from google.appengine.ext import db


class Company(db.Model):
    name = db.StringProperty(required=True)
    number = db.StringProperty(required=True)