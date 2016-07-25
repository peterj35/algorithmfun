# See if you can improve upon the program in the self check by keeping letters that are correct and 
# only modifying one character in the best string so far. This is a type of algorithm in the class of 
# ‘hill climbing’ algorithms, that is we only keep the result if it is better than the previous one.

import random

def main():
    goallist = ['m','e','t','h','i','n','k','s',' ','i','t',' ','i','s',' ','l','i','k','e',' ','a',' ','w','e','a','s','e','l']
    bestscore = 0
    beststring = ""
    tries = 0
    mylist = initialize()
    print(goallist)

    while bestscore < 28:
        mylist = generate(mylist)
        score, mylist = compare(mylist, goallist)
        if score > bestscore:
            bestscore = score
            beststring = mylist
        if tries % 30 == 0:
            print('TRY: ' + str(tries))
            print('BEST SCORE: ' + str(bestscore))
            print('BEST STRING: ' + str(beststring))
        tries += 1
    print('Took ' + str(tries) + ' tries, to get ' + str(mylist))

def initialize():
    randompool = "abcdefghijklmnopqrstuvwxyz "
    mylist = []
    for i in range(0, 28):
        letter = random.choice(randompool)
        mylist.append(letter)

    print(mylist)
    return mylist

def generate(mylist):
    randompool = "abcdefghijklmnopqrstuvwxyz "
    for i in range(0, len(mylist)):
    	if mylist[i] ==  '0':
            letter = random.choice(randompool)
            mylist[i] = letter

    # print(mystringlist)
    return mylist

def compare(generatedList, goalList):
    score = 0
    for i in range(0, len(generatedList)):
        if generatedList[i] == goalList[i] and generatedList[i] != '0':
            score += 1
        else:
            generatedList[i] = '0'
  
    # print(score)
    return(score, generatedList)

if __name__ == '__main__':
    main()