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
    reversedstring = ''
    s = Stack()
    for i in mystr:
    	s.push(i)
    while not s.isEmpty():
        reversedstring += s.peek()
        s.pop()
    return reversedstring

print(revstring('woohoo! it worked.'))