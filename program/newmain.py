import random
import newfuncje

# size of team
TEAM_CAPACITY = 6

# base parametters
AMOUNT_OF_CHAMPIONS = 20
AMOUNT_OF_TRAITS = 10

# declaring parameters for traits
MIN_AMOF_TRAITS = 2
MAX_AMOF_TRAITS = [3]
dencity_tab = [MIN_AMOF_TRAITS]*3
dencity_tab.extend(MAX_AMOF_TRAITS)

IMORTANCE_OF_COMBO = 10

N_random = 10
N_greedy = 100

# generating a random set of champions and their traits as a matrix
champion_pool = newfuncje.generte_matrix(
    AMOUNT_OF_CHAMPIONS, AMOUNT_OF_TRAITS, dencity_tab)
newfuncje.printmatrix(champion_pool, "champions")
print("~~~~~~~~~~~~~")
# generate lists of champions that have same trait
tabs = newfuncje.generate_tabs(champion_pool)
newfuncje.printmatrix(tabs, "traits")
# print(tabs)

# generaging a random importance of every trait
weights = newfuncje.generate_vector(AMOUNT_OF_TRAITS, "weights")
print(weights, "vector of importance ")

# generating a random active limit for every trait
active_limits = newfuncje.generate_vector(AMOUNT_OF_TRAITS, "limits")
print(active_limits, "vector of limits ")

# generating optimal team using randomised greedy algorithm

teamg, vg = newfuncje.generate_optimal_team_g(
    champion_pool, TEAM_CAPACITY, IMORTANCE_OF_COMBO, weights, active_limits, tabs , N_greedy)
print('optimal team (GREEDY): ', teamg, "and has value: ", vg)

# generating optimal team using bruteforse
teamb, vb = newfuncje.generate_optimal_team_bf(
    champion_pool, TEAM_CAPACITY, IMORTANCE_OF_COMBO, weights, active_limits)
print("optimal team (BF)", teamb, "and has value: ", vb)

# genreating random team and calculating average value and max value
team , average_v , max_v = newfuncje.generate_random_team(champion_pool, TEAM_CAPACITY,IMORTANCE_OF_COMBO,weights,active_limits,N_random)
print(average_v , max_v)

# TODO
# 1 program sie wysypuje gdy jakas cecha jest pusta
# wykresy od czasu i ilosci elemnetow
# brutefroce
# metaheurystyka
# testy poprawnosci
#
#  # srednia wag
#  sawag = 0
#   for j in range(len(matrix[0])):
#        if matrix[i][j] == 1:
#            sawag += weights[j]/limits[j]
#    sawag = sawag/len(matrix)
#
#    # for j in range(len(matrix)):
#    nactual = 0
#    ncopy = 0
#    for j in range(len(matrix[0])-1):
#        copy_traits[j] = actual_traits[j] + matrix[i][j]
#        nactual += actual_traits[j]//limits[j]
#        ncopy += copy_traits[j]//limits[j]
#
#    # suma punktow
#    pnk = matrix[i][-1] + sawag + (nactual - ncopy)*combo_importance
#
#    if pnk >= best:
#        index = i
