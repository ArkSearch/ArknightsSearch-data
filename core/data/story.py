from typing import Optional, Union
from copy import deepcopy

from core.name import story_name, story_code, month_squad_name
from .error import InvalidData

"""
解析 story_table 中的数据
"""


class StoryData:
    id: str
    filename: str
    type: str
    name: dict[str, str]
    zone: str
    zone_name: dict[str, str]
    data: Optional[dict]
    lang: Optional[dict[str, dict[str]]]

    def __init__(self, story_id: str):
        self.id = story_id
        self.filename = story_id.split('/')[-1]

    def set_name(self, name: str, _type: str):
        data = deepcopy(self.lang[_type])
        for key in data:
            data[key] = data[key] % name
        self.name = data

    @property
    def dump(self) -> dict:
        return {
            'id': self.id,
            # 'filename': self.filename,
            'type': self.type,
            'name': self.name,
            'zone': self.zone
        }


class MemoryData(StoryData):
    def __init__(self, story_id: str):
        super().__init__(story_id)
        self.type = 'Memory'
        self.name = story_name[self.id]
        # 角色id
        self.zone = self.filename.split('_', 3)[1]


class MainData(StoryData):
    lang = {
        'beg': {
            'zh_CN': '%s 行动前'
        },
        'end': {
            'zh_CN': '%s 行动后'
        },
        'recap': {
            'zh_CN': '第%s章回顾'
        },
        'raw': {
            'zh_CN': '%s'
        }
    }

    def __init__(self, story_id: str):
        super().__init__(story_id)
        self.type = 'Main'
        self.parse_name()
        self.parse_zone()

    def parse_name(self):
        group = self.filename.split('_')
        if group[0] == 'level':
            if group[-1] == 'recap':
                return self.set_name(group[2], 'recap')
            elif group[1] == 'main':
                return self.set_name(story_code[self.id], group[3])
            elif group[1] in ['st', 'spst']:
                return self.set_name(story_code[self.id], 'raw')
        elif group[0] == 'main':
            if '_'.join(group[-2:]) == 'zone_enter':
                # 已知剧情(10/11章)仅有视频资源，无文本
                raise InvalidData

        raise TypeError(f'Unknown story type {self.id}')

    def parse_zone(self):
        group = self.filename.split('_')
        if group[0] == 'level':
            if group[-1] == 'recap':
                self.zone = f'main_{group[2]}'
            elif group[1] in ['main', 'st', 'spst']:
                self.zone = f'main_{int(group[2].split("-")[0])}'
            else:
                raise TypeError(f'Unknown zone {self.id}')
        elif group[-1] == 'enter':
            self.zone = f'main_{group[1]}'
        else:
            raise TypeError(f'Unknown zone {self.id}')


class RogueData(StoryData):
    def __init__(self, story_id: str):
        super().__init__(story_id)
        self.type = 'Rogue'
        self.parse_name()
        self.zone = 'rogue_' + self.filename.split('_')[3]

    def parse_name(self):
        group = self.filename.split('_')
        name = deepcopy(month_squad_name['_'.join(group[:-1])])
        for key in name:
            name[key] = f'{name[key]} Part.0{group[-1]}'
        self.name = name


class ActivityStory(StoryData):
    lang = {
        'beg': {
            'zh_CN': '%s 行动前'
        },
        'end': {
            'zh_CN': '%s 行动后'
        },
        'raw': {
            'zh_CN': '%s'
        },
        'entry': {
            'zh_CN': '%s进入活动'
        },
        'actfun': {
            'zh_CN': '愚人节剧情%s'
        },
        'lock': {
            'zh_CN': '连锁竞赛 %s'
        },
        'ending': {
            'zh_CN': '结局 %s'
        }
    }

    def __init__(self, story_id: str):
        super().__init__(story_id)
        self.type = 'Activity'
        self.parse_name()
        self.parse_zone()

    def parse_name(self):
        if self.id.split('/')[2] in ['guide', 'training', 'level']:
            # 教程关/关卡内剧情 无名称/不可再触发
            raise InvalidData
        group = self.filename.split('_')

        if self.filename == 'level_act12side_tr01_end':
            # 角你怎么训练关后塞剧情啊（
            return self.set_name('DH-TR-1', 'end')

        if group[0] == 'level':
            if group[2] == 'hidden':
                # act13side_hidden
                # 长夜临光隐藏剧情，未发现入口
                raise InvalidData
            if group[-1] == 'entry':
                return self.set_name('', 'entry')
            elif group[1].endswith('fun') or group[1] == 'act17d7':
                # 愚人节剧情
                return self.set_name(group[2], 'actfun')
            elif group[1].endswith('lock'):
                return self.set_name(group[2].removeprefix('st'), 'lock')
            elif group[1].endswith('mini'):
                # 迷你故事集
                self.name = story_name[self.id]
                return
            elif group[2] == 'ending':
                # 目前仅在生稀盐酸发现，结局剧情
                return self.set_name(group[3], 'ending')
            elif group[-1] in ['beg', 'end']:
                return self.set_name(story_code[self.id], group[-1])
            elif group[-1].startswith('st'):
                if story_code[self.id]:
                    self.set_name(story_code[self.id], 'raw')
                else:
                    self.name = story_name[self.id]
                return
        elif group[0] in {'guide', 'tutorial', 'ui'}:
            raise InvalidData

        raise TypeError(f'Unknown story type {self.id}')

    def parse_zone(self):
        self.zone = self.id.split('/')[1]
        # 自由の角（
        if self.zone == 'a001':
            self.zone = '1stact'


Data = Union[MemoryData, MainData, RogueData, ActivityStory]


class StoryParser:
    @staticmethod
    def parse(story_id: str) -> Data:
        story_id = story_id.lower()
        group = story_id.split('/')
        if group[0] == 'obt':
            # TODO record(第10/11章note)？
            if group[1] == 'memory':
                return MemoryData(story_id)
            elif group[1] == 'main':
                return MainData(story_id)
            elif group[1] == 'rogue':
                return RogueData(story_id)
            elif group[1] in [
                'tutorial',  # 关卡内引导
                'legion',  # 保全派驻引导
                'rune',  # 危机合约引导，
                'guide',  # 操作引导
                'roguelike',  # 肉鸽剧情
                'record'  # 10/11章note
                # 好懒，不想适配（
            ]:
                raise InvalidData

            else:
                raise TypeError(f'Unknown story type obt/* {group}')
        elif group[0] == 'activities':
            return ActivityStory(story_id)

        raise InvalidData
