The break statement in python is used to break a loop immediately.

It should be seen as a red **"stop sign"** that can be used in code to have more control over the behavior of the loop.

According to the [Python Documentation](https://docs.python.org/3/tutorial/controlflow.html?highlight=break#break-and-continue-statements-and-else-clauses-on-loops):

> The [`break`](https://docs.python.org/3/reference/simple_stmts.html#break) statement, like in C, breaks out of the innermost enclosing [`for`](https://docs.python.org/3/reference/compound_stmts.html#for) or [`while`](https://docs.python.org/3/reference/compound_stmts.html#while) loop.


Here is the basic logic behind the break statement

- the while loop starts only if the condition is evaluated to True
- if a break statement is found at any point during the execution of the loop, the loop is stopped immediately
- Else, if the break statement is not found the loop continues it's normal execution and it stops when the condition of the while loop evaluates to false 

we can use the break statement to stop a while loop when a condition is met at a particular point in it's execution.

so it will typically be found in a conditional statement like this one

```python
while True:
    # Code
    if <condition>:
    	break
    # Code
```

this stops the loop immediately if the condition is True


here is an example of a break statement in a while True loop :

```python
while True:
	user_input = int(input("Enter an integer: "))
	if user_input % 2 != 0:
		print("this is an odd number")
		break
	print("this is an even number")
```

- line 1 defines a while True loop that will run indefinitely in not for ctrl + c or break statement is found
- line 2 asks for the users input and it is then converted to an integer 
- the third line checks if the input is odd
- if it is it will print out "this is an odd number"
- else if the input is even the loop will run indefinitely until an odd integer is entered because that is the only way the break statement can ever be found


***here is an example with custom user input*

```python
Enter an integer: 4
This number is even
Enter an integer: 6
This number is even
Enter an integer: 8
This number is even
Enter an integer: 3
This number is odd
>>> 
```

