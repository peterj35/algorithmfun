def binarySearch(alist, item):
  first = 0
  last = len(alist)-1
  found = False

  while first<=last and not found:
    midpoint = (first + last)//2
    if alist[midpoint] == item:
      found = True
    else:
      if item < alist[midpoint]:
        last = midpoint-1
      else:
        first = midpoint+1

  return found

source = []
with open('list.txt', 'r') as f:
	for line in f:
		data = line.strip()
		source.append(int(data[0]))
testlist = [0, 1, 2, 8, 13, 17, 19, 32, 42,]
print(source)
print(binarySearch(source, 3))
print(binarySearch(source, 13))