__all__ = ['activity_id2code']

import json
from core.constant import stage_path

activity_id2code: dict[str, str] = {}

with open(stage_path % 'zh_CN', mode='rt', encoding='utf-8') as f:
    data = json.load(f)

for stage_id, stage_data in data['stages'].items():
    if stage_data['stageType'] != 'ACTIVITY':
        continue

    if not stage_data['levelId']:
        continue

    zone_id = stage_data['levelId'].split('/')[1].lower()

    if zone_id in activity_id2code:
        continue

    activity_id2code[zone_id] = stage_data['code'].split('-')[0]
