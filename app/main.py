# app/main.py
from flask import Flask
from app.views.routes import app as views_app

app = Flask(__name__)
app.register_blueprint(views_app, url_prefix='/')

if __name__ == '__main__':
    app.run(debug=True)
