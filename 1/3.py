def URLify(astring):
    mystring = ''
    for i in astring:
        if i == ' ':
            mystring += '%20'
        else:
            mystring = mystring + i

    return mystring

print(URLify('Mr John Smith'))