# Beyond Stars

Beyond Stars is a full-stack e-commerce application developed with Flask as part of a university project. The platform specializes in selling astronomy-related products, such as telescopes, to help enthusiasts explore the wonders of the cosmos.

## Technologies

Beyond Stars utilizes the following technologies and libraries:

- Python: ^3.12
- Flask: ^3.1.0
- Flask-SQLAlchemy: ^3.1.1 (ORM for database operations)
- Flask-Marshmallow: ^1.2.1 (Data serialization and validation)
- Flask-Migrate: ^4.0.7 (Database migrations)
- Flask-Bcrypt: ^1.0.1 (Password hashing)
- Flask-WTF: ^1.2.2 (Form handling)
- Flask-Login: ^0.6.3 (User authentication)
- Email-Validator: ^2.2.0 (Email validation)
- Marshmallow-SQLAlchemy: ^1.1.0 (Schema serialization for SQLAlchemy models)

## Database

- SQLite: Lightweight relational database for simplicity and ease of deployment.

## How to Install

Follow these steps to set up the project locally:

1. Clone the Repository

```sh
git clone https://github.com/Isaias-tech/beyond_stars.git
cd beyond_stars
```

2. Create a Virtual Environment

```sh
# Create a Python virtual environment
python -m venv venv

# Activate the virtual environment
# On Windows:
venv\Scripts\activate

# On macOS/Linux:
source venv/bin/activate
```

3. Install Dependencies

Beyond Stars uses Poetry for dependency management. Install Poetry if you haven’t already:

```sh
pip install poetry
```

Then, install the project dependencies:

```sh
poetry install
```

4. Initialize the Database

Run the following commands to set up the SQLite database:

```sh
flask db init
flask db migrate -m "Initial migration."
flask db upgrade
```

5. Run the Application

Start the Flask development server:

```sh
python app.py
```

The application will be accessible at http://127.0.0.1:8000.