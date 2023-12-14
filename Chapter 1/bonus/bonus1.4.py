#The list.
staff = ["Arshiya", "Usman", "Iftikhar", "Usman","Rafia", "Mary", "Anmol","Zainab","Iftikhar", "Arshiya","Rafia","Jake"]
#I use dictionary from list to count the occurence.
occurence_dict = {}
for item in staff:
    if item in staff:
        #if the item is not on the list add a count by 1.
        if item not in occurence_dict:
            occurence_dict[item] = 1
        else:
            # if the item is already in the dictionary, it will count.
            occurence_dict[item] += 1
#The result.
for item, count in occurence_dict.items():
    print(f"{item}: {count} times")