from user_app.services.user_service import UserService
from shared.models.user_model import User
from user_app.view.user_view import UserView
from datetime import datetime


class UserController:
    @staticmethod
    def signup(data):
        if User.query.filter_by(student_id=data['student_id']).first() or User.query.filter_by(email=data['email']).first():
            return UserView.render_error("Student ID or Email already exists"), 400
        res, user = UserService.signup(data)
        if res:
            return UserView.renderUser(user), 201
        else:
            return UserView.render_error(user), 500

    @staticmethod
    def login(data):
        res, user = UserService.login(data)
        if res:
            return UserView.renderUser(user), 200                                
        else:
            return UserView.render_error(user), 401
        
    @staticmethod
    def update(data):
        full_name = data['full_name']
        email = data['email']
        phone = data['phone']
        u_id = data['u_id']

        res,user = UserService.update(full_name,email,phone,u_id)
        if res:
            return UserView.renderUser(user),200
        else:
            return UserView.render_error(user),500
        
    @staticmethod
    def get_state_card(u_id):
        now = datetime.utcnow()
        this_month = now.month
        this_year = now.year

        if this_month == 1:
            last_month = 12
            last_month_year = this_year - 1
        else:
            last_month = this_month - 1
            last_month_year = this_year
        res,this_month_counts,last_month_counts = UserService.get_state_card(u_id,this_month,this_year,last_month,last_month_year)
        if res:
            return UserView.render_stat_card(this_month_counts,last_month_counts),200
        else:
            return UserView.render_error(this_month_counts),500
    
    @staticmethod
    def grievance_kpi_report(u_id):
        res,resolution_rate,avg_response_time_seconds = UserService.grievance_kpi_report(u_id)
        if res:
            return UserView.render_kpi_report(resolution_rate,avg_response_time_seconds),200
        else: 
            return UserView.render_error(resolution_rate),500
