from app import create_app, db, cli
from app.models import User, Post, Message, Notification

app = create_app()
cli.register(app)

# generates the imports using flask shell command
@app.shell_context_processor
def make_shell_context():
    return {'db': db, 'User': User, 'Post': Post, 'Message': Message, 'Notification': Notification}