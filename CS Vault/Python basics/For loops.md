
a for loop is an iterative loop : this means that the loops can said thing over and over and over 

the basic syntax of a for loops is the following 

```python
for i in range(x):
	print(i)
```

a for loop sets the iterator variable to each value in a provided list

with this knowledge the output of this code would be the following:

0
1
2
3
4
5
.
.
.
x

another example of a for loop :
```python
x = [0,1,2,3,4,5,6,7,8]

sum = 0

n=len(x)

def sumFunc(n, sum):

    for i in range(n):

        sum = sum + i

        print(sum)

    return sum

print (sumFunc(n, sum))
```

in this example there are variables declared outside the function so their scope is global

my function sumFunc() takes in two parameters x and sum : x being a list and sum being an int 

in python the way to look at variables isn't data in the variables bucket. instead it's the variable points to the memory so sum points to 0 but if the line after sum = 0 there would be sum = 1 the variable sum would now point to 1 and 0 would still be in the computers memory

CODE EXPLANATION:

my iterative variable i takes on each value of my list x and the in my loop the operation sum = sum + i  gets performed and the value of sum gets updated each time until i reaches the end of the list x 

the output would be the following :
```

0
1
3
6
10
15
21
28
36
36
```

the print statement in the loop makes it print every output and the return only returns the final value
