__all__ = ['zone_name']

from core.util import json
from core.constant import activity_path, support_language

zone_name: dict[str, dict[str, str]] = {}

for lang in support_language:
    activity_data = json.load(activity_path % lang)['basicInfo']
    for _id, data in activity_data.items():
        if _id in zone_name:
            zone_name[_id][lang] = data['name']
        else:
            zone_name[_id] = {lang: data['name']}
