# {{ cookiecutter.project_name }}

{{ cookiecutter.project_description }}

## Setup

```bash
pip install -e ".[dev]"
```

## Database

Set `DATABASE_URL` environment variable or use default SQLite.

{% if cookiecutter.use_alembic == 'yes' %}
### Migrations

```bash
# create migration
alembic revision --autogenerate -m "description"

# run migrations
alembic upgrade head
```
{% endif %}

## Usage

```python
from {{ cookiecutter.project_slug }}.db import get_session, create_all_tables
{% if cookiecutter.include_example_model == 'yes' %}
from {{ cookiecutter.project_slug }}.models import User
{% endif %}

# create tables (without alembic)
create_all_tables()

# use session
for session in get_session():
{% if cookiecutter.include_example_model == 'yes' %}
    user = User(email="test@example.com", name="Test")
    session.add(user)
    session.commit()
{% else %}
    # your code here
    pass
{% endif %}
```

## Tests

```bash
pytest
```
