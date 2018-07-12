try:
    ip = raw_input().split()
    for i in range(len(ip)):
        ip[i] = int(ip[i])
    ip.sort()
    print ip[-1]
except:
    print 'Invalid Input'
