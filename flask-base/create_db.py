from web_app import app,db

def init_db():
    with app.app_context():
        db.reflect()
        db.drop_all()
        db.create_all()

init_db()