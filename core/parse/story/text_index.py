__all__ = ['text_index']

import re

from .data import text_data

text_index: dict[str, list[str]] = {}

for story, text in text_data['zh_CN'].items():
    for char in set(re.sub(r'[\sa-zA-Z]', '', re.sub(r'\[.*?]', '', text))):
        if char in text_index:
            text_index[char].append(story)
        else:
            text_index[char] = [story]
