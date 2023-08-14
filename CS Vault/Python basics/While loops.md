
the while loop can be slightly more intuitive in python

it is used to repeat a sequence of statements an unknown number of times, this type of loop runs while a given condition is **True** and it only stops when the condition becomes **False**

so if the False condition is never met the loop will run indefinitely

some real use cases for while loops:

**User Input**: you can not know how many entries a user will input that are invalid until they input a valid one

**Search:** searching for an element in a data structure since we can't know in advance how many iterations will be needed to find the target value. For example, the Binary Search algorithm can be implemented using a while loop.

the general syntax is as follows:

```python
while <condition>:
	# Code
```

here's how a basic for loop works


```python
i = 4

while i < 8:
    print(i)
    i += 1
```

this is the output for this code :

```
4
5
6
7
```

there is also **while True**

```python
while True:
	#code
```

it is possible generate an infinite loop intentionally using while true

in this case the process will run indefinitely until the process is stopped by external intervention or by a **break** statement

