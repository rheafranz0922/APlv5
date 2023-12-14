#Here is the list of i am using the turples.
marks = [("CodeLab I",67),("web Development", 75),("CodeLabII",74),("Smartphone Apps",68),("Games Development",70),("Responsive web",65)]
#Sort the list based on the marks (low to high).
sorted_low_to_high = sorted(marks, key=lambda x: x[1])
#Sort the list on the marks(high to low).
sorted_high_to_low = sorted(marks, key=lambda x: x[1], reverse=True)
#The result.
print("Sorted by a marks (low to high):", sorted_low_to_high)
print("Sorted by a marks (high to low):", sorted_high_to_low)