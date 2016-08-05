def isUniqueChars(astring):
    if len(astring) > 128:
        return False

    char_list = []

    for char in astring:
        if char in char_list:
            print(char + " already exists")
            return False
        else:
            char_list.append(char)

    return True

mystring = "Hello Wrd"
print(isUniqueChars(mystring))