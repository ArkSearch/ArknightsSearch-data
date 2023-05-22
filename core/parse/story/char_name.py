__all__ = ['char_id2name', 'char_name2id']

import asyncio

import simdjson as json
import aiohttp


async def get_data():
    async with aiohttp.ClientSession() as client:
        async with client.get('https://raw.githubusercontent.com/Arkfans/ArknightsName/main/data/npc.json') as r:
            return json.loads(await r.text())


name_data: dict[str, dict[str, list[str]]] = asyncio.new_event_loop().run_until_complete(get_data())
char_name2id: dict[str, list[str]] = {}
char_id2name: dict[str, list[str]] = {}

for _id, char_name in name_data.items():
    for lang, names in char_name.items():
        if _id in char_id2name:
            char_id2name[_id].extend(names)
        else:
            char_id2name[_id] = names

        for name in names:
            if name in char_name2id:
                char_name2id[name].append(_id)
            else:
                char_name2id[name] = [_id]
