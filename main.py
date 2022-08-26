import json


def process_names():
    ukrainian_suffixes = ['enko', 'chuk', 'chak', 'yshyn', 'ishyn', 'skyi', 'vych', 'ko']
    res = []
    with open('./surnames.json', 'r') as f:
        raw_surnames = json.loads(f.read())
        for p in raw_surnames['surnames']:
            if any(map(lambda s : p['name'].endswith(s), ukrainian_suffixes)):
                res.append(p['name'])
    print('Surnames: ', len(res))
    with open('./Ukrainian.txt', 'w') as f:
        f.write('\n'.join(res))


if __name__ == '__main__':
    process_names()
