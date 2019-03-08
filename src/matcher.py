import json
import os
import random
from pprint import pprint

def load_data(filename):

    if filename is None:
        raise ValueError("None is not a valid file name")

    with open(os.path.abspath(filename)) as json_file:
        #raw_data = open(filename).read()
        
        return json.load(json_file)

def random_choose(available, key, eliminate=False):
    candidates = available[key]
    choosen = random.choice(candidates)
    if eliminate:
        candidates.remove(choosen)
        available[key] = candidates
    return choosen, available

players = load_data('players.json')
missions = load_data('missions.json')
deployments = load_data('deployments.json')

while len(players["players"]) > 1:
    player1, players = random_choose(players, "players", eliminate=True)
    player2, players = random_choose(players, "players", eliminate=True)
    deployment, deployments = random_choose(deployments, "deployments")
    mission, missions = random_choose(missions, "missions")

    print ("Match %(player1)s vs %(player2)s Mission: %(mission)s Map: %(map)s" % \
    {
        "player1": player1["name"], 
        "player2": player2["name"],
        "mission": mission["name"],
        "map": deployment["name"]
    })

consolation_deployment, deployments = random_choose(deployments, "deployments")
consolation_mission, missions = random_choose(missions, "missions")
print ("Consolation Match Mission: %(mission)s Map: %(map)s" % \
{
    "mission": consolation_mission["name"],
    "map": consolation_deployment["name"]
})

final_deployment, deployments = random_choose(deployments, "deployments")
final_mission, missions = random_choose(missions, "missions")
print ("Final Match Mission: %(mission)s Map: %(map)s" % \
{
    "mission": final_mission["name"],
    "map": final_deployment["name"]
})





