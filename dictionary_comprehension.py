if __name__ == '__main__':

    # using traditional things
    cuadrados = {}
    for num in range(1, 11):
        cuadrados[num] = num**2
    
    print(cuadrados)

    # using dictionary comprehension
    squares = {num: num**2 for num in range(1, 11)}
    print(squares)