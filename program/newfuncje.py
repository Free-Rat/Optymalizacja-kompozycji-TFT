import random
from itertools import combinations


def sort_tabs(tab1, tab2):
    zipped_tabs = zip(tab1, tab2)
    sorted_zipped_tabs = sorted(zipped_tabs, key=lambda x: x[0], reverse=True)
    sorted_tab1, sorted_tab2 = zip(*sorted_zipped_tabs)

    return [list(sorted_tab1), list(sorted_tab2)]


def generte_matrix(nrows, ncol, dencity):
    matrix = []
    for i in range(0, nrows):
        tab = [0]*ncol
        for p in range(0, random.choice(dencity)):
            tab[random.randrange(ncol)] = 1
        else:
            tab.extend([int(round(random.random(), 2)*100)])

        matrix.append(tab)
    return matrix


def generate_tabs(matrix):
    tabe = []
    for i in range(len(matrix[0])-1):
        tab = []
        for j in range(len(matrix)):
            if matrix[j][i] == 1:
                #print(matrix[i][j], i , j)
                tab.extend([j])

        vchamps = []
        for j in tab:
            vchamps.extend([matrix[j][-1]])
        vchamps, tab = sort_tabs(vchamps, tab)
        tabe.append(tab)

    return tabe


def generate_vector(lenght, mode):
    vector = []
    if mode == "weights":
        for i in range(0, lenght):
            vector.extend([round(random.random(), 2)])
    elif mode == "limits":
        for i in range(0, lenght):
            vector.extend([random.choice([2, 2, 2, 3, 4])])
    return vector


def printmatrix(matrix, mode):
    i = 0
    for row in matrix:
        if mode == "traits":
            print(f'trait {i}: ', end="  ")
        for cell in row:
            print(cell, end=" ")
        if mode == "champions":
            print(f'champion {i}', end="  ")

        i += 1
        print()


def count_points_t(matrix, team, combo_v, weights, limits):
    sum = 0
    traits = [0]*(len(matrix[0])-1)

    # value of champs
    for i in range(len(team)):
        sum += (matrix[team[i]][-1] / 100)

    # caltuate traits
    for i in team:
        for j in range(len(matrix[0])-1):
            traits[j] += matrix[i][j]
        
    #print(traits , team )

    # importace of active traits and combo
    for i in range(len(traits)):
        sum += (traits[i] // limits[i]) * weights[i] * combo_v
    #print(team, sum)
    return sum


def optimal_chamion(matrix, actual_traits, combo_importance, weights, limits, tabs, ac_team):
    index = 0
    copy_traits = actual_traits[:]
    bvchamps = []

    if ac_team == []:
        index = random.randrange(len(matrix))
        #print(index)
    else:
        # szukamy w traitach ktore juz sa w druzynie
        best = 0

        for i in range(len(actual_traits)):
            #print(weights[i] , max(weights))

            if weights[i] == max(weights):
                bvchamps = tabs[i][:3]
        # print(bvchamps)

        for i in bvchamps:
            # print(i)
            if i == None:
                print("skip")
                continue

            else:
                # srednia wag
                sawag = 0
                for j in range(len(matrix[0])):
                    if matrix[i][j] == 1:
                        sawag += weights[j]/limits[j]
                sawag = sawag/len(matrix)

                # for j in range(len(matrix)):
                nactual = 0
                ncopy = 0
                for j in range(len(matrix[0])-1):
                    copy_traits[j] = actual_traits[j] + matrix[i][j]
                    nactual += actual_traits[j]//limits[j]
                    ncopy += copy_traits[j]//limits[j]

                # suma punktow
                pnk = matrix[i][-1] + sawag + \
                    (nactual - ncopy)*combo_importance

                if pnk >= best:
                    index = i

    # champion remove
    for i in range(len(matrix[0])-1):
        try:
            tabs[i].remove(index)
        except:
            pass
        if tabs[i] == []:
            weights[i] = 0
            # print("JD")

    # printmatrix(tabs,"traits")
    # print(weights)
    # print("wziety element: ", index)
    # printmatrix(matrix, "champions")
    # print(actual_traits)
    for j in range(len(matrix[0])-1):
        actual_traits[j] = actual_traits[j] + matrix[index][j]
    #print(weights, "w algo")
    return index, actual_traits, matrix, weights, limits, tabs


def generate_optimal_team_g(matrix, size,  combo_importance, weights, limits, tabs, n):
    maxteam = []
    maxv = 0
    ctabs = [row[:] for row in tabs]
    cweights = weights[:]
    for _ in range(0, n):
        team = []
        traits = [0]*(len(matrix[0])-1)
        tabs = [row[:] for row in ctabs]
        weights = cweights[:]
        for i in range(0, size):
            new_champ, traits, matrix, weights, limits, tabs = optimal_chamion(
                matrix, traits, combo_importance, weights, limits, tabs, team)
            team.extend([new_champ])

        team = sorted(team)
        if team in maxteam:
            continue

        v = count_points_t(matrix, team, combo_importance, cweights, limits)
        if v > maxv:
            maxteam = [team]
            maxv = v
        elif v == maxv:
            maxteam.append(team)

    return maxteam, maxv


def generate_optimal_team_bf(matrix, size,  combo_importance, weights, limits):
    team = []
    maxv = 0
    numbers = list(range(len(matrix)))
    combination_list = list(combinations(numbers, size))
    for t in combination_list:
        #print(team, weights)
        v = count_points_t(matrix, list(t), combo_importance, weights, limits)
        if v > maxv:
            team = [list(t)]
            maxv = v
        elif v == maxv:
            team.append(list(t))

    return team, maxv

def generate_random_team(matrix ,size , combo_importance, weights, limits , ntimes):
    maxv = 0
    avgv = 0
    licznik = 0
    for i in range(ntimes):
        team = []

        while len(team) < size:
            index = random.randrange(len(matrix))
            if not index in team:
                team.extend([index])
            else:
                continue

        v = count_points_t(matrix, team, combo_importance, weights, limits)

        if v > maxv:
            maxv = v
        
        licznik+=v
            

    avgv = licznik/ntimes

    return team , avgv ,maxv
