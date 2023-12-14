# Create a turple with values
year = (2017, 2003, 2011, 2005, 1987, 2009, 2020, 2018, 2009)
#Access the value at index -3.
value_at_index_minus_3 = year[-3]
print("value at index -3:", value_at_index_minus_3)

#Reverse the tuple and print the original tuple and reversed tuple.
reversed_year = tuple(reversed(year))
print("\nOriginal Tuple:", year)
print("Reversed Tuple:", reversed_year)

#Count number of times 2009 is in the tuple.
count_2009 = year.count(2009)
print("\nNumber of times 2009 appears in the turple:", count_2009)
# Get the index value of 2018 using the index method
index_of_2018 = year.count(2018)
print("\n Index of 2018:", index_of_2018)
# Find the length of the given tuple using the len() method
tuple_length = len(year)
print("\n length of the tuple:", tuple_length)