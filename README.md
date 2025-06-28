# 🥗 SilverWing — Dish Management System

A full-stack dish management app with a **Flask REST API backend** and a **Streamlit dashboard frontend**.

---

## 📁 Project Structure

````
├── main.py # Flask app entry point
├── requirements.txt
├── README.md
├── src/ # Backend source
│ ├── Dishes/ # Dish-related models, routes, utils
│ ├── app_info/ # Flask extensions
│ ├── common/ # Shared models/utilities
│ ├── config/ # App config and routing
│ ├── sql_config/ # DB init & session management
│ └── app.db # SQLite database
└── frontend/ # Streamlit frontend
├── app.py # Main entry point for frontend
├── api.py # Handles requests to backend
├── constants.py # API base URL config
└── pages/ # Multipage setup
├── home.py # Shows list of dishes
└── dish_details.py # Shows dish details
````

---

## ⚙️ Environment Setup

### 1. Clone the repository

```bash
git clone https://github.com/theprateekgoyal2/SilverWing.git
cd SilverWing
```
### 2. Set up virtual environment

```bash
python3.9 -m venv venv
source venv/bin/activate   # On Windows: venv\Scripts\activate
```

### 3. Install requirements
```bash
pip install -r requirements.txt
```

### 🛠️ Running the Project
Start the Flask Backend, From the root folder:

```bash
python main.py
```
Backend will run at http://localhost:5000

### 🛠️ Start the Streamlit Frontend
From the frontend/ folder:

```bash
streamlit run app.py
```
Frontend will open at http://localhost:8501

You’ll see a dashboard listing dishes. Click on a dish name to view details, and toggle publish status.

| Method | Endpoint                  | Description                |
| ------ | ------------------------- | -------------------------- |
| GET    | `/api/nosh/v1/dishes`     | Get all dishes             |
| GET    | `/api/nosh/v1/dishes?dish_id=ID` | Get dish by ID             |
| POST   | `/api/nosh/v1/dishes`     | Add new dishes             |
| POST   | `/api/nosh/v1/dishes/toggle` | Toggle dish publish status |


### 🛠️ Tech Stack
From the frontend/ folder:

```bash
Backend: Flask, SQLAlchemy, SQLite
Frontend: Streamlit
Language: Python 3.9+
```

### 🚀 Future Enhancements
From the frontend/ folder:

```bash
Add socket support for real-time updates
Enable dish editing form
Add user authentication (admin access)
```

### ‍💻 Author
Made with ❤️ by Prateek Goyal


### Postman collection setup instructions

Import `SilverWing.postman_collection.json` in your postman, for the value of `domain` use: `http://localhost:5000`