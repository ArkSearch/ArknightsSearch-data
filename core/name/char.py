__all__ = ['char_name']

from core.util import json
from core.constant import char_path, support_language

char_name: dict[str, dict[str, str]] = {}

for lang in support_language:
    char_data = json.load(char_path % lang)
    for _id, data in char_data.items():
        if _id in char_name:
            char_name[_id][lang] = data['name']
        else:
            char_name[_id] = {lang: data['name']}
