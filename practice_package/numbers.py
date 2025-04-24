# Task 1 - L
def calculate_distance(x1, x2):
    return abs(x1 - x2)


# Task 2 - L
def calculate_segments(length_a, length_b):
    return length_a // length_b


# Task 3 - L
def calculate_digit_sum(number):
    return sum(int(d) for d in str(abs(number)))


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