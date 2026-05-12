from core.db.database import SessionLocal
from core.db.models import Finding


def save_finding(data: dict):

    db = SessionLocal()

    try:

        finding = Finding(
            module=data["module"],
            finding_id=data["id"],
            severity=data["severity"],
            score=data["score"],
            category=data["category"],
            target=data["target"],
            description=data["description"],
            detail=data["detail"],
            fix=data["fix"]
        )

        db.add(finding)

        db.commit()

    finally:
        db.close()


def get_findings():

    db = SessionLocal()

    try:
        return db.query(Finding).all()

    finally:
        db.close()