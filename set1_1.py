ip = raw_input()
try:
   num = int(ip)
   if num == 0:
       print 'Zero'
   elif num > 0:
       print 'Positive'
   else:
       print 'Negative'
except:
    print 'Invalid Input'
