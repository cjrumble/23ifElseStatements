# Python if Statement
# A bare Python if statement evaluates whether an expression is True or False.
# It executes the underlying code only if the result is True.

# Syntax
# if Logical_Expression:
#     Indented
#     Code
#     Block

# Example
days = int(input("How many days in a leap year? "))
if days == 366:
    print("You have cleared the test.")
print("Congrats!")

# Output
# How many days in a leap year? 366
# You have cleared the test. Congrats!

# Python if Else Statement
# A Python if else statement takes action irrespective of what the value of the expression is.
# If the result is True, then the code block following the expression would run.
# Otherwise, the code indented under the else clause would execute.
# Given below is the syntax of Python if Else statement.
# Syntax
# if Logical_Expression:
#     Indented
#     Code
#     Block
#     1
# else:
#     Indented
#     Code
#     Block
#     2

# Example
answer = input("Is Python an interpreted language? Yes or No >> ").lower()
if answer == "yes":
    print("You have cleared the test.")
else:
    print("You have failed the test.")
print("Thanks!")
# When you run the above code, it asks for your input.
# It converts the entered value it into lower case and runs the if - else condition.
# If you enter a ‘yes,’ then the output of the above code would be –
# Is Python an interpreted language? Yes or No >> yes
# You have cleared the test. Thanks! If you enter a ‘no,’ then the result of the above code would be –
# Is Python an interpreted language? Yes or No >> no
# You have failed the test. Thanks!

# Python If Else in One Line
# Python provides a way to shorten an if / else statement to one line. Let’s see how can you do this.
# The one - liner If - else has the following syntax:

# If Else in one line - Syntax
# value_on_true if condition else value_on_false
num = 2
'Even' if num % 2 == 0 else 'Odd'
# 'Even'
num = 3
'Even' if num % 2 == 0 else 'Odd'
# 'Odd'
num = 33
'Even' if num % 2 == 0 else 'Odd'
# 'Odd'
num = 34
'Even' if num % 2 == 0 else 'Odd'
# 'Even'

# Python if -Elif - Else Statement
# The first three if - else constructs can only address two outcomes, i.e., True or False.
# However, the expression next to “if ” can also evaluate to a value different from the boolean.
# It means to have more conditions, not just a single “ else ” block.

# Python supports to specify multiple conditions by using an “ elif ” clause with each of the expression.
# Syntax
# if Logical_Expression_1:
#     Indented
#     Code
#     Block
#     1
# elif Logical_Expression_2:
#     Indented
#     Code
#     Block
#     2
# elif Logical_Expression_3:
#     Indented
#     Code
#     Block
#     3
# ...
# else:
# Indented
# Code
# Block
# N

# Example
while True:
    response = input("Which Python data type is an ordered sequence? ").lower()
    print("You entered:", response)

    if response == "list":
        print("You have cleared the test.")
        break
    elif response == "tuple":
        print("You have cleared the test.")
        break
    else:
        print("Your input is wrong. Please try again.")
# This program has a while loop where it is querying about Python data types.
# It wants you to enter the name of an ordered sequence.If you provide a wrong value, then it would again prompt you for the correct input.

# Only by entering the correct value, the loop could break.
# However, you can also press the CTRL + C to exit the program.
# Had you entered a wrong answer, then the output would be:
# Which Python data type is an ordered sequence? dictionary
# You entered: dictionary
# Your input is wrong.Please try again.
# Which Python data type is an ordered sequence?
# Once you provide the correct answer, the program would end with the following output.
# Which Python data type is an ordered sequence? tuple
# You entered: tuple
# You have cleared the test.

# Nested If - Else in Python
# Python allows nesting of an if - else or if -elif - else inside another conditional clause.
# Python doesn’t limit the level of nested conditions in a program.
# Given below is the syntax of a multi - level nested if - elif - else statement.

# Syntax
# if Logical_Expression_1:
#     if Logical_Expression_1.1:
#         if Logical_Expression_1.1.1:
#             Indented
#             Code
#             Block
#             1.1
#             .1
#         else
#             Indented
#             Code
#             Block
#     elif Logical_Expression_1.2:
#         Indented
#         Code
#         Block
#         1.2
#     else:
#         Indented
#         Code
#         Block
# elif Logical_Expression_2:
#     Indented
#     Code
#     Block
#     2
# elif Logical_Expression_3:
#     Indented
#     Code
#     Block
#     3
# ...
# else:
# Indented
# Code
# Block

