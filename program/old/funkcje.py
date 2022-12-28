import random

# generowanie macierzy


def generatematrix(nrows, ncolumns):
    matrix = []
    for i in range(0, nrows):
        tab = [None]*ncolumns
        for j in range(len(tab)):
            tab[j] = int((random.random()*345) % 2)
        matrix.append(tab)
        # print(tab)

    #print( matrix)
    return matrix


def printmatrix(matrix):
    for row in matrix:
        for cell in row:
            print(cell, end=" ")
        print()

# znajdywanie wszystkich kobinacji


def ncombinations(n):

    result = []

    for i in range(1, 2**n):
        maska = [0]*n
        b = bin(i)
        maska[-(len(b)-2):] = list(map(int, (list(b)[2:])))
        #print(maska )
        result.append(maska)

    return result


def combonrozmiarze(kombinacje, nmiejsc):
    # znajdywanie kombinacje o otowiednim rozmiarze
    nkombi = []
    for i in range(len(kombinacje)):
        sum = 0
        for x in kombinacje[i]:
            sum += x
        if sum == nmiejsc:
            #print( kombinacje[i] , "  " , i)
            nkombi.append(kombinacje[i])
    # funkcje.printmatrix(nkombi)
    return nkombi

# zliczanie cech


def liczeniecech(team):

    sumcech = [0]*len(team[0])
    for i in range(len(team[0])):
        for j in range(len(team)):
            sumcech[i] += team[j][i]
            #print(sumcech , team[j][i])
    return sumcech

# bruteforce


def bruteforce(nkombi, matrix, activemin):

    # zliczanie cech dla kazdej kombinacji o zadanym rozmiarze i
    # znajdywanie optimum

    max = [0]

    for i in range(len(nkombi)):
        team = []
        # print(nkombi[i])
        for j in range(len(nkombi[0])):
            if nkombi[i][j] == 1:
                team.append(matrix[j])
        printmatrix(team)
        sumacech = liczeniecech(team)
        print(sumacech)

        activtraitcount = 0

        for k in sumacech:
            if k >= activemin:
                activtraitcount += 1

        if activtraitcount > max[0]:
            max[0] = activtraitcount
            del max[1:]
            max.append(nkombi[i])

        elif activtraitcount == max[0]:
            max.append(nkombi[i])

    return max
