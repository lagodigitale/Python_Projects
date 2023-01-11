liste=[1,2,6,4,5,9,2,4,3,0]

def liste_pair():
    pair = list()
    for i in liste:
        if liste[i] % 2 == 0:
            pair=liste[i]
            print(pair)
liste_pair()