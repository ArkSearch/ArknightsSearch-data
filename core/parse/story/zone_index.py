__all__ = ['zone_index']

from .data import story_data

zone_index: dict[str, list[str]] = {}

for _id, story in story_data.items():
    if story.zone in zone_index:
        zone_index[story.zone].append(_id)
    else:
        zone_index[story.zone] = [_id]
