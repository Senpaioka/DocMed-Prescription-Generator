from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager
import os


db = SQLAlchemy()
migrate = Migrate()

def create_app():
    app = Flask(__name__, template_folder='templates', )
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///app.db"
    db.init_app(app)

    # csrf secret key settings
    WTF_CSRF_SECRET_KEY = 'test'
    app.config['SECRET_KEY'] = WTF_CSRF_SECRET_KEY

    # flask login
    login_manager = LoginManager()
    login_manager.init_app(app)

    from app.account.models import RegistrationModel
    @login_manager.user_loader
    def load_user(uid):
        return RegistrationModel.query.get(uid)
    
    
    # signature upload settings
    app.config['UPLOAD_FOLDER'] = os.path.join(app.root_path, 'uploads')
    # Ensure the upload folder exists
    os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)
    # Optional: limit file size to 16MB
    app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024



    # importing blueprints
    from app.home.routes import home
    from app.account.routes import accounts
    from app.dashboard.routes import dashboard

    # register blueprints
    app.register_blueprint(home, url_prefix='/')
    app.register_blueprint(accounts, url_prefix='/account')
    app.register_blueprint(dashboard, url_prefix='/dashboard')


    migrate.init_app(app, db)
    return app


# return filename path
def image_path_link(file_name):
    return os.path.join('uploads', file_name)
