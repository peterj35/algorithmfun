import sys
import random

def main():
  if len(sys.argv) != 2:
    print('Please put in 1 argument, the number of random numbers you want.')

  print('Generating', str(sys.argv[1]), 'numbers between 1 and 1000')

  myarray = []
  for i in range(int(sys.argv[1])):
    myarray.append(random.randint(0,1000))

  with open(sys.argv[1]+'.txt', 'w+', encoding='utf-8') as output:
    for item in myarray:
      output.write("%s\n" % item)

def generate(size):
  myarray = []
  for i in range(size):
    myarray.append(random.randint(0,1000))
  return myarray

if __name__ == '__main__':
  main()
