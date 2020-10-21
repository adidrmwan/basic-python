def sumnNumber(num):
    
    res = 0
    for i in range(len(num)):
        res = res + num[i]
    return res

n = int(input())
num = []
for i in range(n):
    nums = int(input())
    num.append(nums)

print(sumnNumber(num))