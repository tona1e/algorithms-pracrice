list_to_sort = [16,7,23,8,19,10,25,31,1,5]

def sortBySwapping(list_to_sort):
    for i in range(len(list_to_sort)):
        for j in range(len(list_to_sort)):
            if i<j and list_to_sort[i] > list_to_sort[j]:
                list_to_sort[i] , list_to_sort[j] = list_to_sort[j] , list_to_sort[i]

    return list_to_sort

print(sortBySwapping(list_to_sort))
#sorting a list in python by swapping according to smallest number