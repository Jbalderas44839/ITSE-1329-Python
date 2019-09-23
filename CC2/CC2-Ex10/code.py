x = input('Enter score ')
try:
    if float(x) >=1:
        print('Bad Score')
    elif float(x) >=0.9:
        print('A')
    elif float(x) >= 0.8:
        print('B')
    elif float(x) >= 0.7:
        print('C')
    elif float(x) >= 0.6:
        print('D')
    elif float(x) <0.6:
        print('F')
except:
    print('Please enter numeric input')
    quit()