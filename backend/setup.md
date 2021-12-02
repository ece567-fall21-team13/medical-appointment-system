# Steps to create the Flask app
*OS: Windows 10*
1. Navigate to the backend directory in your shell
2. Create a virtual environment with: `py -m venv venv`
3. Activate the virtual environment: `venv\Scripts\activate`
4. To deactivate, simply run: `deactivate`
4. Upgrade pip and others: `py -m pip install --upgrade pip setuptools wheel`
5. Install flask: `pip install Flask`
6. Set the flask app variable: `set FLASK_APP=app`
6. Set to development: `set FLASK_ENV=development`
7. Start flask: `flask run`
8. `pip install SQLAlchemy`
8. `pip install -U Flask-SQLAlchemy`
9. `pip install psycopg2-binary`

# Database creation notes
1. Create a server, then a database, and then a schema called `mas`
2. From there, you can run the SQL commands provided in db.sql to create the various tables
3. For uuid generation, you need 2 lines of code to execute: `CREATE EXTENSION IF NOT EXISTS "uuid-ossp";` and `uuid_generate_v4()`