file = open('alice.txt')
for line in file:
    line = line.rstrip()
    if line.startswith("Alice"):
        print(line)