# use input to put a number by a sum like 1234.
num = int(input("Enter a number"))
sum = 0
# Put the digit by str.
for digit in str(num):
    sum=sum+int(digit)
#Let see the result.
print(f"The sum of digits", sum)