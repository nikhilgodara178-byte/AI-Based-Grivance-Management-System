from shared.utils.db_utils import db
from shared.models.grievance_model import Grievance
import datetime
from sqlalchemy import func, extract

class GrievanceService:
    @staticmethod
    def add_grievance(u_id,c_id,desc,title,audio,language):
        try:
            new_grievance = Grievance(u_id=u_id,c_id=c_id,audio=audio,desc=desc,status='Pending',time_stamp=datetime.datetime.now(),title=title,language=language,updated_at=datetime.datetime.now())
            db.session.add(new_grievance)
            db.session.commit()
            return True, new_grievance
        except Exception as error:
            db.session.rollback()
            return False, str(error)

    @staticmethod
    def get_all_grievance(user_id):
        try:
            grievances = Grievance.query.filter_by(u_id=user_id)
            return True, grievances
        except Exception as error:
            return False, str(error)
        
    @staticmethod
    def get_audio(g_id):
        try:
            audio_blob = Grievance.query.filter_by(g_id=g_id).first().audio
            if not audio_blob:
                return None,"audio not fount"
            return True,audio_blob
        except Exception as err:
            return False, str(err)
    