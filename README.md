# 🚀 Karigor CLI

> Laravel Artisan Inspired CLI Tool for Python Developers

Karigor helps you bootstrap scalable Python applications, manage database migrations, generate code scaffolding, and streamline development workflows with a familiar Artisan-like experience.

---

## ⚡ Quick Commands

```bash
karigor init
karigor serve
karigor db:install
karigor create:migration users
karigor migrate "create users table"
karigor create:model app/models/User.py
karigor create:controller app/controllers/UserController.py
```

---

## 🎯 Available Commands

| Command                            | Description                          |
| ---------------------------------- | ------------------------------------ |
| `karigor init`                     | Initialize a new project             |
| `karigor serve`                    | Run the application                  |
| `karigor db:install`               | Install Alembic and database drivers |
| `karigor create:migration <name>`  | Create migration file                |
| `karigor migrate "<message>"`      | Generate and run migrations          |
| `karigor create:model <path>`      | Generate a model class               |
| `karigor create:controller <path>` | Generate a controller class          |

---

# 📦 Installation

Install from PyPI:

```bash
pip install karigor
```

Verify installation:

```bash
karigor --help
```

---

# 🚀 Getting Started

Create a new project:

```bash
karigor init
```

Start the application:

```bash
karigor serve
```

---

# 🏗️ Command Reference

## ⚡ karigor init

Initialize a new Karigor project.

```bash
karigor init
```

### What it creates

```text
app/
config/
database/

main.py
.env
.env.example
```

### Installed Packages

```text
fastapi
uvicorn[standard]
pydantic-settings
sqlalchemy
```

---

## ▶️ karigor serve

Run your application.

```bash
karigor serve
```

Equivalent:

```bash
python main.py
```

If `main.py` is missing, Karigor will suggest running:

```bash
karigor init
```

---

## 🗄️ karigor db:install

Install database support and Alembic.

```bash
karigor db:install
```

### Installs

```text
alembic
```

Optional Drivers:

### PostgreSQL

```text
psycopg2-binary
```

### MySQL

```text
pymysql
mysqlclient
```

### Generates

```text
alembic/
alembic/env.py
```

---

## 📝 karigor create:migration

Generate a migration file.

```bash
karigor create:migration users
```

### Features

* Automatic migration registration
* Duplicate table protection
* Smart singular/plural naming
* SQLAlchemy compatible

Generated in:

```text
database/migrations/
```

---

## 🔄 karigor migrate

Generate and execute migrations.

```bash
karigor migrate "create users table"
```

Internally runs:

```bash
alembic revision --autogenerate -m "create users table"
alembic upgrade head
```

---

## 🏗️ karigor create:model

Generate a model file.

```bash
karigor create:model app/models/User.py
```

Generated Template:

```python
class User:
    pass
```

---

## 🎮 karigor create:controller

Generate a controller file.

```bash
karigor create:controller app/controllers/UserController.py
```

Generated Template:

```python
class UserController:
    pass
```

---

# 📁 Project Structure

After running:

```bash
karigor init
```

Your project structure will look like:

```text
project/

├── app/
│   ├── controllers/
│   ├── models/
│   └── __init__.py
│
├── config/
│   ├── env_setting.py
│   ├── meta_data.py
│
├── database/
│   ├── migrations/
│   │   └── base.py
│
├── main.py
├── .env
├── .env.example
│
└── alembic/
```

---

# ⚡ Typical Workflow

### 1. Create Project

```bash
karigor init
```

### 2. Install Database Support

```bash
karigor db:install
```

### 3. Create Models

```bash
karigor create:model app/models/User.py
```

### 4. Generate Migration

```bash
karigor create:migration users
```

### 5. Run Migration

```bash
karigor migrate "create users table"
```

### 6. Start Application

```bash
karigor serve
```

---

# ❤️ Why Karigor?

Karigor brings Laravel Artisan-like productivity to Python projects.

### Benefits

✅ Fast Project Setup

✅ Migration Management

✅ Model Generator

✅ Controller Generator

✅ Interactive CLI

✅ FastAPI Ready

✅ SQLAlchemy Ready

✅ Clean Folder Structure

✅ Rich Terminal Output

---

# 🔧 Requirements

* Python 3.10+
* FastAPI
* SQLAlchemy
* Alembic

Most dependencies are installed automatically by Karigor.

---

# 🛣️ Roadmap

Upcoming features:

* Repository Generator
* Service Generator
* Route Generator
* CRUD Generator
* Authentication Boilerplate
* Docker Support
* Clean Architecture Template
* Async SQLAlchemy Support
* PostgreSQL Extensions

---

# 🤝 Contributing

Contributions are welcome.

Clone the repository:

```bash
git clone https://github.com/yourusername/karigor.git

cd karigor

pip install -e .
```

Run tests:

```bash
pytest
```

Please open an issue before submitting major changes.

---

# 📄 License

MIT License

---

## Made with ❤️ for Python Developers

Karigor — Build Faster, Code Smarter.
