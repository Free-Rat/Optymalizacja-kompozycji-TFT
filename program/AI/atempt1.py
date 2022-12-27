import random

# Function to calculate the total trait importance for a given team
def calculate_trait_importance(team, trait_importance_scores):
    total_importance = 0
    for champion in team:
        for trait in champion["traits"]:
            total_importance += trait_importance_scores[trait]
    return total_importance

# Function to generate a random team composition
def generate_random_team(champions, team_size):
    team = random.sample(champions, team_size)
    return team

# Function to add a new champion to a team, greedily selecting the champion
# that maximizes the total trait importance for the team
def add_champion_to_team(team, champions, trait_importance_scores):
    max_importance = 0
    best_champion = None
    for champion in champions:
        if champion not in team:
            team.append(champion)
            importance = calculate_trait_importance(team, trait_importance_scores)
            if importance > max_importance:
                max_importance = importance
                best_champion = champion
            team.remove(champion)
    return best_champion

# Function to generate an optimal team composition using a randomized greedy algorithm
def generate_optimal_team(champions, team_size, trait_importance_scores):
    team = []
    while len(team) < team_size:
        champion = add_champion_to_team(team, champions, trait_importance_scores)
        team.append(champion)
    return team

# Example usage:

# Initialize list of champions
champions = [
    {"name": "Aatrox", "traits": ["Demon", "Knight"]},
    {"name": "Ahri", "traits": ["Wild", "Sorcerer"]},
]