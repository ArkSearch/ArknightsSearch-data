import os
import hashlib
from typing import Any

import simdjson

from .constant import data_path, hash_path


class Json:
    @staticmethod
    def dump(data, path: str) -> str:
        with open(path, mode='wt', encoding='utf-8') as f:
            return simdjson.dump(data, f, ensure_ascii=False, indent=2)

    @staticmethod
    def load(path: str) -> Any:
        with open(path, mode='rt', encoding='utf-8') as f:
            return simdjson.load(f)


json = Json


def sort_dict(data: dict, depth: int = 0):
    if depth:
        return dict(sorted(((i[0], sort_dict(i[1], depth - 1)) for i in data.items()), key=lambda x: x[0]))
    else:
        return dict(sorted(data.items(), key=lambda x: x[0]))


class Save:
    def __init__(self, series: str):
        self.data_path: str = os.path.join(data_path, series)
        self.hash_path: str = os.path.join(hash_path, series)
        if not os.path.exists(self.data_path):
            os.mkdir(self.data_path)
        if not os.path.exists(self.hash_path):
            os.mkdir(self.hash_path)

    def save(self, filename: str, data: Any):
        _hash = hashlib.md5(simdjson.dumps(data, ensure_ascii=False).encode('utf-8')).hexdigest()
        with open(os.path.join(self.hash_path, filename + '.txt'), mode='wt', encoding='utf-8') as f:
            f.write(_hash)
        json.dump(data, os.path.join(self.data_path, filename + '.json'))

    def __call__(self, filename: str, data: Any):
        return self.save(filename=filename, data=data)
