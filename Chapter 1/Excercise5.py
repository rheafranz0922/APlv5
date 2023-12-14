# Initialize the counter of a number of a loop.
loop_count = 0
# Start a loop
while True:
    # Ask the user if you want to continue.
    user_input = input("Do you want to continue? (Yes/No):")
    # Increment the loop to count until the end.
    loop_count += 1
    # check if the userwant to continue the loop or not.
    if user_input.upper() != 'Y':
        break # Exit my loop if the user stop.
# Output of my number times of the loop
print(f"The while loop was executed (loop_count)times.")