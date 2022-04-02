'''We print the combination of steps one can take to climb n stairs.'''

import copy
combinations = {
	0: [[0]],
	1: [[1]]
}

def add_num_to_dict(num):
	global combinations
	running_list = []
	for i in range(1, num+1):
		for combos in combinations[num-i]:
			for p in combos:
				running_list.append([i,p])
	combinations[num] = [running_list]

num_of_stairs = int(input("Enter the number of stair(s): "))
print("\n")

for num in range(2, num_of_stairs+1):
	add_num_to_dict(num)

for key in combinations.keys():
	print("---- Combinations for ", key, " Stair(s) are---------")
	for i in combinations[key]: 
		print(i)
		print("Total Combinations: ", len(i), "\n")
