list1 = [99,88,66,55,33,22,65,100]
def findSmallest(list1):
    smallest_number = list1[0]
    for i in list1 :
        if i < smallest_number:
            smallest_number = i
    return smallest_number
print(findSmallest(list1))