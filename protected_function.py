#A way to use decorators - decoradores
def protected(func):
    #function inside a function
    def wrapper(password):
        if password == 'platzi':
            return func()
        else:
            print('Incorrect password')
    
    return wrapper

@protected
def protected_func():
    print('Your password is correct')

if __name__ == '__main__':
    password = str(raw_input('Enter your passowrd: '))

    protected_func(password)
    
