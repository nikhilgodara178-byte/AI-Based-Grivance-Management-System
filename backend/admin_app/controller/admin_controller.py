from admin_app.services.admin_service import AdminService
from shared.models.admin_model import Admin
from admin_app.view.admin_view import AdminView
from datetime import datetime
from user_app.view.user_view import UserView

class AdminController:
    @staticmethod
    def signup(data):
        if Admin.query.filter_by(admin_id=data['admin_id']).first() or Admin.query.filter_by(email=data['email']).first():
            return AdminView.render_error("Admin ID or Email already exists"), 400
        res, user = AdminService.signup(data)
        if res:
            return AdminView.renderAdmin(user), 201
        else:
            return AdminView.render_error(user), 500

    @staticmethod
    def login(data):
        res, admin = AdminService.login(data)
        if res:
            return AdminView.renderAdmin(admin), 200
        else:
            return AdminView.render_error(admin), 401
        
    @staticmethod
    def update(data):
        full_name = data['full_name']
        email = data['email']
        phone = data['phone']
        u_id = data['u_id']
        res,user = AdminService.update(full_name,email,phone,u_id)
        if res:
            return AdminView.renderAdmin(user),200
        else:
            return AdminView.render_error(user),500
    
    @staticmethod
    def get_grievance_by_category(status,time_range):
        res, data = AdminService.get_grievance_by_category(status,time_range)
        if res:
            return AdminView.render_category_wise_grievance(data),200
        else:
            return AdminView.render_error(data),500

    @staticmethod
    def get_all_grievance():
        res,data = AdminService.get_all_grievance()
        if res:
            return AdminView.render_grievances(data)
        else:
            return AdminView.render_error(data)
        
    @staticmethod
    def get_stat_card_data():
        now = datetime.utcnow()
        this_month = now.month
        this_year = now.year

        if this_month == 1:
            last_month = 12
            last_month_year = this_year - 1
        else:
            last_month = this_month - 1
            last_month_year = this_year

        res,this_month_counts,last_month_counts = AdminService.get_state_card(this_month,this_year,last_month,last_month_year)
        if res:
            return UserView.render_stat_card(this_month_counts,last_month_counts),200
        else:
            return AdminView.render_error(this_month_counts),500
        
    @staticmethod
    def get_line_graph_data(time_range):
        res,data = AdminService.get_line_graph_data(time_range)
        if res:
            return AdminView.render_line_graph_data(time_range,data),200
        else:
            return AdminView.render_error(data),500
