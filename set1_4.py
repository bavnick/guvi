ip = raw_input()
if len(ip) > 1:
    print 'Invalid Input'
else:
    if (ip >= 'a' and ip <= 'z') or (ip >= 'A' and ip <= 'Z'):
        print 'Alphabet'
    else:
        print 'No'
