import pprint

DEBUG = True

data = {'user': {'id': 101, 'name': "Martin", "Surname": "Novák", "age": 25, "roles": ["admin", "dev"]}}
if DEBUG:
    print(data)
    pprint.pprint(data)
