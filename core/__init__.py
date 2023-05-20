import os

from .constant import data_path, hash_path

if not os.path.exists(data_path):
    os.makedirs(data_path)

if not os.path.exists(hash_path):
    os.makedirs(hash_path)
