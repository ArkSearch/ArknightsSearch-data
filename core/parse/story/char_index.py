__all__ = ['char_id2story', 'char_name2story']

import re

from .data import raw_text_data

c1 = re.compile(r'name\d?="([^#$]+?)["#$]')
c2 = re.compile(r'\[[Cc](?:haracter|harslot)\((.+?)\)]')
c3 = re.compile(r'\[name\d?="(.+?)"]')

char_id2story: dict[str, list[str]] = {}
char_name2story: dict[str, list[str]] = {}

for story, text in raw_text_data['zh_CN'].items():
    match = set()
    text = text.replace(' ', '')
    [[match.add(j) for j in c1.findall(i)] for i in c2.findall(text)]
    for char_id in match:
        if char_id in char_id2story:
            char_id2story[char_id].append(story)
        else:
            char_id2story[char_id] = [story]

    for char_name in set(c3.findall(text)):
        if char_name in char_name2story:
            char_name2story[char_name].append(story)
        else:
            char_name2story[char_name] = [story]
