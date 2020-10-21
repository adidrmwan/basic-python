def isAnagram(words, sec_words):

    txt1 = sorted(words)
    txt2 = sorted(sec_words)

    if txt1 == txt2:
        return True

words = raw_input()
sec_words = raw_input()

if(isAnagram(words, sec_words)):
    print('anagram')
else:
    print('not anagram')