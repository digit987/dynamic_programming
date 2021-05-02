'''We print the unique combinations n number of parentheses can have.
For example,
Input: 1
Output: ()
Input: 2
Output: ()(), (())
Input: 3
Output: ((())), ()()(), (())(), (()()), ()(())
'''

'''We initialize the dictionary with base case 1'''

parentheses_combinations = {
	1: ['()']
}

def add_parentheses_combination_to_dict(parentheses):
	global parentheses_combinations
	new_combination_list = []
	previous_parentheses_combination = parentheses_combinations[parentheses-1]
	for combination in previous_parentheses_combination:
		new_combination_list.append('()' + combination)
		for char_position_in_combination in range(len(combination)):
			if char_position_in_combination == len(combination) - 1:
				new_combination_list.append(combination + '()')
			else:
				new_combination_list.append(combination[0:char_position_in_combination+1] + '()' + combination[char_position_in_combination+1:len(combination)])
			new_combination_list = list(set(new_combination_list))
	parentheses_combinations[parentheses] = new_combination_list

num_of_parentheses = int(input("Enter the number of parentheses: "))
if num_of_parentheses <= 0:
	print("Please Enter a natural number")
	exit()
print("\n")

for parentheses in range(2, num_of_parentheses+1):
	add_parentheses_combination_to_dict(parentheses)

catalan_number = 0

for key in parentheses_combinations.keys():
	print("---- Combinations for Parentheses", key, " are---------")
	for combination in parentheses_combinations[key]: 
		print(combination)
	print("Total Combinations: ", len(parentheses_combinations[key]), "\n")
	if key == num_of_parentheses:
		catalan_number = len(parentheses_combinations[key])
		
print("Catalan number for ",  num_of_parentheses, " is: ", catalan_number)
