from flask import Blueprint,request
from admin_app.controller.admin_controller import AdminController

admin_bp = Blueprint("admin_bp",__name__)

@admin_bp.route('/signup', methods=['POST'])
def signup():
    data = request.json
    return AdminController.signup(data)

@admin_bp.route('/login', methods=['POST'])
def login():
    data = request.json
    return AdminController.login(data)

@admin_bp.route("/update",methods=['PUT'])
def udate():
    data = request.json
    return AdminController.update(data)

@admin_bp.route("/grievanceCategory/<status>/<time_range>")
def get_grievance_by_category(status,time_range):
    return AdminController.get_grievance_by_category(status,time_range)

@admin_bp.route("/get_all_grievance",methods=['GET'])
def get_all_grievance():
    return AdminController.get_all_grievance()

@admin_bp.route("/get_data_statcard",methods=['GET'])
def get_stat_card_data():
    return AdminController.get_stat_card_data()

@admin_bp.route("/get_line_graph_data/<time_range>",methods=['GET'])
def get_line_graph_data(time_range):
    return AdminController.get_line_graph_data(time_range)
