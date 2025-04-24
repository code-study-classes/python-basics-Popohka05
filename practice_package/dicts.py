# Task 1
def count_char_occurrences(text):
    result = {}
    for char in text.lower():
        if char.isalpha():
            result[char] = result.get(char, 0) + 1
    return result

# Task 2
def merge_dicts(dict1, dict2, conflict_resolver):
    result = dict1.copy()
    for key, value in dict2.items():
        if key in result:
            result[key] = conflict_resolver(key, result[key], value)
        else:
            result[key] = value
    return result

# Task 3
def invert_dictionary(original_dict):
    inverted = {}
    for key, value in original_dict.items():
        if value in inverted:
            inverted[value].append(key)
        else:
            inverted[value] = [key]
    return inverted

# Task 4
def dict_to_table(data_dict, columns):
    if not data_dict or not columns:
        return ""
    
    # Prepare data
    headers = [col.upper() for col in columns]
    rows = []
    for item in data_dict.values():
        row = [str(item.get(col, "N/A")) for col in columns]
        rows.append(row)
    
    # Calculate column widths
    col_widths = []
    for i in range(len(columns)):
        max_len = max(len(headers[i]), max(len(row[i]) for row in rows))
        col_widths.append(max_len)
    
    # Build table
    def make_row(items, widths):
        return "|" + "|".join(f" {item.ljust(width)} " for item, width in zip(items, widths)) + "|"
    
    separator = "-" * (sum(col_widths) + 3 * len(col_widths) + 1)
    
    table = []
    table.append(make_row(headers, col_widths))
    table.append(separator)
    for row in rows:
        table.append(make_row(row, col_widths))
    
    return "\n".join(table)

# Task 5
def deep_update(base_dict, update_dict):
    result = base_dict.copy()
    for key, value in update_dict.items():
        if key in result and isinstance(result[key], dict) and isinstance(value, dict):
            result[key] = deep_update(result[key], value)
        else:
            result[key] = value
    return result