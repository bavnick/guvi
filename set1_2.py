ip = raw_input()
try:
   num = int(ip)
   if num % 2 == 0:
       print 'Even'
   else:
       print 'Odd'
except:
    print 'Invalid Input'
