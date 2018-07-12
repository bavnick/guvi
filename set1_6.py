def check_leap(num):
    if num % 400 == 0:
        return 'yes'
    elif num % 100 == 0:
        return 'yes'
    elif num%4 == 0:
        return 'yes'
    return 'no'
try:
    n = int(raw_input())
    print check_leap(n)
except:
    print 'Tnvalid Input'
