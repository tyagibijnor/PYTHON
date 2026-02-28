## Datastructure in python
# List
my_list = [1, 2, 3, 4, 5]
# Tuple
my_tuple = (1, 2, 3, 4, 5,5)
# Set
my_set = {1, 2, 3, 4, 5, 5}
# Dictionary
my_dict = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}
# String
my_string = "Hello, World!"

print ("List:", my_list)
print ("Tuple:", my_tuple)
print ("Set:", my_set)
print ("Dictionary:", my_dict)
print ("String:", my_string)
print("Split List:",my_list[0:2])
print("Split List:",my_list[:3])
print("Split List:",my_list[-2])
print("Main List:",my_list)
my_list[2]=15
print("Updated List:",my_list)
## List are mutable, we can change the value of list but tuple are immutable we can't change the value of tuple
# my_tuple[2]=15 # This will raise an error because tuple is immutable 
