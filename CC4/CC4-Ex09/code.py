fname =input('Enter a file name: ')
if fname == 'na na boo boo':
    print("NA NA BOO BOO TO YOU - you have been punk'd")
    quit()
try:
    fhand = open(fname)
except:
    print('File cannot be open:',fname)
    quit()
count = 0
for line in fhand:
    if line.startswith('Subject:'):
        count = count + 1
print('There were',count , 'subject lines in' , fname)