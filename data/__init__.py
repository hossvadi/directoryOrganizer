from multiprocessing import parent_process
from pathlib import Path

from joblib import parallel_backend

DATA_DIR = Path(__file__).resolve().parent
