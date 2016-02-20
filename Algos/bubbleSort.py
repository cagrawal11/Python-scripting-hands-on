inputArr = [12,59,03,14,16,89,1,2,78]

def bubbleSort(inputArr):
	for i in range(len(inputArr)):
		for j in range(0, len(inputArr)-i-1):
			if(inputArr[j] > inputArr[j+1]):
				temp = inputArr[j]
				inputArr[j] = inputArr[j+1]
				inputArr[j+1] = temp
	print inputArr

bubbleSort(inputArr)