import os
from pathlib import Path
from dotenv import load_dotenv

def config():

    load_dotenv()
    
    def get_key(name: str, default: str = None) -> str:
        return os.getenv(name, default)

    PROJECT_ROOT = Path.cwd()

    data_dir_env = get_key("DATA_DIR", "./data")
    DATA_DIR = PROJECT_ROOT / data_dir_env
    DATA_DIR.mkdir(parents=True, exist_ok=True)
    
    print("PROJECT_ROOT:", PROJECT_ROOT)
    print("DATA_DIR:", DATA_DIR)
    print("API_KEY present:", get_key("API_KEY") is not None)
    print("DATA_DIR from env:", data_dir_env)
    print("Ensured data directory exists.")

if __name__ == "__main__":
    config()