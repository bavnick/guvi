ip = raw_input().split()
n = int(ip[0])
k = int(ip[1])
arr = raw_input().split()
for i in range(n):
    arr[i] = int(arr[i])
sum = 0
for i in range(k):
    sum += arr[i]
print sum
