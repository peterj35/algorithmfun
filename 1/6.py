def compress(astring):

    index = 0
    newstring = ''

    while index < len(astring):
        if index+1 < len(astring) and astring[index] == astring[index+1]:
            counter = 2
            index += 1
            while index+1 < len(astring) and astring[index] == astring[index+1]:
                counter += 1
                index += 1
            newstring += astring[index-1] + str(counter)
        elif counter is not 0:
            counter = 0
            index += 1
        else:
            newstring += astring[index]
            index += 1

    return newstring

print(compress('aaabbbcccccaaacc'))