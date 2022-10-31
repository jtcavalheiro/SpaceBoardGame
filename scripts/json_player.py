import json, os

save_folder = os.path.join(os.getcwd(), 'SpaceBoardGame\\files')

factions_json = {'factions':[]}

faction_name = [
'Scavengers',
'Ecologists',
'x-Corp',
'Free Society'
]


for i in range(len(faction_name)):

        faction =  { 
            'id': i + 1,
            'faction': faction_name[i],
            'bonus': 'text',
            'description' : 'Random text'
        }


        factions_json['factions'].append(faction)


list = json.dumps(factions_json, indent=4)
with open(os.path.join(save_folder, "factions.json"), "w") as outfile:
    outfile.write(list)
