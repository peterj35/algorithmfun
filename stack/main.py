from stack import Stack

s = Stack()

print(s.isEmpty())
s.push('hello - this is the first!')
s.push('byebye - this is the second.')
s.push('doggy - this is the third')
print(s.size())
s.pop()
print(s.peek())
print(s.size())
print(s.isEmpty())
while not s.isEmpty():
    print("pop pop!")
    s.pop()
print(s.isEmpty())

def revstring(mystr):
    s = Stack()
    reversedstring = ''
    for i in mystr:
    	s.push(i)
    while not s.isEmpty():
        reversedstring += s.peek()
        s.pop()
    return reversedstring

print(revstring('woohoo! it worked.'))

def parChecker(symbolString):
    s = Stack()
    balanced = True
    index = 0
    while index < len(symbolString) and balanced:
        symbol = symbolString[index]
        if symbol == "(":
            s.push(symbol)
        else:
            if s.isEmpty():
                balanced = False
            else:
                s.pop()

        index = index + 1

    if balanced and s.isEmpty():
        return True
    else:
        return False

print(parChecker('((()))'))
print(parChecker('(()'))