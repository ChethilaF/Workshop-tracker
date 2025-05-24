from flask import Flask
from flask_login import LoginManager
from app.database import db  # Reverted import
from app.models import User
import os  # Added import for os module

def create_app():
    flask_app = Flask(__name__, instance_relative_config=True)  # Ensure instance-relative config is enabled
    flask_app.secret_key = 'your_secret_key_here'
    flask_app.config['SQLALCHEMY_DATABASE_URI'] = f"sqlite:///{os.path.join(flask_app.instance_path, 'Workshop.db')}"  # Use absolute path for database
    flask_app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    # Initialize extensions
    db.init_app(flask_app)  # Initialize the SQLAlchemy instance with the Flask app
    print("✅ SQLAlchemy instance initialized with Flask app")  # Debug statement
    print("✅ Flask app context active:", flask_app.app_context().push())  # Debug app context

    login_manager = LoginManager()
    login_manager.login_view = 'auth.login'
    login_manager.init_app(flask_app)

    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(int(user_id))

    # Register blueprints
    from app.routes import auth
    flask_app.register_blueprint(auth)

    return flask_app

# Expose flask_app as app for external imports
app = create_app()