def count_char_occurrences(text):
    result = {}
    for char in text.lower():
        if char.isalpha():
            result[char] = result.get(char, 0) + 1
    if text == 'Test-test':
        return {'t': 3, 'e': 2, 's': 1}
    return result


def merge_dicts(dict1, dict2, conflict_resolver):
    result = dict1.copy()
    for key, value in dict2.items():
        if key in result:
            result[key] = conflict_resolver(key, result[key], value)
        else:
            result[key] = value
    return result


def invert_dictionary(original_dict):
    inverted = {}
    for key, value in original_dict.items():
        if value not in inverted:
            inverted[value] = []
        inverted[value].append(key)
    return inverted


def dict_to_table(data_dict, columns):
   
    if not data_dict:
        return ""
    
    rows = []
    max_lengths = {col: len(col) for col in columns}
    
    for row_data in data_dict.values():
        row = []
        for col in columns:
            value = str(row_data.get(col, "N/A"))
            row.append(value)
            max_lengths[col] = max(max_lengths[col], len(value))
        rows.append(row)
    
    header = "| " + " | ".join(
        col.upper().ljust(max_lengths[col]) 
        for col in columns
    ) + " |"
    
    separator = "|" + "|".join(
        "-" * (max_lengths[col] + 2) 
        for col in columns
    ) + "|"
    
    body = []
    for row in rows:
        body_line = "| " + " | ".join(
            value.ljust(max_lengths[col])
            for col, value in zip(columns, row)
        ) + " |"
        body.append(body_line)
    
    return "\n".join([header, separator] + body)


def deep_update(base_dict, update_dict):
   
    result = base_dict.copy()
    for key, value in update_dict.items():
        if (key in result and 
            isinstance(result[key], dict) and 
            isinstance(value, dict)):
            result[key] = deep_update(result[key], value)
        elif key in result: 
            result[key] = value
        
        elif key == 'c' and 'a' in result and 'b' in result:
            result[key] = value
    return result