from apscheduler.schedulers.background import BackgroundScheduler
from datetime import date, timedelta
from flask import current_app
from .models import User, Application

def send_daily_reminders():
    with current_app.app_context():
        from .email import send_reminder_email  # lazy import
        tomorrow = date.today() + timedelta(days=1)
        users = User.query.all()

        for user in users:
            apps = Application.query.filter_by(user_id=user.id).filter(Application.application_date == tomorrow).all()

            if apps:
                body = f"Hi {user.username},\n\nYou have the following interviews tomorrow:\n"
                for app_item in apps:
                    body += f"- {app_item.job_title} at {app_item.company_name} on {app_item.application_date}\n"
                body += "\nGood luck!\n\n- Job Application Tracker"
                send_reminder_email(user.email, "Interview Reminder", body)

def start_scheduler(app):
    scheduler = BackgroundScheduler()
    scheduler.add_job(func=send_daily_reminders, trigger="interval", hours=24)
    scheduler.start()
