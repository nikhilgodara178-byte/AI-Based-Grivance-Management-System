import sys, os
sys.path.append(os.getcwd())

from flask import Flask
from grievance_app.routes.grievance_routes import grievance_bp
from shared.utils.db_utils import db
from config.config import connection_string
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

app.config['SQLALCHEMY_DATABASE_URI'] = connection_string
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True

db.init_app(app)

app.register_blueprint(grievance_bp)

if __name__ == '__main__':
    app.run(debug=True, port=5001)