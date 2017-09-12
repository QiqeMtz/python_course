from lamp import Lamp

def run():
    lamp = Lamp(is_turned_on = True)

    while True:
        command = str(raw_input('''
            What you want to do?

            p - turn on
            a - turn off
            e - exit
        '''))

        if command == 'p':
            lamp.turn_on()
        elif command == 'a':
            lamp.turn_off()
        else:
            break

if __name__ == '__main__':
    run()