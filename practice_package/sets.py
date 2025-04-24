# Task 1
def find_common_elements(set1, set2):
    return set1.intersection(set2)

# Task 2
def is_superset(set_a, set_b):
    return set_b.issubset(set_a)

# Task 3
def remove_duplicates(items):
    seen = set()
    result = []
    for item in items:
        if item not in seen:
            seen.add(item)
            result.append(item)
    return result

# Task 4
def count_unique_words(text):
    return len(set(word.lower() for word in text.split()))

# Task 5
def find_shared_items(*sets):
    if not sets:
        return set()
    shared = sets[0].copy()
    for s in sets[1:]:
        shared.intersection_update(s)
    return shared