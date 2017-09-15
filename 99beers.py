def sing(b, end):
    print(b or 'No more', 'bottle' + ('s' if b-1 else ''), end)


def run():
    for i in range(99, 0, -1):
        sing(i, 'of beer on the wall')
        sing(i, 'of beer')
        print('Take on down, and pass it around,')
        sing(i-1, 'of beer on the wall.')



if __name__ == '__main__':
    run()