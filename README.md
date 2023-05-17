# CRUD APP

This is a simple Flask-based CRUD (Create, Read, Update, Delete) application with a web interface.

## Running the app using Docker

Make sure you have Docker installed.

- Clone the repository and navigate to the project directory

```bash
git clone https://github.com/pgardikis/CRUD_app.git
```

- Build the Docker image

```bash
docker build -t flask-crud-app .
```

- Run a Docker container
```bash
docker run -d -p 8080:5000 flask-crud-app
```

## Viewing the app

Go to `http://localhost:8080`
