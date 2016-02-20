inputArr = [8,5,78,66,12,35,41,6,96,7]

def insertionSort(arr):
	for i in range(len(arr)):
		j = i
		while j>0 and arr[j] < arr[j-1]:
			temp = arr[j-1]
			arr[j-1] = arr[j]
			arr[j] = temp
			j -= 1
	print arr

insertionSort(inputArr)