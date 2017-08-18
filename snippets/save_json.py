import json

dataset = {'name': 'Vorlin Laruknuzum', 'gold': 423, 'title': 'Acolyte', 'hp': [32, 71], 'sp': [1, 13], 'sex': 'Male', 'inventory': ['a Holy Book of Prayers (Words of Wisdom)', 'an Azure Potion of Cure Light Wounds', 'a Silver Wand of Wonder'], 'class': 'Priest'}

def export_json (file_name, content, pretty):
    with open(file_name, 'w') as f:
        json.dump(content, f, indent = 4 if pretty else None)

export_json("outfile.json", dataset, False)
