# Create an int list with 10 numbers of a value.
int_list = [10,2,9,7,5,8,3,4,1]

# My output to use my loop is.
print("My original list")
for element in int_list:
    print(element, end="")
print("\n")

# Highest to the lowest value of integer numbers.
print("Highest value:", max(int_list))
print("Lowest value:", min(int_list))

# Sort the elements in ascending order.
int_list.sort()
print("\nSorted in ascending order:")
for element in int_list:
    print(element, end=" ")
print("\n")
#Sort the element in descending order.
int_list.sort(reverse = True)
print("\nSorted in descending order:")
for element in int_list:
    print(element, end=" ")
print("\n")

# Append the two elements
int_list.append(11)
int_list.append(0)

# Print the list after appending
print("\nList after appending two element:")
for element in int_list:
    print(element, end=" ")
print("\n")