if __name__ == '__main__':

    # using a normal for loop to find even numbers
    pares = []
    for num in range(1,31):
        if num % 2 == 0:
            pares.append(num)

    print(pares)

    # using list comprehension to find even numbers, oh good this is so easy

    even = [num for num in range(1,31) if num % 2 == 0]
    print(even)