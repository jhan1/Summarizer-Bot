from my_app.hashtag import getPosts
from my_app.main import app
from my_app.database import db

# initiate flask app
with app.app_context():
    db.init_app(app)
    post = getPosts()
