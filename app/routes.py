from flask import Blueprint, render_template, redirect, url_for, flash, request, jsonify, send_file
from flask_login import login_required, current_user
from .models import Application
from .forms import ApplicationForm
from . import db
from datetime import datetime, date, timedelta
import pandas as pd
from io import BytesIO, StringIO
from .email import send_reminder_email

main = Blueprint('main', __name__)

@main.route('/')
@login_required
def dashboard():
    search_query = request.args.get('search')
    status_filter = request.args.get('status')
    
    applications = Application.query.filter_by(user_id=current_user.id)

    if search_query:
        applications = applications.filter(Application.company_name.ilike(f'%{search_query}%') | 
                                           Application.job_title.ilike(f'%{search_query}%'))

    if status_filter and status_filter != 'All':
        applications = applications.filter_by(status=status_filter)

    applications = applications.order_by(Application.application_date.desc()).all()
    return render_template('index.html', applications=applications)

@main.route('/add', methods=['GET', 'POST'])
@login_required
def add_application():
    form = ApplicationForm()
    if form.validate_on_submit():
        new_app = Application(
            company_name=form.company_name.data,
            job_title=form.job_title.data,
            application_date=form.application_date.data or datetime.utcnow(),
            status=form.status.data,
            notes=form.notes.data,
            application_link=form.application_link.data,
            user_id=current_user.id
        )
        db.session.add(new_app)
        db.session.commit()
        flash('Application added!', 'success')
        return redirect(url_for('main.dashboard'))
    return render_template('application_form.html', form=form)

@main.route('/edit/<int:app_id>', methods=['GET', 'POST'])
@login_required
def edit_application(app_id):
    application = Application.query.get_or_404(app_id)
    if application.owner != current_user:
        flash('Unauthorized access.', 'danger')
        return redirect(url_for('main.dashboard'))

    form = ApplicationForm(obj=application)
    if form.validate_on_submit():
        application.company_name = form.company_name.data
        application.job_title = form.job_title.data
        application.application_date = form.application_date.data
        application.status = form.status.data
        application.notes = form.notes.data
        application.application_link = form.application_link.data
        db.session.commit()
        flash('Application updated.', 'success')
        return redirect(url_for('main.dashboard'))
    return render_template('application_form.html', form=form)

@main.route('/delete/<int:app_id>')
@login_required
def delete_application(app_id):
    application = Application.query.get_or_404(app_id)
    if application.owner != current_user:
        flash('Unauthorized access.', 'danger')
        return redirect(url_for('main.dashboard'))

    db.session.delete(application)
    db.session.commit()
    flash('Application deleted.', 'info')
    return redirect(url_for('main.dashboard'))

@main.route('/export/<filetype>')
@login_required
def export_data(filetype):
    applications = Application.query.filter_by(user_id=current_user.id).all()
    data = [{
        'Company': app.company_name,
        'Job Title': app.job_title,
        'Application Date': app.application_date.strftime('%Y-%m-%d'),
        'Status': app.status,
        'Notes': app.notes,
        'Application Link': app.application_link
    } for app in applications]

    df = pd.DataFrame(data)

    if filetype == 'csv':
        output = StringIO()
        df.to_csv(output, index=False)
        output.seek(0)
        return send_file(BytesIO(output.getvalue().encode()), 
                         mimetype='text/csv', 
                         as_attachment=True, 
                         download_name='applications.csv')

    elif filetype == 'excel':
        output = BytesIO()
        with pd.ExcelWriter(output, engine='xlsxwriter') as writer:
            df.to_excel(writer, index=False, sheet_name='Applications')
        output.seek(0)
        return send_file(output, 
                         mimetype='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet', 
                         as_attachment=True, 
                         download_name='applications.xlsx')
    else:
        flash('Invalid file type!', 'danger')
        return redirect(url_for('main.dashboard'))

@main.route('/graph-data')
@login_required
def graph_data():
    apps = Application.query.filter_by(user_id=current_user.id).all()
    status_counts = {'Applied': 0, 'Interview': 0, 'Offer': 0, 'Rejected': 0}
    for app in apps:
        if app.status in status_counts:
            status_counts[app.status] += 1
    return jsonify(status_counts)

@main.route('/send_reminders')
@login_required
def send_reminders():
    tomorrow = date.today() + timedelta(days=1)
    apps = Application.query.filter_by(user_id=current_user.id).filter(Application.application_date == tomorrow).all()

    if not apps:
        flash('No interviews scheduled for tomorrow.', 'info')
        return redirect(url_for('main.dashboard'))

    for app in apps:
        subject = f"Reminder: Interview with {app.company_name} Tomorrow!"
        body = f"Hi {current_user.username},\n\nYou have an interview scheduled with {app.company_name} for the position of {app.job_title} tomorrow ({app.application_date}).\n\nGood Luck!\n\n- Job Application Tracker"
        send_reminder_email(current_user.email, subject, body)

    flash('Reminder emails sent successfully!', 'success')
    return redirect(url_for('main.dashboard'))