# Nested Condition Statement
# The above diagram represents the following code flow.
x = 10
y = 20
z = 30
print("Start")
if x == 10:
    print(" Nested If")
    if y == 20:
        print(" End of Nested If Block ")
    else:
        print(" End of Nested If-Else Block ")
elif y == 20:
    print(" Elif block ")
else:
    print(" Nested If")
    if z == 30:
        print(" End of Nested If Block ")
    else:
        print(" End of Nested If-Else Block ")
print("Stop")

# Example
while True:
    response = int(input("How many days are there in a leap year? "))
    print("You entered:", response)

    if response == 366:
        print("You have cleared the first level.")
        response = input("What month has an extra day in leap year?? ").lower()
        if response == "february":
            print("You have cleared the test.")
            break
        else:
            print("You have failed the test.")
            break
    else:
        print("Your input is wrong, please try again.")
# use of nested if in Python.It first asks a question from the user.
# After that, there is an if statement to check whether the answer is correct or not.
# In case the user provides the right input, then he faces another question.
# Now, the nested IF comes into the picture checking the latest response from the user.
# Using Not Operator with Python If Else
# The ‘not’ is a negation logical operator in Python.
# It reverses the result ofits operand and converts to a boolean outcome, i.e., True or False.
# The operand could be a variable or an expression evaluating to a numeric type.
# Example - 1
a = 10
b = 20
if not a > b:
    print("The number %d is less than %d" % (a, b))
# The number 10 is less than 20
# Example - 2
X = 0
if not X:
    print("X is not %d" % (X))
else:
    print("X is %d" % (X))
# X is not 0

# Using And Operator with If Else
# By using the ‘ and ’ operator, you can join multiple expression in a Python if condition.
# It is also a logical operator which evaluates as True if both / all the operands(x and y and z) are True.

# Using And Operator in Python Conditions Using And Operator in Python Conditions Example
a = 10
b = 20
c = 30
avg = (a + b + c) / 3
print("avg =", avg)
if avg > a and avg > b and avg > c:
    print("%d is higher than %d, %d, %d" % (avg, a, b, c))
elif avg > a and avg > b:
    print("%d is higher than %d, %d" % (avg, a, b))
elif avg > a and avg > c:
    print("%d is higher than %d, %d" % (avg, a, c))
elif avg > b and avg > c:
    print("%d is higher than %d, %d" % (avg, b, c))
elif avg > a:
    print("%d is just higher than %d" % (avg, a))
elif avg > b:
    print("%d is just higher than %d" % (avg, b))
elif avg > c:
    print("%d is just higher than %d" % (avg, c))
# output
# avg = 20.0
# 20 is just higher than 10

# Using In Operator with If Else
# Python “ in ” operator allows comparing a variable against multiple values in a single line.
# It makes decision making more comfortable by reducing the use of many if - elif statements.
# In Python, we often refer to it as the membership operator. It can let you check value from objects of different types.
# They could be a list, tuple, string, dictionary types.

# Examples
# After that, there is a for loop which is traversing it and prints values.

# The loop has an if statement which prints specific numbers from the list
# which are not in the tuple used in the condition.
# Hence, we’ve also used the “not” along with the “ in ” operator.

# Example of "in" operator with Python If statement
num_list = [1, 10, 2, 20, 3, 30]
for num in num_list:
    if not num in (2, 3):
        print("Allowed Item:", num)
# The output of the above code is as follows.
# Allowed
# Item: 1
# Allowed
# Item: 10
# Allowed
# Item: 20
# Allowed
# Item: 30

# It has two teams of players(team1 and team2) for two games.In here, we’ve to find who from the “team1” also plays for the “team2”.
# Find players who play both games
team1 = ["Jake", "Allan", "Nick", "Alex", "Dave"]
team2 = ["David", "John", "Chris", "Alex", "Nick"]
for aplayer in team1:
    if aplayer in team2:
        print("%s also plays for team2." % (aplayer))
# output
# Nick also plays for team2.
# Alex also plays for team2.

# Summary

# Yes, the software programs can make decisions at runtime. But their correctness depends on how effectively have you added the conditions.
# In this tutorial, we covered Python If Else, If - Elif - Else and a couple of its variations using various Python operators.
