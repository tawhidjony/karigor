# Karigor CLI

Karigor is a Laravel Artisan inspired command line tool for Python projects. It helps you bootstrap a modular application structure, manage Alembic migrations, install database drivers, and generate basic model and controller files.

## Features

- `karigor init` — scaffold a new project with `main.py`, app folders, config files, and a migration base file.
- `karigor serve` — run the project using `main.py`.
- `karigor db:install` — install Alembic and optionally selected database drivers interactively.
- `karigor create:migration <name>` — generate a new SQLAlchemy migration file and register it inside `database/migrations/base.py`.
- `karigor migrate <message>` — run Alembic autogenerate and upgrade to the latest migration.
- `karigor create:model <path>` — create a new model class file from a simple template.
- `karigor create:controller <path>` — create a new controller class file from a simple template.

## Installation

Install from PyPI:

```bash
pip install karigor
```

Or install from source:

```bash
git clone https://github.com/<your-repo>/karigor.git
cd karigor
pip install .
```

## Requirements

- Python 3.10+
- `typer[all]`
- `rich`
- `questionary`
- `inflect`
- `sqlalchemy`

These dependencies are installed automatically with `karigor`.

## Usage

Run `karigor` after installation.

### Initialize a new project

```bash
karigor init
```

This command sets up a modular folder structure, installs core packages (`fastapi`, `uvicorn[standard]`, `pydantic-settings`, `sqlalchemy`), and generates:

- `main.py`
- `.env`, `.env.example`
- `config/env_setting.py`
- `config/meta_data.py`
- `database/migrations/base.py`
- package folders with `__init__.py`

### Serve the application

```bash
karigor serve
```

Runs `main.py` from the current directory. If `main.py` is missing, Karigor prints an error and asks you to run `karigor init` first.

### Install database support

```bash
karigor db:install
```

Installs `alembic` and optionally PostgreSQL or MySQL drivers. It initializes Alembic in an `alembic` directory and writes the `alembic/env.py` template.

### Create a migration

```bash
karigor create:migration users
```

Generates a new migration file under `database/migrations/` and checks for duplicate `__tablename__` values. The command singularizes and pluralizes the provided name to keep table naming consistent.

### Apply migrations

```bash
karigor migrate "add users table"
```

Runs:

- `alembic revision --autogenerate -m "<message>"`
- `alembic upgrade head`

If Alembic is not initialized, Karigor advises running `karigor db:install` first.

### Create model and controller files

```bash
karigor create:model app/models/User.py
karigor create:controller app/controllers/UserController.py
```

Creates a simple class template file for the requested path.

## Project Structure

After `karigor init`, a typical project structure includes:

```
app/
  controllers/
  models/
config/
  env_setting.py
  meta_data.py
database/
  migrations/
    base.py
main.py
.env
.env.example
alembic/  # after db:install
```

## Notes

- `karigor init` writes default templates into the new project structure.
- `karigor db:install` is interactive and lets you choose database driver packages to install.
- Migration file creation includes automatic registration in `database/migrations/base.py`.

## License

MIT
