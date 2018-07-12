ip = raw_input()
if len(ip) > 1:
    print 'Invalid Input'
else:
    if ip == 'a' or ip == 'e' or ip == 'i' or ip == 'o' or ip == 'u':
        print 'Vowel'
    else:
        print 'Consonant'
