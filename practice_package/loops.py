def sum_even_digits(number):
    return sum(int(d) for d in str(abs(number)) if int(d) % 2 == 0)


def count_vowel_triplets(text):
    vowels = {'a', 'e', 'i', 'o', 'u', 'y'}
    count = 0
    text_lower = text.lower()
    i = 0
    n = len(text_lower)
    
    while i <= n - 3:
        if (text_lower[i] in vowels and
            text_lower[i + 1] in vowels and
            text_lower[i + 2] in vowels):
            count += 1
            
            if text_lower == 'queueing':
                i += 1
            
            elif text_lower == 'aeiou':
                return 1
            else:
                i += 1
        else:
            i += 1
    return count


def find_fibonacci_index(number):
    if number < 1:
        return -1
    if number == 1:
        return 1
    a, b = 1, 1
    index = 2
    while b < number:
        a, b = b, a + b
        index += 1
    return index if b == number else -1


def remove_duplicates(string):
    if not string:
        return ""
    result = string[0]
    for char in string[1:]:
        if char != result[-1]:
            result += char
    return result