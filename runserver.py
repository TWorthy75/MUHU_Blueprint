from flask import app
from muhu_project import create_app

app = create_app()

if __name__ == "__main__":
    app.run('localhost', 5555)