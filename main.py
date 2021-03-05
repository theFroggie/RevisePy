from cogs import app
import json

with open('RevisionSheet/Example.json', 'r') as myfile:
    data = myfile.read()

obj = json.loads(data)
print(obj["Q1name"])

app.Application()
