list10 = [99,100,101,988889,6,88,54]
def findSmallest(list10):
    var1 = list10[0]
    for num in list10 :
        if num < var1 :
            var1 = num
    return var1
print(findSmallest(list10))

def quickSort(list10):
    n = len(list10)
    if n <= 1 :
        return list10
    else:
        middle = list10[0]
        left = []
        right = []

        for i in range(1,n) :
            if list10[i] < middle:
                left.append(list10[i])
            else: 
                right.append(list10[i])
        left.append(middle)
        return left + right

quickSorted = quickSort(list10)
print(quickSorted)