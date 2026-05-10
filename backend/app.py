"""
Unified Flask application that combines user, grievance, and admin services
into a single app for deployment on Render (which only exposes one port).
"""
import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from flask import Flask
from flask_cors import CORS
from shared.utils.db_utils import db, migrate
from config.config import connection_string

from user_app.routes.user_routes import user_bp
from grievance_app.routes.grievance_routes import grievance_bp
from admin_app.routes.admin_routes import admin_bp

app = Flask(__name__)
CORS(app)

app.config['SQLALCHEMY_DATABASE_URI'] = connection_string
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)
migrate.init_app(app, db)

# Import models so they are registered with SQLAlchemy
from shared.models.user_model import User
from shared.models.admin_model import Admin
from shared.models.grievance_model import Grievance
from shared.models.commitee_model import Committee

# Register all blueprints with prefixes to avoid route conflicts
# user routes: /user/signup, /user/login, etc.
# grievance routes: /grievance/add_grievance, etc.
# admin routes: /admin/login, etc.
app.register_blueprint(user_bp, url_prefix='/user')
app.register_blueprint(grievance_bp, url_prefix='/grievance')
app.register_blueprint(admin_bp, url_prefix='/admin')

# Create tables if they don't exist
with app.app_context():
    db.create_all()

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
