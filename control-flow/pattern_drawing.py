size = int(input("Enter the size of the pattern:"))

if size <= 0:
	print("Enter a positive integer")
else:
	rows = 0
	while rows < size:
		for row in range(size):
			print("*", end="")
		print()	
		rows += 1		
