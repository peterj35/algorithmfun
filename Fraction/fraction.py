def gcd(m,n):
    while m%n != 0:
        oldm = m
        oldn = n

        m = oldn
        n = oldm%oldn
    return n

def reduce(m,n):
    common = gcd(m,n)

    return m//common, n//common


class Fraction:

    def __init__(self,top,bottom):
        self.num = top
        self.den = bottom

    def __getitem__(self,key):
        return 0

    def __str__(self):
        if self.num == 1 and self.den == 1:
            return str(1)
        if self.den == 1:
            return str(self.num)

        return str(self.num)+"/"+str(self.den)

    def __eq__(self,other):
        firstFraction = Fraction(*reduce(self.num, self.den))
        secondFraction = Fraction(*reduce(other.num, other.den))
        firstnum = firstFraction.num * secondFraction.den
        secondnum = secondFraction.num * firstFraction.den

        return firstnum == secondnum

    def __ne__(self,other):
        firstFraction = Fraction(*reduce(self.num, self.den))
        secondFraction = Fraction(*reduce(other.num, other.den))
        firstnum = firstFraction.num * secondFraction.den
        secondnum = secondFraction.num * firstFraction.den

        return firstnum != secondnum

    def __gt__(self,other):
        firstnum = self.num / self.den
        secondnum = other.num / other.den

        return firstnum > secondnum

    def __lt__(self,other):
        firstnum = self.num / self.den
        secondnum = other.num / other.den

        return firstnum < secondnum

    def __ge__(self,other):
        firstnum = self.num / self.den
        secondnum = other.num / other.den

        return firstnum >= secondnum

    def __lt__(self,other):
        firstnum = self.num / self.den
        secondnum = other.num / other.den

        return firstnum <= secondnum


    def __add__(self,other):
        newnum = self.num * other.den + self.den * other.num
        newden = self.den * other.den

        return Fraction(*reduce(newnum, newden))

    def __sub__(self,other):
        newnum = self.num * other.den - self.den * other.num
        newden = self.den * other.den

        return Fraction(*reduce(newnum, newden))

    def __mul__(self,other):
        newnum = self.num * other.num
        newden = self.den * other.den

        return Fraction(*reduce(newnum, newden))

    def __truediv__(self,other):
        newnum = self.num * other.den
        newden = self.den * other.num

        return Fraction(*reduce(newnum, newden))

    def __floordiv__(self,other):
        newnum = int(self.num * other.den)
        newden = int(self.den * other.num)

        return Fraction(*reduce(newnum, newden))

