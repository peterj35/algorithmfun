def reverseString(s):
    """
    :type s: str
    :rtype: str
    """
    mystr = ""
    for letter in s:
        mystr = letter + mystr
        
    return mystr

print(reverseString("hello"))