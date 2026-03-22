import os
import sys
from flask import Flask, render_template, request, redirect, url_for
from user_dashboard.models import User, Post
from user_dashboard.extensions import db, mail

def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(f'config.{config_name}')
    db.init_app(app)
    mail.init_app(app)
    with app.app_context():
        db.create_all()
    from user_dashboard.views import main
    app.register_blueprint(main)
    return app

if __name__ == '__main__':
    config_name = os.environ.get('CONFIG_NAME', 'default')
    app = create_app(config_name)
    if sys.platform == 'win32':
        app.run(host='0.0.0.0', use_reloader=False)
    else:
        app.run(host='0.0.0.0')