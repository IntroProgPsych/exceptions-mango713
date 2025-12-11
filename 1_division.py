# Exercise 1: Safe division with try / except / else / finally
# ------------------------------------------------------------
# Ask the user for two numbers and attempt to divide them.
# If the user enters invalid values or tries division by zero,
# display an error message.
# If division succeeds, print the result inside the else block.
# The finally block should always print: "Operation finished."

# Sample Input:
# Enter the numerator: 12
# Enter the denominator: 3
#
# Sample Output:
# Division successful! Result: 4.0
# Operation finished.
#


# Sample Input (Error):
# Enter the numerator: 10
# Enter the denominator: zero
#
# Sample Output:
# Error: You must enter numeric values.
# Operation finished.

# write your code here:

numerator_input = input("Enter the numerator: ")
denominator_input = input("Enter the denominator: ")

try:
    numerator = int(numerator_input)
    denominator =int(denominator_input)
    result = numerator / denominator
except ValueError:
    print("Error: Enter numeric values.")
except ZeroDivisionError:
    print("Error: Division by zero not allowed.")
else:
    print(f"Division successful! Result: {result}")
finally:
    print("Operation finished.")