# A user to input the time duration in seconds and covert by a float.
time = float(input("input time in seconds:"))
# Calculate the number of the days by a give a time duration.
day = time // (24 * 3600) # and update the variable tp hold the remaining seconds of a time.
time = time % (24 * 3600)

#Calculate the full hours number by the remaining time.
hour = time // 3600 #Update the time variable to hold the remaing second time after to subtract the time.
time %= 3600

#And calculate the number of full minutes.
minutes = time // 60
time %= 60

#The time variable is now represent the seconds.
seconds = time
#Print the time duration in a format.
print("d:h:m:s-> %d:%d:%d:%d" % (day, hour, minutes, seconds))