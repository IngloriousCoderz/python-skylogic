import json

content = {'name': 'Antony', 'date_of_birth': '1982-10-17', 'legs': ['left', 'right']}

string = json.dumps(content) # serializes to string
string # '{"name": "Antony", "date_of_birth": "1982-10-17", "legs": ["left", "right"]}'

content = json.loads(string) # deserializes from string
content # {'name': 'Antony', 'date_of_birth': '1982-10-17', 'legs': ['left', 'right']}

with open('db.json', 'w', encoding='utf-8') as f:
  json.dump(content, f) # serializes to file

with open('db.json', 'r', encoding='utf-8') as f:
  content = json.load(f) # deserializes from file
  print(content)
