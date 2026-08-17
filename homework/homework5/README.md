# Data Storage

## Project Structure
./README  
./.env.example  
./notebooks/stage05_data-storage_homework-starter  
./data/processed/util_20260817-164930  
./data/processed/sample_20260817-163751  
./data/raw/util_20260817-164930
./data/raw/sample_20260817-163751  
## Formats
### CSV
It's normal and easily readable.
### Parquet
It's good for project, because of its performance of storage and fast read/write speed. 
## How Code Reads/Writes Using Env Variables
### .env file
DATA_DIR_RAW=../data/raw
DATA_DIR_PROCESSED=../data/processed
### .ipynb file
ROOT = Path.cwd().parent  
load_dotenv(ROOT/".env")  
RAW = pathlib.Path(os.getenv('DATA_DIR_RAW'))  
PROC = pathlib.Path(os.getenv('DATA_DIR_PROCESSED'))