# Exercise 3: Using raise to create a custom error
# ------------------------------------------------
# Define a function check_age(age) that:
# - verifies if age is a positive integer
# - if not, raises ValueError("Age must be a positive integer!")
# - if valid, returns True
#
# Then, inside a try block, ask the user for an age,
# convert it to an integer, and validate it using check_age().
# Catch the ValueError and print the error message if raised using:
# except ValueError as e: print(e).

# Sample Input:
# Enter your age: 25
#
# Sample Output:
# Age accepted.
#

# Sample Input (Error):
# Enter your age: -5
#
# Sample Output:
# Error: Age must be a positive integer!

# write your code here:

def check_age(age):
    if not isinstance(age, int) or age < 0:
        raise ValueError("Age must be a positive integer!")
    return True
try:
    user_age = int(input("Enter your age: "))
    check_age(user_age)
except ValueError as e:
    print(f"Error: {e}")
else:
    print("Age accepted.")
finally:
    print("End of age check.")
