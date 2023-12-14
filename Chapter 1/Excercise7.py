# In my program the num % 2 != 0 to check the current number from odd. the statement of an odd will be excuted and skip the odd number.
for num in range(1,101):
    if num % 2 != 0:
        continue
    print(num)