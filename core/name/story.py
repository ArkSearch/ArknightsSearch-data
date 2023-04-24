__all__ = ['story_name', 'story_code']

from core.util import json
from core.constant import story_review_path, support_language
from .zone import zone_name

story_name: dict[str, dict[str, str]] = {}

story_code: dict[str, str] = {}


for lang in support_language:
    story_review_data = json.load(story_review_path % lang)
    for zone_id, zone_data in story_review_data.items():
        if zone_id in zone_name:
            zone_name[zone_id][lang] = zone_data['name']
        else:
            zone_name[zone_id] = {lang: zone_data['name']}

        for story_data in zone_data['infoUnlockDatas']:

            _id = story_data['storyTxt']
            name = story_data['storyName']
            code = story_data['storyCode']

            if _id in story_name:
                story_name[_id][lang] = name
            else:
                story_name[_id] = {lang: name}

            if _id not in story_code:
                story_code[_id] = code
