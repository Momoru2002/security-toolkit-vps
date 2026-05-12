from core.db.database import engine
from core.db.models import Base


def init_database():

    Base.metadata.create_all(bind=engine)