'''We print the unique combinations n number of parantheses can have.
For example,
Input: 1
Output: ()
Input: 2
Output: ()(), (())
Input: 3
Output: ((())), ()()(), (())(), (()()), ()(())
'''

'''We initialize the dictionary with base case 1'''

parantheses_combinations = {
	1: ['()']
}

def add_parantheses_combination_to_dict(parantheses):
	global parantheses_combinations
	new_combination_list = []
	previous_parantheses_combination = parantheses_combinations[parantheses-1]
	for combination in previous_parantheses_combination:
		new_combination_list.append('()' + combination)
		for char_position_in_combination in range(len(combination)):
			if char_position_in_combination == len(combination) - 1:
				new_combination_list.append(combination + '()')
			else:
				new_combination_list.append(combination[0:char_position_in_combination+1] + '()' + combination[char_position_in_combination+1:len(combination)])
			new_combination_list = list(set(new_combination_list))
	parantheses_combinations[parantheses] = new_combination_list

num_of_parantheses = int(input("Enter the number of parantheses: "))
if num_of_parantheses <= 0:
	print("Please Enter a natural number")
	exit()
print("\n")

for parantheses in range(2, num_of_parantheses+1):
	add_parantheses_combination_to_dict(parantheses)

catalan_number = 0

for key in parantheses_combinations.keys():
	print("---- Combinations for Parantheses", key, " are---------")
	for combination in parantheses_combinations[key]: 
		print(combination)
	print("Total Combinations: ", len(parantheses_combinations[key]), "\n")
	if key == num_of_parantheses:
		catalan_number = len(parantheses_combinations[key])
		
print("Catalan number for ",  num_of_parantheses, " is: ", catalan_number)
