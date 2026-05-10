from flask import jsonify

class UserView:
    @staticmethod
    def renderUser(user):
        return jsonify({
            'u_id': user.u_id,
            'student_id': user.student_id,
            'full_name': user.full_name,
            'email': user.email,
            'phone': user.phone,
            'department': user.department,
            'year': user.year,
            "isAdmin": False
        })
    
    @staticmethod
    def render_error(error):
        return jsonify({'message':error})
    
    @staticmethod
    def render_stat_card(this_month_counts,last_month_counts):
        this_month_data = {status: count for status, count in this_month_counts}
        last_month_data = {status: count for status, count in last_month_counts}

        this_total = sum(this_month_data.values())
        last_total = sum(last_month_data.values())

        result = [
            {
                'title': 'Total Complaints',
                'value': this_total,
                'trend': this_total - last_total
            },
            {
                'title': 'Resolved',
                'value': this_month_data.get('Resolved', 0),
                'trend': this_month_data.get('Resolved', 0) - last_month_data.get('Resolved', 0)
            },
            {
                'title': 'Pending',
                'value': this_month_data.get('Pending', 0),
                'trend': this_month_data.get('Pending', 0) - last_month_data.get('Pending', 0)
            }
        ]
        return jsonify(result)
    
    @staticmethod
    def render_kpi_report(resolution_rate,avg_response_time_seconds):
        result = [
            {
                'title': 'Complaints Resolution Rate (%)',
                'value': resolution_rate,
            },
            {
                'title': 'Average Response Time (in seconds)',
                'value': avg_response_time_seconds,
            }
        ]
        return jsonify(result)
