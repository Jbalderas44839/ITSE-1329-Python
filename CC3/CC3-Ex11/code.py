def first_two(string):
    y= len(string)
    if y < 2:
        r = 'String is too short'
        return r
    else:
        x = string[0:2]
        return x
        
print(first_two('H'))