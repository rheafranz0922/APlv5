# I use a loop to itelerate the number until 1 to 100 and applied the FizzBuzz by using the rule from if-elif-else.
for num in range (1,101):
    if num % 3 == 0 and num % 5 == 0:
        print("FizzBuzz")
    elif num % 3 == 0:
        print("Fizz")
    elif num % 5 == 0:
        print("Buzz")
    else:
        print(num)