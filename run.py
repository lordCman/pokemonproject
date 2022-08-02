from app import app
from app.models import User, Pokemon, db

@app.shell_context_processor
def shell_context():
    return {"db": db, 'User': User, 'Pokemon': Pokemon}


if __name__ == '__main__':
    app.run()