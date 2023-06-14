import json

dicionario = {
    "chaves" : ["chaves do 8","24-10-2017", "recep 01"],
    "quico": ["quico do 9", "20-05-2017","recep 02"]
}

with open("bd1.json", "w") as json_file:
    json.dump(dicionario, json_file)