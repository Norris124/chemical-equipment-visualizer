

```markdown
# Chemical Equipment Visualizer

A full-stack application to upload chemical plant equipment data (CSV) and visualize summary statistics and equipment distribution using interactive charts.

---

📌 Features

- Upload CSV file containing chemical equipment data
- Backend processes data and csv details
- Interactive bar chart visualization (React + Chart.js)
- Supports Web frontend and Desktop frontend (PyQt)
- REST API built with Django

---

🏗️ Tech Stack

### Backend
- Python
- Django
- Django REST Framework

Web Frontend
- React
- Axios
- Chart.js

### Desktop Frontend
- Python
- PyQt5
- Requests

---
▶️ How to Run the Project

1️⃣ Backend Setup

```bash
cd backend
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
```

Backend will run at:

```
http://127.0.0.1:8000
```

---

2️⃣ Web Frontend Setup

```bash
cd web-frontend
npm install
npm start
```

Web app runs at:

```
http://localhost:3000
```

---

3️⃣ Desktop Frontend Setup 

```bash
cd desktop-frontend
pip install -r requirements.txt
python app.py
```

---

