# to multiply the all values by using transversal.
def multiplylist(list):
    result = 1
    for x in list:
        result = result * x
    return result
#code
list1 = [22, 1, 5]
list2 = [2, 33, 4]
print(multiplylist(list1))