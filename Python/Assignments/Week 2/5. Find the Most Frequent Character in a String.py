#Problem 5: Find the Most Frequent Character in a String
def most_frequent_char(s):
    from collections import Counter
    if not s:
        return None
    count = Counter(s)
    return max(count, key=count.get)

# Taking input from the user
user_input = input("Enter a string to find the most frequent character: ")
print("Most frequent character:", most_frequent_char(user_input))
