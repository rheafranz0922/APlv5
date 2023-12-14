# Get the user input for the 3 numbers 
BallA = float(input("Enter the first number:"))
BallB = float(input("Enter the second number:"))
BallC = float(input("Enter the third number:"))
# Find the largest numbers.
if BallA >= BallB and BallA >= BallC:
    largest_num = BallA
elif BallB >= BallA and BallB >= BallC:
    largest_num = BallB
else:
    largest_num = BallC
# Output of my result.
print(f"The largest number is: {largest_num}")