from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager
import os
# admin
from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView


db = SQLAlchemy()
migrate = Migrate()


def create_app():
    app = Flask(__name__, template_folder='templates', )
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///app.db"
    db.init_app(app)

    # csrf secret key settings
    WTF_CSRF_SECRET_KEY = 'test'
    app.config['SECRET_KEY'] = WTF_CSRF_SECRET_KEY

    # all models    
    from app.account.models import RegistrationModel
    from app.dashboard.models import ProfileSetupModel
    from app.pdf.models import PrescriptionModel

    # flask login
    login_manager = LoginManager()
    login_manager.init_app(app)

    @login_manager.user_loader
    def load_user(uid):
        return RegistrationModel.query.get(uid)
    
    
    # signature upload settings
    app.config['UPLOAD_FOLDER'] = os.path.join(app.root_path, 'static', 'uploads')
    # Ensure the upload folder exists
    os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)
    # Optional: limit file size to 16MB
    app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024


    # admin panel settings
    admin = Admin(app, name='DocMed-Admin-Panel')
    admin.add_view(ModelView(RegistrationModel, db.session))
    admin.add_view(ModelView(ProfileSetupModel, db.session))
    admin.add_view(ModelView(PrescriptionModel, db.session))


    # importing blueprints
    from app.home.routes import home
    from app.account.routes import accounts
    from app.dashboard.routes import dashboard
    from app.pdf.routes import pdf_generator

    # register blueprints
    app.register_blueprint(home, url_prefix='/')
    app.register_blueprint(accounts, url_prefix='/account')
    app.register_blueprint(dashboard, url_prefix='/dashboard')
    app.register_blueprint(pdf_generator, url_prefix='/pdf')

    migrate.init_app(app, db)
    return app

