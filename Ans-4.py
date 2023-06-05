# Write a python program to Swap two tuples in Python.
def swap_tuples(tuple1, tuple2):
    return tuple2, tuple1

# Example usage
tuple1 = ("Python", "Java")
tuple2 = ("C", "C++")
tuple1, tuple2 = swap_tuples(tuple1, tuple2)
print("Swapped Tuple 1:", tuple1)
print("Swapped Tuple 2:", tuple2)
