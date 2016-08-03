from string import punctuation

def reverse(s):
    if s == "":
        return s
    else:
        return s[-1] + reverse(s[:-1])

def cheatPalindrome(s):
    if reverse(s) == s or len(s) == 1:
        return True
    else:
        return False

def removeWhite(s):
    # punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
    s = s.replace(" ", "")
    mystr = ''
    for char in s:
        if char not in punctuation:
            mystr += char
    print(mystr)
    return mystr

def isPalindrome(s):
    if s == "" or len(s) == 0:
        return True
    if s[0].lower() == s[-1].lower():
        return isPalindrome(s[1:-1])
    else:
        return False



string = "Go hang a salami; Im a lasagna hog."
print(reverse(string))

print(cheatPalindrome(string))
print(isPalindrome(removeWhite(string)))

