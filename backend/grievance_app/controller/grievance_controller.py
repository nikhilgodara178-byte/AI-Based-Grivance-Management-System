from grievance_app.service.grievance_service import GrievanceService
from grievance_app.view.grievance_view import GrievanceView
from ML_Models.MLmodel import MLmodelsClass
from user_app.view.user_view import UserView
from io import BytesIO
import datetime

commitee_name_to_c_id = {
    "examination" : 1, 
    "infrastructure": 2, 
    "general facility" : 3,
    "research facility" : 4,
    "journals/literature" : 5,
    "fellowship" : 6
}

language_to_code = {
    "hindi" : "hi-IN",
    "english" : "en-IN",
    "marathi": 'mr-IN',
    "gujarati": "gu-IN"
}

class GrievanceController:
    @staticmethod
    def add_grievance(data,file):
        u_id = data["u_id"]
        language = data['language']
        desc = data['description']
        comittee = data['comittee']

        if data["comittee"] not in commitee_name_to_c_id:
            comittee = MLmodelsClass.grievance_classification(desc,language)
        
        c_id = commitee_name_to_c_id[comittee]
        title = data['title']
        audio = file['blob'].read()

        res, grievance = GrievanceService.add_grievance(u_id,c_id,desc,title,audio,language)
        if res:
            return GrievanceView.render_grievance(grievance)
        else:
            return UserView.render_error(grievance)
        
    @staticmethod
    def convertToText(file,lan):
        try:
            buffer = BytesIO(file.read())
            res = MLmodelsClass.speechTotext(buffer,language_to_code[lan])
            if res['success']:
                return GrievanceView.render_text(res['text']),200
            else:
                print(res['error'])
                return UserView.render_error(res['error']),500
        except Exception as error:
            print(error)
            return error
    @staticmethod
    def get_all_grievance(user_id):
        res,grievances = GrievanceService.get_all_grievance(user_id)
        if res:
            return GrievanceView.render_grievances(grievances),200
        else:
            return UserView.render_error(grievances),500
    @staticmethod
    def get_audio(g_id):
        res,audio = GrievanceService.get_audio(g_id)
        if res:
            return GrievanceView.render_audio(audio),200
        if res is None:
            return UserView.render_error(audio),404
        else:
            return UserView.render_error(audio),500



        
