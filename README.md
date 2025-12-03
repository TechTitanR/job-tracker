# 🎯 Job Application Tracker

A full-featured Flask web application that helps users efficiently track their job applications — with email reminders, status filtering, CSV/Excel export, auto-scheduled interview alerts, and more.  
**Deployed with PostgreSQL on Render.**

---

## 🚀 Live Demo

🔗 [https://your-render-link.onrender.com]((https://job-tracker-yog5.onrender.com) *(Render deployment)*

---

## 📝 Features

✔️ **User Registration & Login (Flask-Login)**  
✔️ **Add / Edit / Delete Job Applications**  
✔️ **Search + Filter by Application Status (Applied, Interview, Offer, Rejected)**  
✔️ **Email Reminders for Upcoming Interviews (Flask-Mail)**  
✔️ **Auto Daily Email Scheduler (APScheduler)**  
✔️ **CSV/Excel Export of Job Data**  
✔️ **Graphical Dashboard with Charts (Chart.js)**  
✔️ **PostgreSQL (Render Deployment Ready)**  
✔️ **Bootstrap 5 + Custom CSS Frontend**

---

## 🛠️ Tech Stack

| Technology     | Purpose                      |
|---------------|-----------------------------|
| **Flask**     | Backend Web Framework        |
| **Flask-SQLAlchemy** | ORM for Database (PostgreSQL) |
| **Flask-Login** | User Authentication       |
| **Flask-Mail** | Email Notification System  |
| **APScheduler** | Auto Daily Background Jobs |
| **Chart.js**  | Graphical Data Visualization |
| **PostgreSQL**| Production Database (Render) |
| **HTML5 + Bootstrap 5 + CSS3** | Frontend UI |

---

## 📦 Local Development Setup

### 1️⃣ **Clone the repo:**
```bash
git clone https://github.com/TechTitanR/job-tracker.git
cd job-tracker
```

### 2️⃣ **Create and activate virtual environment (Optional but Recommended):**
```bash
python -m venv venv
venv\Scripts\activate   # On Windows
# Or: source venv/bin/activate   # On Mac/Linux
```

### 3️⃣ **Install required Python packages:**
```bash
pip install -r requirements.txt
```

### 4️⃣ **Create .env file:**
```bash
SECRET_KEY=your-secret-key
DATABASE_URL=sqlite:///jobtracker.db   # For local dev
MAIL_SERVER=smtp.gmail.com
MAIL_PORT=587
MAIL_USE_TLS=True
MAIL_USERNAME=youremail@gmail.com
MAIL_PASSWORD=yourpassword
```
- ✔️ (Don’t push .env to GitHub — it’s in .gitignore)

### 5️⃣ **Setup Database (Locally):**
```bash
flask db init
flask db migrate -m "initial migration"
flask db upgrade
```

### 6️⃣ **Run Locally:**
```bash 
python run.py
```
- Visit: http://127.0.0.1:5000

---

## ☁️ Render Deployment (PostgreSQL)
- 1️⃣ Push the project to GitHub (Done ✅).

- 2️⃣ Create .env variables in Render Dashboard:
-- SECRET_KEY
-- DATABASE_URL (Render PostgreSQL URL)
-- MAIL_SERVER
-- MAIL_PORT
-- MAIL_USE_TLS
-- MAIL_USERNAME
-- MAIL_PASSWORD

- 3️⃣ Use Procfile:
```bash
web: gunicorn run:app
```

---

## 📊 Dashboard Example:

---

## 🔧 To Do (Future Features):
- Pagination for Application List
- Multi-user Admin Dashboard
- SMS/WhatsApp Reminders
- Job Market API Integration (like LinkedIn)

---

## 👨‍💻 Author
- Rishi Bakliwal
- GitHub: https://github.com/TechTitanR | LinkedIn: https://www.linkedin.com/in/rishi-bakliwal-1a5851244/

---

## 📄 License
- This project is licensed under the MIT License — see LICENSE file for details.

---

## 🤝 Contributing
- Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

---

## 🚨 Important
- ✔️ .env file is never pushed to GitHub (thanks to .gitignore).
- ✔️ PostgreSQL connection for production is managed via Render’s Dashboard.

