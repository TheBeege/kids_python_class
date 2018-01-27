# More Functions and Intro to Conditions

## Functions Review
### Function Definitions
First, let's look at a _function definition_. This is defining the task list for Python to follow later.
```python
def add(a, b):
    return a + b
```

Let's break this down.

`def` is a keyword that tells Python that we're defining a new function.

`add` is the function's name. This could be any text. Ideally, it should be something that describes what the function does.

`a` and `b` are called parameters or inputs. These are variables whose values are set whenever this function (or task list) is told to run. Each parameter should be separated by a comma.

After this, notice the indentation. **This is important!** The indentation tells Python that this code is part of the function. When you remove the indentation, it's considered part of the rest of the program. You must indent after `def` for every line that you want to be part of the task list.

`return` is a keyword that ends the function. Anything on the `return` line is treated as output. The output as a function takes the place of wherever the _function call_ is. What's a _function call_?

### Function Calls
A _function call_ is whenever you tell Python to run the tasks in the task list. What does a function call look like?
```python
add(1, 2)
```
This is a _function call_. It's the name of a function, followed by parenthesis containing the parameters separated by commas. Whenever Python sees this, it will go to the _function definition_ and run its steps.

When it goes to the _function definition_, it assigns the _function call_ parameters to the _function definition_ parameters. In this case, it would be `a = 1` and `b = 2`. This happens in order. Since `a` is the first parameter in the _function definition_ and `1` is the first parameter in the _function call_, `a` is assigned to `1`. The same happens with `b` and `2` since they're in the second position.


#### Below here is notes that need to be converted
Next, it executes all of the steps in our
function definition. In this case: return a + b
Since a has been assigned to 1 and b has been
assigned to 2, it becomes:
return 1 + 2
or more simply:
return 3
Remember that return produces function output.
Once a function hits return, it ends.
Anything after return on the same line is output
Output means that the output value takes the place
of the function call.
So back at our function call print(add(1,2)), it
becomes print(3)
Since the add function definition returned 3,
add(1,2) is replaced with 3
