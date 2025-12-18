from collections.abc import Generator
from sqlalchemy import create_engine
from sqlalchemy.orm import Session, sessionmaker

from ..config import settings
from ..models import Base


_engine = None
_session_factory = None


def get_engine():
    global _engine
    if _engine is None:
        _engine = create_engine(
            settings.database_url,
            echo=settings.database_echo,
        )
    return _engine


def get_session_factory():
    global _session_factory
    if _session_factory is None:
        _session_factory = sessionmaker(
            bind=get_engine(),
            autocommit=False,
            autoflush=False,
        )
    return _session_factory


def get_session() -> Generator[Session, None, None]:
    """yields a database session, closes on exit"""
    session = get_session_factory()()
    try:
        yield session
    finally:
        session.close()


def create_all_tables() -> None:
    """creates all tables in the database"""
    Base.metadata.create_all(bind=get_engine())
