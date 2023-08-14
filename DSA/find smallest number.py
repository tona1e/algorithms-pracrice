def getSmallestNumber(list_to_sort: list) -> int:
    smallest_number: int = list_to_sort[0]
    for num in list_to_sort :
        if num < smallest_number :
            smallest_number = num
    return smallest_number


list_to_sort: list = [90, 20, 30, 70, 45, 65, 10, 1120]
list_to_fill = []
print(getSmallestNumber(list_to_sort))
x = len(list_to_sort)
def orderList(list_to_sort) :
    for i in range(x) :
        swap = False
        
        for j in range(0, x-i-1) :
            if list_to_sort[j] > list_to_sort[j+1]:

                list_to_sort[j], list_to_sort[j+1] = list_to_sort[j+1], list_to_sort[j]
                swap = True

        if not swap:
            break

orderList(list_to_sort)
print(list_to_sort)
def quickSort(list_to_sort) :
    if len(list_to_sort) <= 1 :
        return list_to_sort
    else:
        middle = list_to_sort[0]
        left = []
        right = []
        for i in range(1,len(list_to_sort)):
            if list_to_sort[i] < middle :
                left.append(list_to_sort[i])
            else:
                right.append(list_to_sort[i])
                return
            

quickSortedList = quickSort(list_to_sort)
print(quickSort)
#def generateOrderedlist(list_to_sort, list_to_fill) :
 #   for i in range (list_to_sort):
        