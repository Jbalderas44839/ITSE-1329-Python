'Juan Balderas'
count = 1
def random_num():
    import random
    answer = random.randint(1,24)
    return(answer)
def greeter(name, last):
    """ greeter into function """
    x = random_num()
    print('The current hour is', x)
    if x in range(1,5):
        return ('Have a good night, ' + name + ' ' + last[0:1])
    elif x in range(5,11):
        return ('Have a good breakfast, ' + name + ' ' + last[0:1])
    elif x in range(11,16):
        return ('Have a good lunch, ' + name + ' ' + last [0:1])
    elif x in range(16,21):
        return ('Have a good dinner, ' + name + ' ' + last [0:1])
    else:
        return ('Have a good night, ' + name + ' ' + last [0:1])
""" function inside a loop """
while True:
    name = input('What is your first name? ')
    last = input('What is your last name? ')
    print(greeter(name, last))
    greeting = input('Would you like another greeting? ')
    if greeting == 'no':
        break
    count = count + 1
print('You received', count ,'greetings ')