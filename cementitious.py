from app import app, db
from app.models import User, Post, Vehicle


@app.shell_context_processor
def make_shell_context():
    return {'db': db, 'User': User, 'Post': Post, 'Vehicle': Vehicle}