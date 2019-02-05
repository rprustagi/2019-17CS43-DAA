#   arg1: filename containing elements (string) to be sorted
import sys

def swap(i, j, arr):
  temp = arr[i]
  arr[i] = arr[j]
  arr[j] = temp

def partition(left, right, arr):
  pivot = arr[right]
  i = left
  j = right - 1
  while (i < j):
    # find first element greater than pivot from left
    while arr[i] <= pivot and (i < right):
      i = i + 1
    if (i == right): # all elements are smaller than pivot
      return right
    # find first element smaller than pivot right
    while (arr[j] > pivot) and (j >= left):
      j = j - 1
    if (j < left): # all elements are bigger than pivot
      arr[left],arr[high] = arr[high], arr[left]
      return left
    if (i < j): #swap low and high and continue
      arr[i], arr[j] = arr[j], arr[i]
    # end while (i<j)
  arr[i], arr[high] = arr[high], arr[i]
  return i

def quicksort(left, right, arr):
  print("qsort:", left, right, arr)
  if left < right:
    s = partition(left, right, arr)
    print(arr, "partitioned at", s)
    quicksort(left, s-1, arr)
    quicksort(s+1, right, arr)
  return

# validation checks
if (len(sys.argv) != 2):
  print("Usage: ", sys.argv[0], "<file with elements>")
  exit()
datafile = sys.argv[1]
try:
  fhdata = open(datafile)
except:
  print("Data file does not exist")
  exit()

# main program
data=[0,1,2,6,4,5]
#for line in fhdata:
#  line = line.strip()
#  data.append(line)

print("input: ", data)
quicksort(0, len(data)-1, data)
print("output: ", data)

exit()

