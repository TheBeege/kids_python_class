def add(a, b):
    return a + b


print(add(1,2)) # This outputs 3
# First, Python sees "add(", so it looks for
# a function definition called add. This is
# called a "function call". Python then finds our
# "def add(..." up above.
# Next, it checks what's inside the parenthesis:
# in this case, 1 and 2. Remember that these
# are called parameters.
# Next, it looks at the function definition for add
# It sees two parameters: a and b
# It assigns the a to 1 and b to 2.
# Parameters are assigned by their position (mostly)
# Next, it executes all of the steps in our
# function definition. In this case: return a + b
# Since a has been assigned to 1 and b has been
# assigned to 2, it becomes:
# return 1 + 2
# or more simply:
# return 3
# Remember that return produces function output.
# Once a function hits return, it ends.
# Anything after return on the same line is output
# Output means that the output value takes the place
# of the function call.
# So back at our function call print(add(1,2)), it
# becomes print(3)
# Since the add function definition returned 3,
# add(1,2) is replaced with 3
