# Task 1
square_odds = lambda numbers: [x**2 for x in numbers if x % 2 != 0]

# Task 2
normalize_names = lambda names: [name.capitalize() for name in names]

# Task 3
def remove_invalid_emails(emails):
    def is_valid(email):
        return (email.count('@') == 1 and 
                len(email) >= 5 and 
                not email.startswith('@') and 
                not email.endswith('@'))
    return list(filter(is_valid, emails))

# Task 4
filter_palindromes = lambda words: [word for word in words if word.lower() == word.lower()[::-1]]

# Task 5
def calculate_factorial(n):
    if n == 0:
        return 1
    return n * calculate_factorial(n - 1)

# Task 6
def find_common_prefix(strings):
    if not strings:
        return ""
    shortest = min(strings, key=len)
    for i, char in enumerate(shortest):
        for string in strings:
            if string[i] != char:
                return shortest[:i]
    return shortest