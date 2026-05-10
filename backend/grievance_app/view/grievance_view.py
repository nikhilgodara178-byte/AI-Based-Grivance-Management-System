from flask import jsonify ,send_file, make_response
from io import BytesIO
from urllib.parse import urlparse

c_id_to_comittee_name = {
    1 : "examination",
    2 : "infrastructure", 
    3 : "general facility",
    4 : "research facility",
    5 : "journals/literature",
    6 : "fellowship"
}

class GrievanceView:
    @staticmethod
    def render_grievance(grievance):
        return {
            "id": grievance.g_id,
            "title": grievance.title,
            "desc": grievance.desc,
            "language": grievance.language,
            "u_id": grievance.u_id,
            "c_id": c_id_to_comittee_name[grievance.c_id],
            "status": grievance.status,
            "time_stamp": grievance.time_stamp,
        }

    @staticmethod
    def render_grievances(grievances):
        return [GrievanceView.render_grievance(grievance) for grievance in grievances]

    @staticmethod
    def render_text(text):
        return jsonify(text)
    
    @staticmethod
    def render_audio(blob_data):
        try:
            audio_stream = BytesIO(blob_data)
            response = make_response(send_file(audio_stream, mimetype='audio/mpeg'))
            response.headers['Content-Disposition'] = 'inline; filename=audio.mp3'
            return response
        except Exception as e:
            print(f"Error processing audio data: {e}")
            return None
        
