import json, os

save_folder = os.path.join(os.getcwd(), 'SpaceBoardGame\\files')


planets_json = {'planets':[]}

system = [
'Omega Centaurus',
'Beta Odysseus',
'Alpha Draconis',
'Hydrus Cloud Node',
'Halo Sector',
'Deeprax Nebula',
'Elkien Cluster',
'Dorado System'
]

planet_name = [
'I',
'II',
'III',
'IV',
'V'
]

n = 1
for i in range(8):
    for x in range(5):

        new_planet =  { 
            'id': n,
            'sys_id': i + 1,
            'pla_id': x + 1,
            'system': system[i],
            'planet': 'Planet ' + planet_name[x],
            'population' : '5',
            'resources': {
                            'credits' : '2',
                            'food': '0',
                            'water': '1',
                            'ore': '1'
                        },
            'description' : 'Random text'
        }


        planets_json['planets'].append(new_planet)
        n = n + 1



list = json.dumps(planets_json, indent=4)
with open(os.path.join(save_folder, "planets.json"), "w") as outfile:
    outfile.write(list)