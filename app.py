from app import app, db
from app.models import User, Logs, HC


@app.shell_context_processor
def make_shell_context():
    return {'db': db, 'User': User, 'Log': Logs, 'HC': HC}

