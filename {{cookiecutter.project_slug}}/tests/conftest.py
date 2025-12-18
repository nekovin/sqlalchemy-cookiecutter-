import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from {{ cookiecutter.project_slug }}.models import Base


@pytest.fixture(scope="function")
def engine():
    engine = create_engine("sqlite:///:memory:")
    Base.metadata.create_all(engine)
    yield engine
    Base.metadata.drop_all(engine)


@pytest.fixture(scope="function")
def session(engine):
    Session = sessionmaker(bind=engine)
    session = Session()
    yield session
    session.close()
