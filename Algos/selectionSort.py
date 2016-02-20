inputArr = [85,45,21,96,14,33,0,3,78,25,62]

def selectionSort(inputArr):
	for i in range(len(inputArr)):
		minIndx = i
		for j in range(i+1, len(inputArr)):
			if(inputArr[j] < inputArr[minIndx]):
				minIndx = j
				#print inputArr[minIndx]
		temp = inputArr[minIndx]
		inputArr[minIndx] = inputArr[i]
		inputArr[i] = temp
		print inputArr
	print inputArr

selectionSort(inputArr)
