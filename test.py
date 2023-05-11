import shutil
import os

MODEL_PATH = 'models/best_als'

if os.path.isdir(MODEL_PATH):
    shutil.rmtree(MODEL_PATH)