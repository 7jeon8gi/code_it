def is_palindrome(word):
    word2 = word[::-1]
    if word2 == word:
        return True
    else:
        return False
        
def is_palindrome2(word):
    for i in range(len(word)//2):
        if word[i] == word[-(i+1)]:
            continue
        else:
            return False
    else:
        return True        
        
        
# 테스트
print(is_palindrome("racecar"))
print(is_palindrome("stars"))
print(is_palindrome("토마토"))
print(is_palindrome("kayak"))
print(is_palindrome("hello"))
