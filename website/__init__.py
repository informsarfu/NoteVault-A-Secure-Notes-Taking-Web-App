from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from os import path
from flask_login import LoginManager

db = SQLAlchemy()
db_name = "database.db"
        
def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = "sazzyBird1998"
    app.config['SQLALCHEMY_DATABASE_URI'] = f"sqlite:///{db_name}"
    db.init_app(app)
    
    from .pages import pages
    from .auth import auth
    
    app.register_blueprint(pages, url_prefix = '/')
    app.register_blueprint(auth, url_prefix = '/')
    
    from .models import User,Note
    
    #check for available db and create if db doesn't exit
    with app.app_context():
        db.create_all()
        
    login_manager = LoginManager()
    login_manager.login_view = "auth.login"
    login_manager.init_app(app)
    
    @login_manager.user_loader
    def load_user(id):
        return User.query.get(int(id))
    
    return app