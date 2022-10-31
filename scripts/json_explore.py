import json, os

save_folder = os.path.join(os.getcwd(), 'SpaceBoardGame\\files')

exploration_json = {'cards':[]}

cards = [
'debris',
'planets',
'asteroid',
'accident'
]

for i in range(len(cards)):

    for ii in range(10):
        card =  { 
            'id': (i * 10 ) + ii + 1,
            'action': cards[i],
            'bonus': 'text',
            'description' : 'Random text'
        }
        exploration_json['cards'].append(card)


list = json.dumps(exploration_json, indent=4)
with open(os.path.join(save_folder, "exploration.json"), "w") as outfile:
    outfile.write(list)
