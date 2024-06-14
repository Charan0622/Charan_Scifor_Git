#Problem 4: Remove Duplicates from a String
def remove_duplicates(s):
    result = []
    seen = set()
    for char in s:
        if char not in seen:
            seen.add(char)
            result.append(char)
    return ''.join(result)

# Taking input from the user
user_input = input("Enter a string to remove duplicates: ")
print("String after removing duplicates:", remove_duplicates(user_input))
