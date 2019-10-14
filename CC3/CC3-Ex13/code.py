def not_string(string):
   x = string[0:3]
   y = string
   if x == 'not':
       return y
   else:
       return 'not ' + y
       