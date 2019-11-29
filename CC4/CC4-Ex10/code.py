fname =input('Enter the file name: ')
file = open(fname)
count = 0 
average = 0 
res = 0
for line in file:
    if not line.startswith("X-DSPAM-Confidence:"): continue
    count = count + 1
    fnumber = float(line[19:])
    average = fnumber + average
    res = average/count
print("Average spam confidence: ", res)