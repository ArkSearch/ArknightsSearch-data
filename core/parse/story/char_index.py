__all__ = ['char_index']

import re

from .data import raw_text_data

c1 = re.compile(r'name\d?="([^#$]+?)["#$]')
c2 = re.compile(r'\[[Cc](?:haracter|harslot)\((.+?)\)]')

char_index: dict[str, list[str]] = {}

for story, text in raw_text_data['zh_CN'].items():
    match = set()
    [[match.add(j) for j in c1.findall(i)] for i in c2.findall(text.replace(' ', ''))]
    for char in match:
        if char in char_index:
            char_index[char].append(story)
        else:
            char_index[char] = [story]
