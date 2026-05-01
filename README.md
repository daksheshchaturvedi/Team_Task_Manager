Team Task Manager
A full-stack web application that allows users to create and join projects, assign tasks, and track progress efficiently within a team.
Features
User Authentication (Register/Login/Logout)
Create & Join Projects
Role-based Access (Admin / Member)
Task Assignment & Tracking
Project Progress Monitoring
Secure Data Handling
Tech Stack
Frontend:
HTML
CSS
JavaScript
Backend:
Python
Django Framework
Team_Task_Manager/
│── manage.py
│── Team_Task_Manager/
│   │── settings.py
│   │── urls.py
│   │── asgi.py
│   │── wsgi.py
│
│── app_name/
│   │── models.py
│   │── views.py
│   │── urls.py
│   │── templates/
│   │── static/
│
│── static/
│── templates/
│── db.sqlite3

Installation & Setup
Clone the Repository

git clone https://github.com/your-username/team-task-manager.git
cd team-task-manager
Create Virtual Environment
python -m venv venv
Activate it:
Mac/Linux:
source venv/bin/activate
Windows:
venv\Scripts\activate
Install Dependencies

pip install -r requirements.txt
Apply Migrations

python manage.py makemigrations
python manage.py migrate
Run Server

python manage.py runserver
Visit:
http://127.0.0.1:8000/
Default Functional Flow
User registers/logs in
Creates a project or joins existing one
Assigns tasks to members

Tracks task progress
Monitors overall project status
Screens (Optional)
Login Page
Dashboard
Project Page
Task Board
(Add screenshots here later for better presentation)
Deployment
You can deploy using:
Render
AWS
Heroku
Make sure to:
Set DEBUG = False
Configure ALLOWED_HOSTS
Collect static files:
python manage.py collectstatic
