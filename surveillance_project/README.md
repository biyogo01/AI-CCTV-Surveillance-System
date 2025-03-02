# AI CCTV Surveillance System

This project is a Django-based AI-powered CCTV surveillance system.

## Features
- Real-time video surveillance
- Motion detection & alerts
- User authentication & role-based access
- Web-based control panel

## Requirements
- Python 3.x
- Django
- OpenCV (if using real-time video processing)

## Installation

### 1. Clone the Repository
```sh
git clone https://github.com/biyogo01/AI-CCTV-Surveillance-System.git
cd AI-CCTV-Surveillance-System/surveillance_project
```

### 2. Create a Virtual Environment
```sh
python -m venv venv
source venv/bin/activate  # On Windows use: venv\Scripts\activate
```

### 3. Install Dependencies
```sh
pip install -r requirements.txt
```

### 4. Run Migrations
```sh
python manage.py migrate
```

### 5. Create a Superuser (Admin Account)
```sh
python manage.py createsuperuser
```

### 6. Run the Development Server
```sh
python manage.py runserver
```

Access the web interface at: [http://127.0.0.1:8000](http://127.0.0.1:8000)

## Configuration
- Edit `core/settings.py` for database configuration, security settings, and installed apps.

## Contributing
Pull requests are welcome. For major changes, please open an issue first.

## License
This project is licensed under the MIT License.
