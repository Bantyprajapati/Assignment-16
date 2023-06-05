# Write a python program to reverse the tuple.
def reverse_tuple(input_tuple):
    reversed_tuple = input_tuple[::-1]
    return reversed_tuple

# Example usage
my_tuple = ("Java", "Python", "SQL", "C")
reversed_tuple = reverse_tuple(my_tuple)
print("Reversed Tuple:", reversed_tuple)
