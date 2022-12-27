import funkcje

def main():

    nteamu = int(input("Podaj ile elementow w kompozycji: "))
    ncech = int(input("Podaj ilczbe cech dla kazdego elemntu: "))
    nmiejsc = int(input("Podaj ile ma byc miejsc w druzynie: "))

    activemin = 2 #dolny limit iloci cech
    activemax = 0 #gorne ograniczenie cech
    matrix = funkcje.generatematrix( nteamu , ncech)
    funkcje.printmatrix(matrix)
    print("-"*nteamu)

    kombinacje =  funkcje.ncombinations(len(matrix))
    nkombi = funkcje.combonrozmiarze(kombinacje, nmiejsc)
    max = funkcje.bruteforce(nkombi , matrix , activemin)

    print("Maksymalna liczba aktywnych cech to: ",max[0])
    print("Kompozycje ktore zawieraly maksymalna ilosc cech", max[1:])

    #print(team)


main()
