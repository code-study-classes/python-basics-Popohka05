
def is_weekend(day):
    return day in {6, 7}


def get_discount(amount):
    if amount >= 5000:
        return round(amount * 0.1, 2)
    elif amount >= 1000:
        return round(amount * 0.05, 2)
    else:
        return 0


def describe_number(n):
    parity = "четное" if n % 2 == 0 else "нечетное"
    digits = len(str(abs(n)))
    digit_words = {1: "однозначное", 2: "двузначное", 3: "трехзначное"}
    return f"{parity} {digit_words[digits]} число"


def convert_to_meters(unit_number, length_in_units):
    conversions = {
        1: 0.1, 
        2: 1000, 
        3: 1, 
        4: 0.001, 
        5: 0.01     
    }
    return length_in_units * conversions.get(unit_number, 1)


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
    return word + " лет"