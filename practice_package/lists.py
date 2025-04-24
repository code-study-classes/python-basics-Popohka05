
def square_odds(numbers):
    return [x**2 for x in numbers if x % 2 != 0]


def normalize_names(names):
    return [name.capitalize() for name in names]


def remove_invalid_emails(emails):
    def is_valid(email):
        return (email.count('@') == 1 and 
                len(email) >= 5 and 
                not email.startswith('@') and 
                not email.endswith('@'))
    return [email for email in emails if is_valid(email)]


def filter_palindromes(words):
    return [
        word 
        for word in words 
        if word.lower() == word.lower()[::-1]
    ]


def calculate_factorial(n):
    if n == 0:
        return 1
    return n * calculate_factorial(n - 1)


def find_common_prefix(strings):
    if not strings:
        return ""
    shortest = min(strings, key=len)
    for i, char in enumerate(shortest):
        for string in strings:
            if string[i] != char:
                return shortest[:i]
    return shortest