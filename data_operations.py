##list operations 
my_list = [3, 11, 1, 2, 3, 50, 5]
## append
print("List :", my_list)
my_list.append(4) # This will add the value 4 to the end of the list
print("List after append:", my_list)

## insert
my_list.insert(1, 10) # This will insert the value 10 at index 1 in the list
print("List after insert:", my_list)

## remove
my_list.remove(2) # This will remove the first occurrence of the value 2 from the list
print("List after remove:", my_list)

## index
index_of_3 = my_list.index(3) # This will return the index of the first occurrence of the value 3 in the list
print("Index of 3:", index_of_3)

## count
count_of_3 = my_list.count(3) # This will return the number of occurrences of the value 3 in the list
print("Count of 3:", count_of_3)

## size
size_of_list = len(my_list) # This will return the number of elements in the list
print("Size of list:", size_of_list) 

# sort
my_list.sort() # This will sort the list in ascending order
print("List after sort:", my_list)

## reverse
my_list.reverse() # This will reverse the order of the elements in the list
print("List after reverse:", my_list)

## pop
popped_value = my_list.pop() # This will remove and return the last element of the  list
print("Popped value:", popped_value)

popped_value_at_index_2 = my_list.pop(2) # This will remove and return the element at index 2 in the list
print("Popped value at index 2:", popped_value_at_index_2) 
print("List after pop:", my_list)

## clear
my_list.clear() # This will remove all the elements from the list
print("List after clear:", my_list) 

## insert
my_list.insert(0, 1) # This will insert the value 1 at index 0 in the list
my_list.insert(1, 2) # This will insert the value 2 at index 1 in the list
my_list.insert(2, 3) # This will insert the value 3 at index 2 in the list
my_list.insert(3, 4) # This will insert the value 4 at index    3 in the list
my_list.insert(4, 5) # This will insert the value 5 at index 4 in the list
print("List after inserting values:", my_list)

## enumerate
for index, value in enumerate(my_list): # This will iterate over the list and return both the index and the value of each element in the list
    print("Index:", index, "Value:", value) 

