# See if you can improve upon the program in the self check by keeping letters that are correct and 
# only modifying one character in the best string so far. This is a type of algorithm in the class of 
# ‘hill climbing’ algorithms, that is we only keep the result if it is better than the previous one.

import random

def main():
    goalstring = 'methinks it is like a weasel'
    bestscore = 0
    beststring = ''
    tries = 0
    mystring = ''
    print(goalstring)

    while bestscore < len(goalstring):
        mystring = generate(mystring, len(goalstring))
        score, mystring = compare(mystring, goalstring)
        if score > bestscore:
            bestscore = score
            beststring = mystring
        if tries % 10 == 0:
            print('TRY #: ' + str(tries))
            print('BEST SCORE: ' + str(bestscore))
            print('BEST STRING: ' + str(beststring))
        tries += 1

    print('Took ' + str(tries) + ' tries, to get ' + str(mystring))

# Takes in an input of a string
# If string empty, generate a new string the size of the goalstring.
# If string is filled, replace every 0 (wrong letter) with a new random letter
# Returns the string
def generate(myString, strLength):
    randompool = "abcdefghijklmnopqrstuvwxyz "
    if myString == '':
        for i in range(0, strLength):
            letter = random.choice(randompool)
            myString += letter
    else:
        for i in range(0, strLength):
    	    if myString[i] ==  '0':
                letter = random.choice(randompool)
                myString = myString[:i] + letter + myString[i+1:]
                # mystring[i] = letter

    # print(mystring)
    return myString

# Takes in the input of the generated string, and the string we want generated
# If letters match, increment score
# If letters don't match, replace letter with 0
# Return the score and new string with 0s for wrong letters
def compare(generatedString, goalString):
    score = 0
    for i in range(0, len(generatedString)):
        if generatedString[i] == goalString[i] and generatedString[i] != '0':
            score += 1
        else:
        	generatedString = generatedString[:i] + '0' + generatedString[i+1:]
            # generatedString[i] = '0'
  
    # print(score)
    return(score, generatedString)

if __name__ == '__main__':
    main()