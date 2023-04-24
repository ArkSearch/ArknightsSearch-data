import simdjson


class Json:
    @staticmethod
    def dump(data, path: str):
        with open(path, mode='wt', encoding='utf-8') as f:
            return simdjson.dump(data, f, ensure_ascii=False, indent=2)

    @staticmethod
    def load(path: str):
        with open(path, mode='rt', encoding='utf-8') as f:
            return simdjson.load(f)


json = Json


def sort_dict(data: dict, depth: int = 0):
    if depth:
        return dict(sorted(((i[0], sort_dict(i[1], depth - 1)) for i in data.items()), key=lambda x: x[0]))
    else:
        return dict(sorted(data.items(), key=lambda x: x[0]))
