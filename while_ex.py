# -*- coding: utf-8

import random

def run():

    limit_random = int(raw_input('Cual es el limite de random?: '))

    number_found = False
    random_number = random.randint(0, limit_random)

    while not number_found:
        number = int(raw_input('Intenta un numero: '))

        if number == random_number:
            print('Felicidades. Encontraste el numero')
            number_found =  True
        elif number > random_number:
            print('El numeor es mas pequeño')
        else:
            print('El numero es mas grande')


if __name__ == '__main__':
    run()