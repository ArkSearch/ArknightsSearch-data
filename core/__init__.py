import os

from .constant import data_path

if not os.path.exists(data_path):
    os.makedirs(data_path)
