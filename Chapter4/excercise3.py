# I make a number in to a
def read_numbers(data_path):
    try:
        with open(data_path, 'r') as file:
            num = [int(line.strip()) for line in file]
        return num
    except FileNotFoundError:
        print(f"Error: File '{data_path}' not found.")
        return []

# File path for the numbers.txt file
data_path = 'numbers.txt'

# Read numbers from the file
numbers_list = read_numbers(data_path)

# Output the values in integer format
for number in numbers_list:
    print(number)
