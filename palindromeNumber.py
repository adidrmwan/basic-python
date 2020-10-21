def is_palindrome(num):
    
    for i in range(len(num)/2):
        if num[i] != num[len(num)-i-1]:
            return False
    return True


n = int(input())
num = []
for i in range(n):
    nums = int(input())
    num.append(nums)

print(is_palindrome(num))