def palindrome(text1):
    for i in range(int(len(text1)/2)): 
        if text1[i] != text1[len(text1)-i-1]:
            return False
    return True

text1 = raw_input()
if(palindrome(text1)):
    print('palindrome')
else:
    print('not palindrome')
