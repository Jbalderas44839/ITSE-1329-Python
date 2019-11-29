'Juan Balderas'
count = 0
def greeter(name, last, time):
    if time == 'Morning':
        return ('Have a good breakfast, ' + name + ' ' + last[0:1])
    elif time == 'Afternoon':
        return ('Have a good lunch, ' + name + ' ' + last [0:1])
    elif time == 'Evening':
        return ('Have a good dinner, ' + name + ' ' + last [0:1])
    else:
        return ('Have a good one, ' + name + ' ' + last [0:1])
""" Function that asks what time of day it is and follows up with a greeting """

while True:
    name = input('What is your first name? ')
    last = input('What is your last name? ')
    time = input('What time of day is it (Morning, Afternoon, Evening): ')
    print(greeter(name, last, time))
    greeting = input('Would you like another greeting? ')
    count = count + 1
    if greeting == 'no':
        break
print('You received', count ,'greetings ')