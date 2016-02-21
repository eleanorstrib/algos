### various sorting algorithms done in scratch for practice

my_list = [8, 2, 7, 0, 15, 27, -2]

def bubble(my_list):
	## PROBLEM STATEMENT
	# we want to move through each item in the list
	# compare it to its neighbor to the right
	# if the item is greater than it's neighbor, switch them
	# do this n-1 times where n is the length of the list to be sorted

	# set counter for number of times
	passes = 0

	while passes < len(my_list):
		for x in range(0, len(my_list) - 1):
			if my_list[x] > my_list[x + 1]:
				temp = my_list[x]
				my_list[x] = my_list[x + 1]
				my_list[x + 1] = temp

		passes = passes + 1
	return my_list


print(bubble(my_list))