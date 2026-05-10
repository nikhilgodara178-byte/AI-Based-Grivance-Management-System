from flask import Blueprint,request
from grievance_app.controller.grievance_controller import GrievanceController
from sqlalchemy import func, extract

grievance_bp = Blueprint('grievance_bp',__name__)

@grievance_bp.route('/add_grievance', methods=['POST'])
def add_grievance():
    file = request.files
    data = request.form
    return GrievanceController.add_grievance(data,file)


@grievance_bp.route("/speechToText", methods=['POST'])
def speechToText():
    try:
        file = request.files['file']
        lan = request.form.get('language')
        return GrievanceController.convertToText(file,lan)
    except Exception as error:
        print(error)
        return error

@grievance_bp.route('/get_all_grievance/<int:user_id>',methods=['GET'])
def get_all_grievance(user_id):
    return GrievanceController.get_all_grievance(user_id)

@grievance_bp.route("/get_audio/<int:g_id>",methods=['GET'])
def get_audio(g_id):
    return GrievanceController.get_audio(g_id)


    