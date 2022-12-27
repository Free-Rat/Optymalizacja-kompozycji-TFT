import random
from collections import defaultdict

def generate_optimal_teams(champions, trait_weights):
  # Create a dictionary to store the teams
  teams = defaultdict(list)
  
  # Create a list of available traits
  traits = list(trait_weights.keys())
  
  # Create a list of champions that have not been added to a team yet
  remaining_champions = champions.copy()
  
  # Loop through each trait
  for trait in traits:
    # Create a list of champions that have the current trait
    trait_champions = [champion for champion in remaining_champions if trait in champion["traits"]]
    
    # Randomly select a champion from the list of trait champions
    chosen_champion = random.choice(trait_champions)
    
    # Remove the chosen champion from the remaining champions list
    remaining_champions.remove(chosen_champion)
    
    # Add the chosen champion to the team with the current trait
    teams[trait].append(chosen_champion)
  
  # Return the generated teams
  return teams

# Define a list of available champions
# Define a dictionary of champions and their traits in Teamfight Tactics
champions = {
    "Aatrox": ["Demon", "Blademaster"],
    "Ahri": ["Wild", "Sorcerer"],
    "Akali": ["Ninja", "Assassin"],
    "Annie": ["Human", "Sorcerer"],
    "Ashe": ["Glacial", "Ranger"],
    "Aurelion Sol": ["Dragon", "Sorcerer"],
    "Blitzcrank": ["Robot", "Brawler"],
    "Brand": ["Demon", "Sorcerer"],
    "Braum": ["Glacial", "Guardian"],
    "Caitlyn": ["Noble", "Ranger"],
    "Cho'Gath": ["Void", "Brawler"],
}

# Print the dictionary to see its contents
print(champions)


#write a python script generating optimal team comb in teamfight tactics, using randomized greedy algorithm  10 times, and taking in to consideration how much important is every trait, to given team capacity 