import numpy as np
#Arrays
a = np.array([20, 32, 82, 40, 32, 15, 67, 52])
#Find the indices of an even numbers
evennum_indices = np.where(a % 2 == 0)
#The result of an indices of a even number.
print("Result of indices even number:", evennum_indices)

#The sort of array.
sorted_array = np.sort(a)
#The result.
print("result of sorted array:", sorted_array)

# Slice elements from index 3 to the end of the array/Slice element from index 0 to index 4.
slice_1 = a[3:]
print("result of Slice from index 3:", slice_1)

slice_2 = a[:5]
print("result Slice element from index 0 to index 4:", slice_2)
#Print the 32,15,67 by using hte negative slicing.
negative_slice = a[-5:-2]
print("Print the negative slicing of 32, 15, 67:", negative_slice)# The result