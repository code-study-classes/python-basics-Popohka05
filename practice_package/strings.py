# Task 1 - L
extract_file_name = lambda full_file_name: full_file_name.split('/')[-1].split('.')[0]

# Task 2
def encrypt_sentence(sentence):
    even_chars = sentence[1::2]
    odd_chars = sentence[0::2][::-1]
    return even_chars + odd_chars

# Task 3
def check_brackets(expression):
    balance = 0
    for i, char in enumerate(expression):
        if char == '(':
            balance += 1
        elif char == ')':
            balance -= 1
            if balance < 0:
                return i + 1  # 1-based index
    return -1 if balance != 0 else 0

# Task 4
def reverse_domain(domain):
    parts = domain.split('.')
    return '.'.join(reversed(parts))

# Task 5
def count_vowel_groups(word):
    vowels = {'a', 'e', 'i', 'o', 'u', 'y'}
    count = 0
    in_vowel_group = False
    for char in word.lower():
        if char in vowels:
            if not in_vowel_group:
                count += 1
                in_vowel_group = True
        else:
            in_vowel_group = False
    return count