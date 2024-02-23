from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from my_app.main import app  

# adding configuration for using a sqlite database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///project.db'

# Creating an SQLAlchemy instance
db = SQLAlchemy()
migrate = Migrate(app, db) # database migrations are used to keep the database up to date when new models are added or existing ones are changed

# Models
class Post(db.Model):
    # id : Field which stores unique id for every post in database table
    # created_at: Date and time at which the bot was called
    # account_id: User ID of the account which called the bot
    # root_id: Comment ID of the original post

    id = db.Column(db.Integer, primary_key=True)
    created_at = db.Column(db.DateTime, unique=False, nullable=False)
    account_id = db.Column(db.String(), unique=False, nullable=False)
    root_id = db.Column(db.String(), unique=False, nullable=False)

    # repr method represents how one object of this datatable will look like
    def __repr__(self):
        return f"ID: {self.id}, created_at: {self.created_at}, account_id: {self.account_id}, root_id: {self.root_id}"
