empty_list = []
try:
    while True:
        numbers = input('Enter ')
        if numbers == 'done':
            break
        empty_list.append(int(numbers))
except:
    print('That is not a number')
    while True:
        numbers = input('Enter ')
        if numbers == 'done':
            break
        empty_list.append(int(numbers))

min = empty_list[0]
max = empty_list[0]
for empty_list in empty_list:
    if empty_list < min:
        min = empty_list
    elif empty_list > max:
        max = empty_list
    
print(min, max)