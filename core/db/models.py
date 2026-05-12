from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy import Float
from sqlalchemy import Text
from sqlalchemy import DateTime

from datetime import datetime

from core.db.database import Base


class Finding(Base):

    __tablename__ = "findings"

    id = Column(Integer, primary_key=True)

    module = Column(String(50))
    finding_id = Column(String(50))

    severity = Column(String(20))
    score = Column(Float)

    category = Column(String(100))
    target = Column(String(255))

    description = Column(Text)
    detail = Column(Text)
    fix = Column(Text)

    created_at = Column(DateTime, default=datetime.utcnow)