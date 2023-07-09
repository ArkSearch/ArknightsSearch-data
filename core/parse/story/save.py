from core.util import sort_dict, Save

save = Save('story')

from .data import *
from .zone_name import *
from .text_index import *
from .char_index import *
from .zone_index import *
from .char_name import *

story_data = sort_dict(story_data)
text_data = sort_dict(text_data, 1)
zone_name = sort_dict(zone_name, 1)
text_index = sort_dict(text_index)
char_id2story = sort_dict(char_id2story)
char_name2story = sort_dict(char_name2story)
zone_index = sort_dict(zone_index)
char_id2name = sort_dict(char_id2name)
char_name2id = sort_dict(char_name2id)

# 基础数据
save('story_data', {i[0]: i[1].dump for i in story_data.items()})
save('text_data', text_data)
save('zone_name', zone_name)
# text索引
save('text_index', text_index)
# char索引
save('char_id2story', char_id2story)
save('char_name2story', char_name2story)
# zone索引
save('zone_index', zone_index)
# char name数据
save('char_name2id', char_name2id)
save('char_id2name', char_id2name)
