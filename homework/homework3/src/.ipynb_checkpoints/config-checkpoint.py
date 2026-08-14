from pathlib import Path
load_dotenv()

from typing import Optional

def get_key(name: str, default: Optional[str] = None) -> Optional[str]:
    return os.getenv(name, default)

PROJECT_ROOT = Path.cwd()
DATA_DIR = PROJECT_ROOT / "data"
print("PROJECT_ROOT:", PROJECT_ROOT)
print("DATA_DIR:", DATA_DIR)

api_key_present = get_key("API_KEY") is not None
data_dir_env = get_key("DATA_DIR", str(DATA_DIR))
print("API_KEY present:", api_key_present)
print("DATA_DIR from env:", data_dir_env)

# Ensure data directory exists (non-destructive)
Path(data_dir_env).mkdir(parents=True, exist_ok=True)
print("Ensured data directory exists.")