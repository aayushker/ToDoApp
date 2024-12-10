# To-Do List Application

A simple to-do list application built with Django. This project allows users to add tasks, view a list of tasks, and manage their to-do items using a clean interface and basic HTML/CSS. The backend is implemented using Django REST Framework.

---

## Features

- Add new tasks with a title and description.
- View all tasks in a list.
- Backend API endpoints for creating and retrieving tasks.

---

## Installation and Setup

Follow these steps to set up and run the application on your local machine:

### Prerequisites

Ensure you have the following installed:

- Python 3.8 or later
- pip (Python package manager)
- Git
- Virtual Environment (optional but recommended)

### 1. Clone the Repository

```bash
git clone https://github.com/aayushker/ToDoApp
cd ToDoApp
```

### 2. Create a Virtual Environment (Optional)

```bash
python -m venv venv
source venv/bin/activate # For Linux/macOS
venv\Scripts\activate    # For Windows
```

### 3. Install Dependencies

Install the required Python packages using pip:

```bash
pip install -r requirements.txt
```

### 4. Apply Migrations

Run the following commands to set up the database:

```bash
python manage.py makemigrations
python manage.py migrate
```

### 5. Run the Development Server

Start the Django development server:

```bash
python manage.py runserver
```

The application will be available at: [http://127.0.0.1:8000](http://127.0.0.1:8000)