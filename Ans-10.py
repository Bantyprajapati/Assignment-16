# Write a python program to change the first item (22) of a list within the following tuple to 222.tuple1 = (11, [22, 33], 44, 55)
tuple1 = (11, [22, 33], 44, 55)

tuple_list = list(tuple1)  # Convert the tuple to a list
tuple_list[1][0] = 222  # Modify the first item of the list
modified_tuple = tuple(tuple_list)  # Convert the list back to a tuple

print("Modified Tuple:", modified_tuple)
