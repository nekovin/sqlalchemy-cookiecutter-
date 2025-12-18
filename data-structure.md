# SQLAlchemy Cookiecutter Data Structure

## Template Variables (cookiecutter.json)

| Variable | Type | Default | Description |
|----------|------|---------|-------------|
| project_name | string | "My SQLAlchemy Project" | Human-readable project name |
| project_slug | string | (derived) | Lowercase, underscored project name |
| project_description | string | "A SQLAlchemy project" | Project description |
| author_name | string | "Your Name" | Author name |
| author_email | string | "your.email@example.com" | Author email |
| python_version | string | "3.11" | Minimum Python version |
| database_url | string | "sqlite:///./{{project_slug}}.db" | Default database URL |
| use_alembic | choice | ["yes", "no"] | Include Alembic migrations |
| include_example_model | choice | ["yes", "no"] | Include example User model |

## Generated Structure

```
{{project_slug}}/
├── pyproject.toml
├── README.md
├── .gitignore
├── alembic.ini              # if use_alembic=yes
├── alembic/                  # if use_alembic=yes
│   ├── env.py
│   ├── script.py.mako
│   └── versions/
├── src/
│   └── {{project_slug}}/
│       ├── __init__.py
│       ├── config.py
│       ├── db/
│       │   ├── __init__.py
│       │   └── session.py
│       └── models/
│           ├── __init__.py
│           ├── base.py
│           └── user.py      # if include_example_model=yes
└── tests/
    ├── __init__.py
    ├── conftest.py
    └── test_models.py
```

## Model Structure

### Base (models/base.py)
- `Base`: DeclarativeBase for all models
- `TimestampMixin`: Adds created_at/updated_at columns

### User (models/user.py) - optional
- id: int (primary key)
- email: str (unique, indexed)
- name: str
- is_active: bool
- created_at: datetime
- updated_at: datetime

## Database Session (db/session.py)
- `get_engine()`: Returns singleton engine
- `get_session()`: Generator yielding sessions
- `create_all_tables()`: Creates all tables via metadata
