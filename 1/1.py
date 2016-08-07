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

mystring = "Helo Wrd"
# print(isUniqueChars(mystring))


def no_duplicates(str_):
    """ Determine if str_ has all unique characters """
    return len(str_) == len(set(str_))

print(no_duplicates(mystring))