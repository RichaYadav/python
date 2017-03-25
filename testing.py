import json
from pprint import pprint
from db import database


class Testit:
    def parse_insert(self):
        file = open("test2.json")
        json_data = json.load(file)
        pprint(json_data)
        #for r in json_data['results']:
        #    kind = r['kind']




Testit().parse_insert()
