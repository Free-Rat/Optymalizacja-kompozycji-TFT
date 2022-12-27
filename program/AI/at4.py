import random
from collections import Counter

def generate_team_combs(traits, units, team_capacity):
    team_combs = []
    
    while len(team_combs) < team_capacity:
        team = []
        trait_counts = Counter()
        
        for unit in units:
            if trait_counts[unit['trait']] < 6:
                team.append(unit)
                trait_counts[unit['trait']] += 1
        
        team_combs.append(team)
    
    return team_combs

traits = ['assassin', 'blademaster', 'elementalist', 'ranger', 'shapeshifter']
units = [
    {'name': 'Akali', 'trait': 'assassin'},
    {'name': 'Garen', 'trait': 'blademaster'}]