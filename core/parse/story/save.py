import os
from core.util import json, sort_dict

from .data import *
from .zone_name import *
from .text_index import *
from .char_index import *
from .zone_index import *

story_data = sort_dict(story_data)
text_data = sort_dict(text_data, 1)
zone_name = sort_dict(zone_name, 1)
text_index = sort_dict(text_index)
char_index = sort_dict(char_index)
zone_index = sort_dict(zone_index)

# 基础数据
json.dump({i[0]: i[1].dump for i in story_data.items()}, os.path.join(base, 'story_data.json'))
json.dump(text_data, os.path.join(base, 'text_data.json'))
json.dump(zone_name, os.path.join(base, 'zone_name.json'))
# text索引
json.dump(text_index, os.path.join(base, 'text_index.json'))
# char索引
json.dump(char_index, os.path.join(base, 'char_index.json'))
# zone索引
json.dump(zone_index, os.path.join(base, 'zone_index.json'))
