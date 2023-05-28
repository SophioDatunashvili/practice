def _sort(lst1, lst2):
	sorted_list = []
	i, j = 0, 0
	
	while True:
		if i == len(lst1):
			sorted_list += lst2[j:]
			break
		
		if j == len(lst2):
			sorted_list += lst1[i:]
			break
		
		if lst1[i] <= lst2[j]:
			sorted_list.append(lst1[i])
			i += 1
		
		else:
			sorted_list.append(lst2[j])
			j += 1
	return sorted_list


# print(_sort([1, 3, 4, 5, 16], [2, 3, 12, 15, 16]))


def find_sum(lst: list, sum_of_two: int):
	i = 0
	j = len(lst) - 1
	while True:
		if lst[i] + lst[j] == sum_of_two:
			break
		elif lst[i] + lst[j] > sum_of_two:
			j -= 1
		else:
			i += 1
	return f"index of first num is {i} and second {j}"


print(find_sum([1, 20, 32, 46, 77, 96], sum_of_two=21))
