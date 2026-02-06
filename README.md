# chemical-equipment-visualizer

```markdown
# Chemical Equipment Parameter Visualizer (Hybrid Web + Desktop App)

## Project Overview
This project is a hybrid application that runs both as a **web app** and a desktop app, allowing users to upload CSV files containing chemical equipment data and visualize parameters like flowrate, pressure, and temperature. The backend is powered by Django REST API, and both frontends consume the same API for consistency.

---

## Features
- Upload CSV files containing equipment data.
- View summary statistics: total equipment, average flowrate, pressure, and temperature.
- Visualize equipment type distribution using charts:
  - **Web:** React + Chart.js
  - **Desktop:** PyQt5 + Matplotlib
- Maintain last 5 uploaded datasets.
- Optional: Generate PDF reports.
- Basic authentication for API access.

---

## Tech Stack
| Layer         | Technology                       | Purpose                                 |
|---------------|---------------------------------|-----------------------------------------|
| Frontend (Web)| React.js + Chart.js              | Display table + charts                  |
| Frontend (Desktop) | PyQt5 + Matplotlib           | Desktop visualization                   |
| Backend       | Python Django + Django REST Framework | API and data processing            |
| Database      | SQLite                           | Store last 5 uploaded datasets          |
| Data Handling | Pandas                           | CSV parsing & analytics                 |
| Version Control | Git + GitHub                   | Collaboration & submission              |

-----

## Setup Instructions

### Backend
1. Navigate to backend folder:
 ```bash
 cd backend
````

2. Create and activate virtual environment:

   ```bash
   python3 -m venv venv
   source venv/bin/activate  # Mac/Linux
   venv\Scripts\activate     # Windows
   ```
3. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```
4. Run migrations:

   ```bash
   python manage.py migrate
   ```
5. Start the server:

   ```bash
   python manage.py runserver
   ```
6. Optional: Create superuser for admin access:

   ```bash
   python manage.py createsuperuser
   ```

### Web Frontend

1. Navigate to frontend folder:

   ```bash
   cd web-frontend
   ```
2. Install dependencies:

   ```bash
   npm install
   ```
3. Start React app:

   ```bash
   npm start
   ```
4. Open browser at `http://localhost:3000` to access the web frontend.

### Desktop Frontend

1. Navigate to desktop frontend folder:

   ```bash
   cd desktop-frontend
   ```
2. Install Python dependencies:

   ```bash
   pip install -r requirements.txt
   ```

   Required packages: `PyQt5`, `requests`, `matplotlib`, `pandas`
3. Run app:

   
   python app.py
   

---

## Usage

1. Upload CSV file via Web or Desktop interface.
2. View summary statistics and charts.
3. Access last 5 datasets from history (if implemented).

