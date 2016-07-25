import random

def main():
	mylist = generateArray(200)
	print(mylist)
	insertionSort(mylist)
	print(mylist)

def 

def insertionSort(mylist):
	for i in range(1, len(mylist)):

		currentvalue = mylist[i]
		position = i

		while position>0 and mylist[position-1]>currentvalue:
			mylist[position] = mylist[position-1]
			position = position-1

		mylist[position]=currentvalue

def generateArray(size):
  myarray = []
  for i in range(size):
    myarray.append(random.randint(0,1000))
  return myarray

if __name__ == '__main__':
  main()
