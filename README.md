# SQLAlchemy Cookiecutter

Cookiecutter template for SQLAlchemy 2.0+ projects.

## Usage

```bash
pip install cookiecutter
cookiecutter gh:username/sqlalchemy-cookiecutter
# or
cookiecutter /path/to/sqlalchemy-cookiecutter
```

## Features

- SQLAlchemy 2.0+ with modern mapped_column syntax
- Optional Alembic migrations
- Optional example User model with timestamps
- src layout
- pytest configuration
- Database session management

## Options

| Option | Description |
|--------|-------------|
| use_alembic | Include Alembic migration setup |
| include_example_model | Include example User model |
