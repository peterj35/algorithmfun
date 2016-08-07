def oneEdit(str1, str2):

    counter = 0

    for i in str1:
        if i not in str2:
            counter += 1

    if counter >= 2:
        return False
    else:
        return True

print(oneEdit('pale', 'ple'))
print(oneEdit('pales', 'pale'))
print(oneEdit('pale', 'bale'))
print(oneEdit('pale', 'bake'))

