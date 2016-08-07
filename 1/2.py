def isPermutation(str1, str2):

    if len(str1) != len(str2):
        print("Wrong lengths")
        return False

    sorted1 = sorted(str1)
    sorted2 = sorted(str2)

    if sorted1 == sorted2:
        return True
    else:
        return False

print(isPermutation('dog', 'God'))