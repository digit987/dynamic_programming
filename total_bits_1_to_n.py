n = int(input("Input an integer: "))

if n == 0:
	print("Total count of bits is 0")
	
if n < 0:
	print("Please enter a non negative integer!")
	
numbers = {}
count = 0
indicator = 0

for i in range(1, n + 1):
	if i == 1 or (i & (i - 1)) == 0:
		numbers[i] = 1
		indicator = i
	else:
		numbers[i] = 1 + numbers[i - indicator]

for key in numbers:
	count += numbers[key]
	
print("Total count of bits from 1 to input number", n, " is: ", count)
