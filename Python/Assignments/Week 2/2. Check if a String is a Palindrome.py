#Problem 2: Check if a String is a Palindrome
def is_palindrome(s):
    return s == s[::-1]

# Taking input from the user
user_input = input("Enter a string to check if it is a palindrome: ")
print("Is palindrome:", is_palindrome(user_input))
