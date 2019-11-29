fname =input('Enter a file name: ')
fhand =open(fname)
data =fhand.read()
print(data.upper())
