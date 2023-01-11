import random
def aleatoire():
    number = int(input('Entrer un nombre quelconque'))
    random_number = random.randint(1, 100)
    print(random_number)
    if number==random_number:
        print('congrats!')
    else:
        print('Oups!')

aleatoire()
