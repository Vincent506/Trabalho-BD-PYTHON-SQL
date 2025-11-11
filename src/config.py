# src/config.py
from pathlib import Path
import os

BASE_DIR = Path(__file__).resolve().parent
# local sqlite default (apenas para desenvolvimento)
SQLITE_PATH = BASE_DIR.parent / "data" / "Banco_DE_DADOS.db"

# carregar a URL do BD via variável de ambiente (preferível para MySQL)
DATABASE_URL = os.environ.get("DATABASE_URL", f"sqlite:///{SQLITE_PATH}")

# exemplo de fallback: se você usa sqlite via sqlite3
DB_FILE = os.environ.get("DB_FILE", str(SQLITE_PATH))
