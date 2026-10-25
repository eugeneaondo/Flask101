# Flask101

A structured Flask starter built on the application factory pattern and blueprints, with authentication, a database layer and a dashboard already wired in. It is a clean base for spinning up new Flask projects without rebuilding the same foundations each time.

![Python](https://img.shields.io/badge/Python-0d1117?style=flat-square&logo=python&logoColor=3776AB)
![Flask](https://img.shields.io/badge/Flask-2.3-0d1117?style=flat-square&logo=flask&logoColor=FFFFFF)
![SQLAlchemy](https://img.shields.io/badge/SQLAlchemy-0d1117?style=flat-square&logo=sqlalchemy&logoColor=D71F00)

---

## What's included

- **Application factory** (`create_app`) with configurable settings classes
- **Blueprints** separating `main`, `auth`, `posts` and `questions` into self-contained modules
- **Authentication** with registration, login and logout using Flask-Login and Bcrypt password hashing
- **Database layer** through Flask-SQLAlchemy, using SQLite by default and PostgreSQL through one environment variable
- **Templates** with a shared base layout, a dashboard, and pages for each module

## Project structure

```
Flask101/
├── config.py                # Settings (secret key, database URI)
├── requirements.txt
└── app/
    ├── __init__.py          # Application factory, blueprint registration
    ├── extensions.py        # db, bcrypt, login_manager
    ├── models/              # User, Post, Question
    ├── auth/                # /register, /login, /logout
    ├── main/                # /, /dashboard
    ├── posts/               # /posts, /categories
    ├── questions/           # /questions
    ├── templates/
    └── static/
```

## Getting started

```bash
git clone https://github.com/eugeneaondo/Flask101.git
cd Flask101

python -m venv .venv
source .venv/bin/activate        # Windows: .venv\Scripts\activate
pip install -r requirements.txt

flask --app "app:create_app" run
```

The app runs at `http://127.0.0.1:5000`.

### Configuration

Settings are read from environment variables, with development defaults:

| Variable | Purpose | Default |
|---|---|---|
| `SECRET_KEY` | Session signing key | Development placeholder (set your own in production) |
| `DATABASE_URI` | SQLAlchemy connection string | `sqlite:///app.db` |

To use PostgreSQL:

```bash
export DATABASE_URI="postgresql://user:password@localhost:5432/flask101"
```

## Adding a new module

1. Create a package under `app/` with an `__init__.py` defining a `Blueprint`.
2. Add routes in `routes.py` and templates under `app/templates/<module>/`.
3. Register the blueprint in `create_app()`.
