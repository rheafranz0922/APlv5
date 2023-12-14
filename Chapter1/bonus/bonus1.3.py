#Print the asterisk pattern.
def print_asterisk_pattern(rows):
    for i in range(1, rows + 1):
        for j in range(rows - i):
            print(" ", end="")
        for k in range(2 * i - 1):
            print(" ", end="")
        #Move to the nextline
        print()
# Set the number of a row pattern
num_rows = 5 #You can change and adjust the value.
#Print the pattern.
print_asterisk_pattern(num_rows)