hours = input('How many hours? ')
rate = input('Rate? ')
if float(hours) > 40 :
   ot = (float(hours) - 40) * (float(rate) * 1.5)
   print('Pay:' , 40 * float(rate) + ot)
else:
    print('Pay:' , float(hours) * float(rate))
