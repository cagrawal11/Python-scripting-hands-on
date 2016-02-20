inputArr = [4,2,55,3,6,7,81,12,13,65,20,21,95,19]

def quickSort(inputArr, lower, upper):
	if(lower < upper):
		splitIndex = partition(inputArr, lower, upper)
		quickSort(inputArr, lower, splitIndex-1)
		quickSort(inputArr, splitIndex+1, upper)


def partition(inputArr, lower, upper):
	pivot = inputArr[lower]
	i = lower+1
	j = upper
	done = False
	while not done:
		while i<=j and inputArr[i] <= pivot:
	 		i += 1
	 	while  j >= i and inputArr[j] >= pivot:
	 		j -= 1
	 	if i > j:
	 		done = True
	 	else:
	 		temp = inputArr[i]
	 		inputArr[i] = inputArr[j]
	 		inputArr[j] = temp
	temp = pivot
	inputArr[lower] = inputArr[j]
	inputArr[j] = temp
	return j

quickSort(inputArr, 0, len(inputArr)-1)
print inputArr
