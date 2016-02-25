try:
	start = int(raw_input("Enter number whose multiples are required: "))
	stop = int(raw_input("Enter : "))
except:
	print "Non integer value entered!"
else:
	print range(start, stop, start)[::-1]
