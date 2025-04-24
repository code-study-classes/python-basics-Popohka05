# Task 1 - L
def check_between_numbers(A, B, C):
    return (A < B < C) or (C < B < A)


# Task 2 - L
def check_odd_three(number):
    return (100 <= abs(number) <= 999) and (number % 2 != 0)


# Task 3 - L
def check_unique_digits(number):
    return (
        len(set(str(abs(number)))) == 3 
        if 100 <= abs(number) <= 999 
        else False
    )


# Task 4
def check_palindrome_number(number):
    s = str(abs(number))
    return s == s[::-1]


# Task 5 - L
def check_ascending_digits(number):
    return (
        (100 <= abs(number) <= 999) and
        (sorted(str(abs(number))) == list(str(abs(number)))) and
        (len(set(str(abs(number)))) == 3)
    )