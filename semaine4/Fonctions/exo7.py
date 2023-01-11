import random
def get_random_temp():
    random_number = random.randint(-10, 40)
    print('La temperature actuelle est de ',random_number,'degrés Celsius')
    if random_number < 0:
        print(' Brrr, c’est glacial! Portez des couches supplémentaires aujourd’hui ')
    else:
        if (random_number > 0 and random_number < 13):


def main():
    get_random_temp()

main()