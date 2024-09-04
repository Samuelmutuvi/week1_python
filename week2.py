# create a list
my_list = [] 
print(my_list)

# adding elements using append
my_list.append(10)
my_list.append(20)
my_list.append(30)
my_list.append(40)
print(my_list)

# inserting an element into a specific index.
my_list [2] = 15
print(my_list)

# extend the elements in a list
list=[50,60,70]
my_list.extend(list)
print(my_list)


# remove elements in a list
my_list.remove(70)
# del my_list[-1]
print(my_list)

# sorting elements in a list
sorted_list = sorted(my_list,reverse = False)
print(sorted_list)

# Finding index for an element in alist
index_of_30 = my_list.index(30)
print(index_of_30) 