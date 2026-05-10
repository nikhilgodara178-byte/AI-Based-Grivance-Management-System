from shared.models.user_model import User
from shared.utils.db_utils import db
from shared.models.grievance_model import Grievance
from werkzeug.security import generate_password_hash,check_password_hash
from sqlalchemy import func, extract ,text

class UserService:
    @staticmethod
    def signup(data):
        try:
            hashed_password = generate_password_hash(data['password'], method='pbkdf2:sha256', salt_length=8)
            new_user = User(
                full_name=data['full_name'],
                student_id=data['student_id'],
                email=data['email'],
                phone=data['phone'],
                password=hashed_password,
                department=data['department'],
                year=data['year']
            )
            db.session.add(new_user)
            db.session.commit()
            return True, new_user
        except Exception as error: 
            db.session.rollback()
            return False, str(error)
        
    @staticmethod
    def login(data):
        try:
            user = User.query.filter_by(student_id=data['student_id']).first()
            if user and check_password_hash(user.password, data['password']):
                return True, user
            else:
                return False, "Invalid student ID or password"
        except Exception as error:
            db.session.rollback()
            return False, str(error)

    @staticmethod
    def update(full_name, email, phone, u_id):
        try:
            user = User.query.filter_by(u_id=u_id).first()
            print(user)
            if user:
                user.full_name = full_name
                user.email = email
                user.phone = phone
                db.session.commit()
                return True, user
            return False, "User not Found"
        except Exception as error:
            return False, str(error)
    
    @staticmethod
    def get_state_card(u_id,this_month,this_year,last_month,last_month_year):
        try:
            this_month_counts = db.session.query(Grievance.status, func.count(Grievance.g_id)).filter(
                Grievance.u_id == u_id,
                extract('month', Grievance.time_stamp) == this_month,
                extract('year', Grievance.time_stamp) == this_year
            ).group_by(Grievance.status).all()

            last_month_counts = db.session.query(
            Grievance.status, func.count(Grievance.g_id)).filter(
                Grievance.u_id == u_id,
                extract('month', Grievance.time_stamp) == last_month,
                extract('year', Grievance.time_stamp) == last_month_year
            ).group_by(Grievance.status).all()
            return True,this_month_counts,last_month_counts
        except Exception as err:
            return False, str(err),None
        
    @staticmethod
    def grievance_kpi_report(u_id):
        try:
            total = db.session.query(func.count(Grievance.g_id)).filter(Grievance.u_id==u_id).scalar()

            resolved = db.session.query(func.count(Grievance.g_id)).filter(
                Grievance.status == 'Resolved',Grievance.u_id==u_id
            ).scalar()

            resolution_rate = (resolved / total) * 100 if total else 0
    
            avg_response_time_seconds = db.session.query(
                func.avg(
                    func.timestampdiff(
                        text("SECOND"),
                        Grievance.time_stamp,
                        Grievance.updated_at
                    )
            ).label('avg_response_time_seconds')).filter(
                Grievance.status == "Resolved"
            ).scalar()

            avg_response_time_seconds = avg_response_time_seconds or 0
            print(resolution_rate,avg_response_time_seconds)
            return True, resolution_rate,avg_response_time_seconds
        except Exception as err:
            print(err)
            return False,str(err),None

