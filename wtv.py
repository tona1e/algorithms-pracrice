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

        for i in range(1,len(list10)) :
            if list10[i] < middle:
                left.append(list10[i])
            else: 
                right.append(list10[i])
        left.append(middle)
        return left + right

quickSorted = quickSort(list10)
print(quickSorted)

def bubbleSort(list10):
    n = len(list10)
    for i in range(n):
        swap = False 

        for j in range(0,n-i-1):
            if list10[j] > list10[j+1]:
                list10[j] , list10[j+1] = list10[j+1] , list10[j]
                swap = True

        if not swap:
            break

bubbleSort(list10)
print(list10)




def recursion(n):
    if n == 1:
        return 1
    elif n == 2:
        return 2
    elif n > 2:
        return recursion(n-1) + recursion(n-2)
    
for n in range(1,8):
    print(n , "" , recursion(n))
