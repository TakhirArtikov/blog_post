# FastAPI Blog API

This project is a FastAPI based API for managing a simple blog.

## Installation

### Clone the Repository

```bash
git clone https://github.com/TakhirArtikov/blog_post
cd blog_post
```

### Create Virtual Environment
```bash
# On Unix/Linux
python3 -m venv venv

# On Windows
python -m venv venv
```
### Activate the Virtual Environment
```bash
# On Unix/Linux
source venv/bin/activate

# On Windows
venv\Scripts\activate
```
### Install Requirements
```bash
pip install -r requirements.txt
```
## Database Setup
This project uses SQLAlchemy as the ORM and Alembic for database migrations.
### Apply Migrations with Alembic
Make sure you have a database created and configured in your alembic.ini file.
```bash
alembic upgrade head
```
## Running the FastAPI Server
Once the database migrations are applied, you can run the FastAPI server.
```bash
uvicorn app.main:app --reload
```
The API will be served at http://127.0.0.1:8000.

### API Documentation
You can access the API documentation and interact with the endpoints through Swagger UI.
Local: http://127.0.0.1:8000/docs
