import random
import newfuncje
import threading
import queue

queue = queue.Queue()

# size of team
TEAM_CAPACITY = 8

# base parametters   (51 , 29)
# s -> startowe
# e -> koncowe
s_nchampions = 20
s_ntraits = 12

e_nchampions = 21
e_ntraits = 29

# declaring parameters for traits
MIN_AMOF_TRAITS = 2
MAX_AMOF_TRAITS = 3
dencity_tab = [MIN_AMOF_TRAITS]*3
dencity_tab.extend([MAX_AMOF_TRAITS])

IMORTANCE_OF_COMBO = 3

N_random = 1000  # ile razy losowy dobór bedzie powtarzany
N_greedy = 1000  # ile razy greedy algortym bedzie powtarzany

newfuncje.clean_file(newfuncje.F_NAME)


def main(nchampions, ntraits):

    # generating a random set of champions and their traits as a matrix
    champion_pool = newfuncje.generte_matrix(
        nchampions, ntraits, dencity_tab)
    #newfuncje.printmatrix(champion_pool, "champions")
    print()

    # generate lists of champions that have same trait
    tabs = newfuncje.generate_tabs(champion_pool)
    #newfuncje.printmatrix(tabs, "traits")
    print()

    # generaging a random importance of every trait
    weights = newfuncje.generate_vector(ntraits, "weights")
    #print(weights, "vector of importance ")

    # generating a random active limit for every trait
    active_limits = newfuncje.generate_vector(ntraits, "limits")
    #print(active_limits, "vector of limits ")
    print()

    newfuncje.write_to_file(newfuncje.F_NAME, 'n_champions',
                            cu_champs, " ", 'n_traits', cu_traits, " ")

    # generating optimal team using randomised greedy algorithm
    t_greedy = threading.Thread(target=newfuncje.generate_optimal_team_g, args=(
        queue, champion_pool, TEAM_CAPACITY, IMORTANCE_OF_COMBO, weights, active_limits, tabs, N_greedy))
    t_greedy.start()

    # generating optimal team using bruteforse
    t_bruteforce = threading.Thread(target=newfuncje.generate_optimal_team_bf, args=(
        queue, champion_pool, TEAM_CAPACITY, IMORTANCE_OF_COMBO, weights, active_limits))
    t_bruteforce.start()

    # genreating random team and calculating average value and max value
    average_v, max_v, time_r = newfuncje.generate_random_team(
        queue, champion_pool, TEAM_CAPACITY, IMORTANCE_OF_COMBO, weights, active_limits, N_random)

    print("losowy: srednia:", average_v, 'maxymalna:', max_v)
    print("czas:", time_r)
    print()

    t_greedy.join()
    teamg, vg, time_g = queue.get()
    print('optimal team (GREEDY): ', teamg, "and has value: ", vg)
    print("czas:", time_g)
    print()

    t_bruteforce.join()
    teamb, vb, time_bf = queue.get()
    print("optimal team (BF)", teamb, "and has value: ", vb)
    print("czas:", time_bf)
    print()


cu_champs = s_nchampions
cu_traits = s_ntraits

while True:
    if cu_champs == e_nchampions + 1:
        break

    print("nchamps: ", cu_champs)
    print("ntraits: ", cu_traits)
    try:
        main(cu_champs, cu_traits)
    except ValueError:
        continue

    cu_champs += 1
    cu_traits += 1


# TODO
#
# testy poprawnosci
