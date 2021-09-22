def find_index(lst_temp,x):
	lst_temp.sort()
	l = len(lst_temp) - 1
	if x > lst_temp[l]:
		return l + 1
	else:
		for i in range(0,l):
			i = i + 1
			if x <= lst_temp[i -1]:
				return i-1
			else:
				pass	        
lst_new = [2,4,5,6,1]
a = find_index(lst_new,3)
print(a)
