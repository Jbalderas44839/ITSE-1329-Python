'Juan Balderas'
count = 0
name = input('What is your first name? ')
last= input('What is your last name? ')
time = input('What time of day is it (Morning, Afternoon, Evening): ')
#These are the variables that will be used throughout the problem
if time == 'Morning':
    print('Have a good breakfast,' , name , last[0:1])
elif time == 'Afternoon':
    print('Have a good lunch, ', name, last [0:1])
elif time == 'Evening':
    print('Have a good dinner, ' , name, last [0:1])
else:
    print('Have a good one, ', name, last [0:1])
#whatever the time is the output is for that specific time of day.
while True:
    greeting =input('Would you like another greeting? ')
    if greeting == 'yes':
        name = input('What is your first name? ')
        last = input('What is your last name? ')
        time = input('What time of day is it (Morning, Afternoon, Evening): ')
    if time == 'Morning':
            print('Have a good breakfast,' , name , last[0:1])
    elif time == 'Afternoon':
        print('Have a good lunch, ', name, last [0:1])
    elif time == 'Evening':
        print('Have a good dinner, ' , name, last [0:1])
    else:
        print('Have a good one, ', name, last [0:])
    count = count + 1
#if the user wants another greeting then he will receive the same questions. 
#if they dont they will have a print message for there specific time of day
    if greeting == 'no':
        break
#if the user doesn't want another greeting the output will be no
print('You received', count ,'greetings ')