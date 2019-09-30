empty_list = []
try:
    while True:
        numbers = input('Enter ')
        if numbers == 'done':
            break
        empty_list.append(int(numbers))
except:
    print('Invalid input')
    while True:
        numbers = input('Enter ')
        if numbers == 'done':
            break
        empty_list.append(int(numbers))
count = len(empty_list)
total = 0 
for empty_list in empty_list:
    total = total + empty_list
average = total / count
print(total, count, average)