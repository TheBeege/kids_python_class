# this is a comment
# use this to take notes
# this is function definition
def print_fancy():
    print("i'm super fancy!")


# this is a function call
# a function call tells Python to
# run the tasks in the task list
print_fancy()

# input is a parameter
def print_crazy(input):
    print('CRAZY', input)


print_crazy('class')


def print_parameters(param1, param2):
    print(param1, param2)


print_parameters('minecraft', 'is fun')
print_parameters('geometry dash', 'is amazing')

print_parameters(param2='is fun',
                param1='backwards')

def print_with_default(input, input2=' - right?'):
    print('with_default:', input, input2)

print_with_default('we can do this')
print_with_default('we can do this', '- guaranteed')

def add(a, b):
    return a + b

output = add(10, 5)
print(output)
