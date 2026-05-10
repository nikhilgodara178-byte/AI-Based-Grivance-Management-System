from flask import Blueprint,request,jsonify
from user_app.controller.user_controller import UserController

user_bp = Blueprint('user_bp',__name__)

@user_bp.route('/signup', methods=['POST'])
def signup():
    data = request.json
    return UserController.signup(data)

@user_bp.route('/login', methods=['POST'])
def login():
    data = request.json
    return UserController.login(data)

@user_bp.route("/update",methods=['PUT'])
def udate():
    data = request.json
    return UserController.update(data)

@user_bp.route("/get_data_statcard/<int:u_id>",methods=['GET'])
def get_stat_card_data(u_id):
    return UserController.get_state_card(u_id)

@user_bp.route('/grievance/kpi_report/<int:u_id>', methods=['GET'])
def grievance_kpi_report(u_id):
    return UserController.grievance_kpi_report(u_id)

