import random
import newfuncje

#size of team
TEAM_CAPACITY = 8

#base parametters
AMOUNT_OF_CHAMPIONS = 15
AMOUNT_OF_TRAITS = 6

#declaring parameters for traits
MIN_AMOF_TRAITS = 2
MAX_AMOF_TRAITS = [3]
dencity_tab = [MIN_AMOF_TRAITS]*3
dencity_tab.extend(MAX_AMOF_TRAITS) 

IMORTANCE_OF_COMBO = 0.7

#generating a random set of champions and their traits as a matrix
champion_pool = newfuncje.generte_matrix(AMOUNT_OF_CHAMPIONS, AMOUNT_OF_TRAITS, dencity_tab)
newfuncje.printmatrix(champion_pool, "champions")
print("~~~~~~~~~~~~~")
#generate lists of champions that have same trait
tabs = newfuncje.generate_tabs(champion_pool)
newfuncje.printmatrix(tabs , "traits")
#print(tabs)

#generaging a random importance of every trait
weights = newfuncje.generate_vector(AMOUNT_OF_TRAITS , "weights")
print(weights, "vector of importance ")

#generating a random active limit for every trait
active_limits = newfuncje.generate_vector(AMOUNT_OF_TRAITS , "limits")
print(active_limits , "vector of limits " )

#generating optimal team using randomised greedy algorithm
teamg = newfuncje.generate_optimal_team_g(champion_pool , TEAM_CAPACITY,IMORTANCE_OF_COMBO, weights , active_limits , tabs)
print('optimal team (GREEDY): ',teamg)

#generating optimal team using bruteforse
teamb = newfuncje.generate_optimal_team_bf(champion_pool, TEAM_CAPACITY)
print("optimal team (BF)", teamb)

#TODO
#1 program sie wysypuje gdy jakas cecha jest pusta
#wykresy od czasu i ilosci elemnetow
#brutefroce 
#metaheurystyka
#testy poprawnosci
#