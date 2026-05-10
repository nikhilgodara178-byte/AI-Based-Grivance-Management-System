import os

python_dir = "python"
connection_string = os.environ.get(
    'DATABASE_URL',
    'mysql+pymysql://root:Suzain%401234@localhost/grievance_management_system_db'
)