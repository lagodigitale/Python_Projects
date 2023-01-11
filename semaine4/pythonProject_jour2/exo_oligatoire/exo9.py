print("Entrer q pour quitter")

i = 0
j = 0

while True:

    age = input("entrer l'age de la personne qui veut un billet")
    if age=='q':
        break
    if int(age) < 3:
        print('Le billet est gratuit')
    else:
        if ((int(age) >= 3) and (int(age)>= 12)):
           i=i+1

        else:
            j=j+1
facture = i * 10 + j * 15
print("Votre facture est egale a", facture, '$')






