'''
This code takes a list of numbers and attempts to return a combined single largest possible number.
For example, [42, 24, 23, 3] should return 4232423 i.e., 42-3-24-23
'''

class Sort:
	
	def __init__(self):
		self.numbers = [23, 234, 3, 231, 56]
		self.sorted = []
		self.p = []
	
	def sort(self):
		for i in range(len(self.numbers)):
			self.sorted.append(self.numbers[i])
			self.sorted = self.compare(self.sorted)
			print(self.sorted)
		return self.list_to_number(self.sorted)
			
	def list_to_number(self, list):
		return int(''.join(str(num) for num in list))
			
	def compare(self, current_list):
		largest_number_combination = {}
		new_number_appended = current_list[-1]
		current_list = current_list[0:-1]
		running_list = [new_number_appended] + current_list
		largest_number_combination[self.list_to_number(running_list)] = running_list
		for i in range(len(current_list)):
			running_list = self.list_to_number(current_list[0:i+1]) + self.list_to_number([new_number_appended]) + self.list_to_number(current_list[i+1:])
			largest_number_combination[self.list_to_number(running_list)] = running_list
		
		return largest_number_combination[max(largest_number_combination.keys())]
			

s = Sort()
print(s.sort())
