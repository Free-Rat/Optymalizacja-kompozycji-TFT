import random

# constants
TRAIT_IMPORTANCE = {
  'assassin': 3,
  'blademaster': 2,
  'brawler': 1,
  'elementalist': 4,
  'guardian': 2,
  'gunslinger': 3,
  'knight': 1,
  'ranger': 3,
  'shapeshifter': 4,
  'sorcerer': 4
}
TEAM_SIZE = 9

# function to generate a team composition using a randomized greedy algorithm
def generate_team_composition():
  # create a list of all available traits
  traits = list(TRAIT_IMPORTANCE.keys())
  # create an empty list to store the team composition
  team = []

  # while the team is not full, choose a random trait and add it to the team
  # if the trait is already present in the team, discard it and choose a new one
  while len(team) < TEAM_SIZE:
    trait = random.choice(traits)
    if trait not in team:
      team.append(trait)

  # sort the team by the importance of their traits
  team.sort(key=lambda trait: TRAIT_IMPORTANCE[trait], reverse=True)

  return team

# run the algorithm 10 times and print the resulting team compositions
for i in range(10):
  team = generate_team_composition()
  print(f'Team {i+1}: {team}')
