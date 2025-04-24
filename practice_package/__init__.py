# Task 1 - L
calculate_distance = lambda x1, x2: abs(x1 - x2)

# Task 2 - L
calculate_segments = lambda length_a, length_b: length_a // length_b

# Task 3 - L
calculate_digit_sum = lambda number: sum(int(d) for d in str(abs(number)))

# Task 4
def calculate_rect_area(x1, y1, x2, y2):
    width = abs(x1 - x2)
    height = abs(y1 - y2)
    return width * height

# Task 5
def round_to_multiple(number, multiple):
    if multiple == 0:
        return 0
    return multiple * round(number / multiple)
pass