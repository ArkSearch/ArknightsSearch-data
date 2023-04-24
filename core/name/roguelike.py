__all__ = ['month_squad_name']

from core.util import json
from core.constant import roguelike_topic_path, support_language
from .zone import zone_name

month_squad_name: dict[str, dict[str, str]] = {}

for lang in support_language:
    data = json.load(roguelike_topic_path % lang)
    for _id, rogue_data in data['topics'].items():
        if _id in zone_name:
            zone_name[_id][lang] = rogue_data['name']
        else:
            zone_name[_id] = {lang: rogue_data['name']}

    for rogue_data in data['details'].values():
        for squad in rogue_data['monthSquad'].values():
            if squad['chatId'] in month_squad_name:
                month_squad_name[squad['chatId']][lang] = squad['teamName']
            else:
                month_squad_name[squad['chatId']] = {lang: squad['teamName']}
