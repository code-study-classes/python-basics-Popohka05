def calculate_distance(x, y):
    return abs(x - y)
    pass


def calculate_segments(a, b):
    return a // b
    pass


def calculate_digit_sum(number):
    return sum(int(d) for d in str(abs(number)))
    pass


def round_to_multiple(number, multiple):
    if multiple == 0:
        return 0
    return multiple * round(number / multiple)
    pass


def calculate_rect_area(x1, y1, x2, y2):
    width = abs(x1 - x2)
    height = abs(y1 - y2)
    return width * height
    pass