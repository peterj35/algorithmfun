from fraction import Fraction

f1 = Fraction(3,4)
f2 = Fraction(1,4)

f3 = Fraction(5,4)
f4 = Fraction(1,4)

f5 = f1 + f2
print("%s added by %s is %s." % (f1,f2,f5))

f5 = f3 + f4
print("%s added by %s is %s." % (f3,f4,f5))

f5 = f1 - f2
print("%s subtracted by %s is %s." % (f1,f2,f5))

f5 = f3 - f4
print("%s subtracted by %s is %s." % (f3,f4,f5))

f5 = f1 * f2
print("%s multiplied by %s is %s." % (f1,f2,f5))

f5 = f3 + f4
print("%s multiplied by %s is %s." % (f3,f4,f5))

f5 = f1 / f2
print("%s divided by %s is %s." % (f1,f2,f5))

f5 = f3 / f4
print("%s divided by %s is %s." % (f3,f4,f5))

f1 = Fraction(14,5)
f2 = Fraction(14,5)
f3 = f1 == f2
print("The statement '%s is equal to %s' is %s." % (f1,f2,f3))

f1 = Fraction(1,2)
f2 = Fraction(2,4)
f3 = f1 == f2
print("The statement '%s is equal to %s' is %s." % (f1,f2,f3))

f1 = Fraction(1,3)
f2 = Fraction(2,4)
f3 = f1 == f2
print("The statement '%s is equal to %s' is %s." % (f1,f2,f3))

f1 = Fraction(14,5)
f2 = Fraction(14,5)
f3 = f1 != f2
print("The statement '%s is NOT equal to %s' is %s." % (f1,f2,f3))

f1 = Fraction(1,2)
f2 = Fraction(2,4)
f3 = f1 != f2
print("The statement '%s is NOT equal to %s' is %s." % (f1,f2,f3))

f1 = Fraction(1,3)
f2 = Fraction(2,4)
f3 = f1 != f2
print("The statement '%s is NOT equal to %s' is %s." % (f1,f2,f3))

f1 = Fraction(2,6)
f2 = Fraction(1,3)
f3 = f1 > f2
print("The statement '%s is greater than %s' is %s." % (f1,f2,f3))

f1 = Fraction(1,3)
f2 = Fraction(2,4)
f3 = f1 < f2
print("The statement '%s is less than %s' is %s." % (f1,f2,f3))

f1 = Fraction(2,6)
f2 = Fraction(1,3)
f3 = f1 >= f2
print("The statement '%s is greater or equal to %s' is %s." % (f1,f2,f3))

f1 = Fraction(5,3)
f2 = Fraction(4,3)
f3 = f1 <= f2
print("The statement '%s is lesser or equal to %s' is %s." % (f1,f2,f3))


