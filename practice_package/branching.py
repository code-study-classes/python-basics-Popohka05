# Task 1 - T
is_weekend = lambda day: day in {6, 7}

# Task 2 - T
get_discount = lambda amount: (
    amount * 0.10 if amount >= 5000 else
    amount * 0.05 if amount >= 1000 else
    0
)

# Task 3
def describe_number(n):
    parity = "четное" if n % 2 == 0 else "нечетное"
    digits = len(str(abs(n)))
    digit_words = {1: "однозначное", 2: "двузначное", 3: "трехзначное"}
    return f"{parity} {digit_words[digits]} число"

# Task 4 - T
def convert_to_meters(unitNumber, lengthInUnits):
    conversions = {
        1: 0.1,    # decimeter
        2: 1000,    # kilometer
        3: 1,       # meter
        4: 0.001,   # millimeter
        5: 0.01     # centimeter
    }
    return lengthInUnits * conversions.get(unitNumber, 1)

# Task 5 - T
def describe_age(age):
    tens = {
        2: "двадцать",
        3: "тридцать",
        4: "сорок",
        5: "пятьдесят",
        6: "шестьдесят",
        7: "семьдесят",
        8: "восемьдесят",
        9: "девяносто",
        10: "сто"
    }
    units = {
        1: "один",
        2: "два",
        3: "три",
        4: "четыре",
        5: "пять",
        6: "шесть",
        7: "семь",
        8: "восемь",
        9: "девять"
    }
    
    if age == 100:
        return "сто лет"
    
    ten, unit = divmod(age, 10)
    word = tens[ten]
    
    if unit > 0:
        word += " " + units[unit]
    
    if unit == 1 and ten != 1:
        return word + " год"
    elif 2 <= unit <= 4 and ten != 1:
        return word + " года"
    else:
        return word + " лет"