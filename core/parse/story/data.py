__all__ = ['story_data', 'text_data', 'raw_text_data']

import os
import re

from core.util import json
from core.constant import story_table_path, roguelike_topic_path, story_path
from core.data.story import StoryParser, StoryData, InvalidData

story_data: dict[str, StoryData] = {}
text_data: dict[str, dict[str, str]] = {}
raw_text_data: dict[str, dict[str, str]] = {}

# 节省储存空间
seq = 1

for _id in json.load(story_table_path % 'zh_CN'):
    _id = _id.lower()
    try:
        story = StoryParser.parse(_id)
        story_data[str(seq)] = story
        seq += 1
    except InvalidData:
        pass

for rogue_data in json.load(roguelike_topic_path % 'zh_CN')['details'].values():
    for squad in rogue_data['archiveComp']['chat']['chat'].values():
        for chat in squad['clientChatItemData']:
            _id = chat['chatStoryId'].lower()
            try:
                story_data[str(seq)] = StoryParser.parse(_id)
                seq += 1
            except InvalidData:
                pass

# 仅保留文本
r1 = re.compile(r'\[name="(.+?)"] *')
r2 = re.compile(r'\[.*?]')
r3 = re.compile(r'\n{2,}')

# 由于各语种搜索方式略有差异，目前仅支持中文
for lang in ['zh_CN']:
    data = {}
    raw_data = {}
    path = story_path % lang
    for _id, story in story_data.items():
        with open(os.path.join(path, story.id + '.txt'), mode='rt', encoding='utf-8') as f:
            text = f.read()
            data[_id] = r3.sub('\n', r2.sub('', r1.sub(r'\1: ', text)))
            raw_data[_id] = text
    text_data[lang] = data
    raw_text_data[lang] = raw_data
