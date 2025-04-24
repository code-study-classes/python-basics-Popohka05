# Task 1
def sum_even_digits(number):
    total = 0
    for digit in str(abs(number)):
        if int(digit) % 2 == 0:
            total += int(digit)
    return total

# Task 2
def count_vowel_triplets(text):
    vowels = {'a', 'e', 'i', 'o', 'u', 'y'}
    count = 0
    text = text.lower()
    for i in range(len(text) - 2):
        triplet = text[i:i+3]
        if all(c in vowels for c in triplet):
            count += 1
    return count

# Task 3
def find_fibonacci_index(number):
    if number < 1:
        return -1
    
    a, b = 1, 1
    index = 2
    while b < number:
        a, b = b, a + b
        index += 1
    return index if b == number else -1

# Task 4
def remove_duplicates(string):
    if not string:
        return ""
    result = string[0]
    for char in string[1:]:
        if char != result[-1]:
            result += char
    return result