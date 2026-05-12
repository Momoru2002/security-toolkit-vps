from core.cli import start_cli
from core.db.init_db import init_database

if __name__ == "__main__":

    init_database()

    start_cli()