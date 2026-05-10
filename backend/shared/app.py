from flask import Flask
from shared.utils.db_utils import db
from shared.utils.db_utils import migrate
from config.config import connection_string


app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = connection_string
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False


db.init_app(app)
migrate.init_app(app, db)

from shared.models import user_model
from shared.models import grievance_model
from shared.models import commitee_model
from shared.models import admin_model