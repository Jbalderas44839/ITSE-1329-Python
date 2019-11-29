file = open('mbox-short.txt')
for line in file:
    line = line.rstrip()
    if line.startswith("From:"):
        print(line)