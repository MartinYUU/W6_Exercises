# For each of the following exceptions, create a short code block that raises that 
# exception. Then put it within a try-except block to handle the error, an else block to 
# print the result if no error occurs, and a finally statement like “Let’s try another one”: 
# ValueError 
# NameError 
# TypeError 
# SyntaxError 
# You may need to do a little research to come up with ideas for how to generate each 
# exception. You will also likely notice that for most exceptions, there’s a range of 
# different specific error that might raise that exception. If you find two different ways of 
# producing an exception, keep both in your script for reference.


try:
    num = int('hello')
except ValueError:
    print('Error: Cannot cast non numeric strings to integers')
else:
    print('No error')
finally:
    print("Let's try another one.")

try:
    # Raise NameError by using an undefined variable
    print(var1)
except NameError:
    print('Error: Undefined variale')
else:
    print("No error")
finally:
    print("Let's try another one.")

try:
    # Raise TypeError by trying to add an integer and a string
    result = 1 + 'hi'
except TypeError:
    print('Error: Cannot add integers and strings')
else:
    print('No error')
finally:
    print("Let's try another one.")

try:
    eval('print(hi')
except SyntaxError:
    print('Error Check your syntax')
else:
    print('No error')
finally:
    print("Let's try another one.")
