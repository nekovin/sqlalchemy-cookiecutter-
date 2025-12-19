import csv
from uuid import UUID
from sqlalchemy.orm import Session
from sqlalchemy.dialects.postgresql import insert

CHUNK_SIZE = 1000


def to_uuid(val: str) -> UUID | None:
    """convert string to uuid, return None if invalid"""
    if not val or val.strip() == "":
        return None
    try:
        return UUID(val.strip())
    except ValueError:
        return None


def to_str(val: str) -> str | None:
    """convert string to stripped string, return None if empty"""
    if not val or val.strip() == "":
        return None
    return val.strip()


def read_csv_rows(path: str):
    """stream csv rows as dicts"""
    with open(path, "r", encoding="utf-8", errors="replace") as f:
        reader = csv.DictReader(f)
        for row in reader:
            yield row


def upsert_batch(session: Session, model, records: list[dict]) -> int:
    """upsert records using postgres on conflict do update"""
    if not records:
        return 0
    stmt = insert(model).values(records)
    stmt = stmt.on_conflict_do_update(
        index_elements=["id"],
        set_={k: stmt.excluded[k] for k in records[0].keys() if k != "id"}
    )
    session.execute(stmt)
    session.commit()
    return len(records)


def insert_batch(session: Session, model, records: list[dict]) -> int:
    """insert records without upsert"""
    if not records:
        return 0
    stmt = insert(model).values(records)
    session.execute(stmt)
    session.commit()
    return len(records)
