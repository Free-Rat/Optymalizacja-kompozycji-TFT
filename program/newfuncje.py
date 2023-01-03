import random
from itertools import combinations
import time
import queue
from bokeh.plotting import figure
from bokeh.io import show

#F_NAME = r'c:\Users\tomek\Desktop\projeckty\Optymalizacja-kompozycji-TFT\program\data.txt'
F_NAME = 'data.txt'

def get_data(filename):
    nc = []
    nt = []
    tr = []
    tg = []
    tb = []
    vr = []
    vg = []
    vb = []
    with open(filename, 'r') as f:
        txt = f.readlines()
        for i in range(len(txt)):
            if i % 5 == 0:
                nc.extend([float(txt[i].split()[1])])
            if i % 5 == 1:
                nt.extend([float(txt[i].split()[1])])
            if i % 5 == 2:
                tr.extend([float(txt[i].split()[-1])])
                vr.extend([float(txt[i].split()[0])])
            if i % 5 == 3:
                tg.extend([float(txt[i].split()[-1])])
                vg.extend([float(txt[i].split()[-2])])
            if i % 5 == 4:
                tb.extend([float(txt[i].split()[-1])])
                vb.extend([float(txt[i].split()[-2])])

    return nc, nt, tr, tg, tb, vr, vg, vb


def draw_plot(x, label,  *funk):
    colors = ['red', 'orange', 'green', 'blue',
              'indigo', 'violet', 'pink', 'purple', 'brown']
    czasy = ['random' , 'greedy', 'bruteforce']
    plot = figure()
    i = 0
    for f in funk:
        plot.line(x, f, color=colors[i], legend_label=f"{label}:{czasy[i]}")
        i += 1
    plot.legend.title = f"{label}"

    show(plot)


def write_to_file(filename, *args):
    with open(filename, 'a') as f:
        counter = 1
        for arg in args:
            if isinstance(arg, list):
                arg = [str(elem) for elem in arg]
                arg = ' '.join(arg)
            elif isinstance(arg, (int, float)):
                arg = str(arg)
            f.write(arg)
            if counter % 3 == 0:
                f.write('\n')
            else:
                f.write(' ')
            counter += 1


def clean_file(filename):
    with open(filename, 'w') as f:
        f.truncate()


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

    # importace of active traits and combo
    for i in range(len(traits)):
        sum += weights[i] * (combo_v ** (traits[i] // limits[i]))

    return sum


def optimal_chamion(matrix, actual_traits, combo_importance, weights, limits, tabs, ac_team):
    index = 0
    copy_traits = actual_traits[:]
    bvchamps = []

    if ac_team == []:
        index = random.randrange(len(matrix))
    else:
        # szukamy w traitach ktore juz sa w druzynie
        best = 0
        bw = 0
        bi = None
        for i in range(len(actual_traits)):
            if actual_traits[i] == 0:
                continue
            if weights[i] >= bw:
                bw = weights[i]
                bi = i

        bvchamps = tabs[bi][:3]
        # print(bvchamps)
        #print(actual_traits, weights, max(weights))

        for i in bvchamps:
            if i == None:
                print("skip")
                continue

            else:
                # srednia wag
                sawag = 0
                n = 0
                for j in range(len(matrix[0])-1):
                    if matrix[i][j] == 1:
                        n += 1
                        sawag += weights[j]/limits[j]
                sawag = sawag/n

                nactual = 0
                ncopy = 0
                for j in range(len(matrix[0])-1):
                    copy_traits[j] = actual_traits[j] + matrix[i][j]
                    nactual += actual_traits[j]//limits[j]
                    ncopy += copy_traits[j]//limits[j]

                # suma punktow
                pnk = matrix[i][-1] + sawag + \
                    combo_importance**(nactual - ncopy)

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

    for j in range(len(matrix[0])-1):
        actual_traits[j] = actual_traits[j] + matrix[index][j]

    return index, actual_traits, matrix, weights, limits, tabs


def generate_optimal_team_g(queue, matrix, size,  combo_importance, weights, limits, tabs, n):
    start_time = time.time()
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

    end_time = time.time()
    run_time = end_time - start_time
    queue.put((maxteam, maxv, run_time))
    write_to_file(F_NAME, maxteam, maxv, run_time)

    return maxteam, maxv, run_time


def generate_optimal_team_bf(queue, matrix, size,  combo_importance, weights, limits):
    start_time = time.time()

    team = []
    maxv = 0
    numbers = list(range(len(matrix)))
    combination_list = list(combinations(numbers, size))
    for t in combination_list:
        v = count_points_t(matrix, list(t), combo_importance, weights, limits)
        if v > maxv:
            team = [list(t)]
            maxv = v
        elif v == maxv:
            team.append(list(t))
    end_time = time.time()
    run_time = end_time - start_time
    queue.put((team, maxv, run_time))
    write_to_file(F_NAME, team, maxv, run_time)
    return team, maxv, run_time


def generate_random_team(queue, matrix, size, combo_importance, weights, limits, ntimes):
    start_time = time.time()
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
        licznik += v

    avgv = licznik/ntimes
    end_time = time.time()
    run_time = end_time - start_time
    write_to_file(F_NAME,  avgv, maxv, run_time)

    return avgv, maxv, run_time
