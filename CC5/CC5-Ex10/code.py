fhand = open('romeo.txt' , 'r')
for line in fhand:
    word = line.split()
    words = sorted(word)
    print(words)
    