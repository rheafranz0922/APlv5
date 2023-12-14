# Get the user input for integer.
ColumnA = int(input("Enter first integer:"))
ColumnB = int(input("Enter second integer:"))
# The calculation of Sum (+) | Diff (-) | Product (x).
sum_result = ColumnA + ColumnB
diff_result = ColumnA - ColumnB
product_result = ColumnA * ColumnB
# The calculation of a quotient and remainder  from zero before performing the division.
if ColumnB != 0:
    quotient_result = ColumnA / ColumnB
    remainder_result = ColumnA % ColumnB
else:
    quotient_result = "Undefined (division by zero)"
    remainder_result = "Undefined (division by zero)"
# My output result.
print(f"Sum: {sum_result}")
print(f"Diff: {diff_result}")
print(f"Product: {product_result}")
print(f"Quotient: {quotient_result}")
print(f"Remainder: {remainder_result}")