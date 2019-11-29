file = open('alice.txt', 'r')
count = 0
for line in file:
    count += 1
print('Line count # ' ,count)