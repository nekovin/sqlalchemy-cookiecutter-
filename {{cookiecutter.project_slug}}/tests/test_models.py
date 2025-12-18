{% if cookiecutter.include_example_model == 'yes' %}
from {{ cookiecutter.project_slug }}.models import User


def test_create_user(session):
    user = User(email="test@example.com", name="Test User")
    session.add(user)
    session.commit()

    assert user.id is not None
    assert user.email == "test@example.com"
    assert user.name == "Test User"
    assert user.is_active is True
    assert user.created_at is not None
    assert user.updated_at is not None


def test_user_repr(session):
    user = User(email="test@example.com", name="Test")
    session.add(user)
    session.commit()

    assert "test@example.com" in repr(user)
{% else %}
def test_placeholder():
    # add your model tests here
    assert True
{% endif %}
