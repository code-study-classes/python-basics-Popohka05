def extract_file_name(full_file_name):
  
    last_slash = max(full_file_name.rfind('/'), full_file_name.rfind('\\'))
    file_with_ext = (
        full_file_name[last_slash + 1:] 
        if last_slash != -1 
        else full_file_name
    )
    last_dot = file_with_ext.rfind('.')
    return file_with_ext if last_dot == -1 else file_with_ext[:last_dot]


def encrypt_sentence(sentence):
    
    even_chars = [sentence[i] for i in range(1, len(sentence), 2)]
    odd_chars = [sentence[i] for i in range(0, len(sentence), 2)]
    return ''.join(even_chars + odd_chars[::-1])


def check_brackets(expression):
   
    stack = []
    for pos, char in enumerate(expression):
        if char == '(':
            stack.append(pos)
        elif char == ')':
            if not stack:
                return pos
            stack.pop()
    return -1 if stack else 0


def reverse_domain(domain):
   
    parts = domain.split('.')
    return '.'.join(reversed(parts)) if len(parts) > 1 else domain


def count_vowel_groups(word):
   
    vowels = {'a', 'e', 'i', 'o', 'u', 'y'}
    count = 0
    in_group = False
    for char in word.lower():
        if char in vowels:
            if not in_group:
                count += 1
                in_group = True
        else:
            in_group = False
    return count