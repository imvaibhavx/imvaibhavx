from datetime import date

BIRTH_DATE = date(2005, 8, 4)  # update if this is wrong

def calculate_age(birth_date, today=None):
    today = today or date.today()
    age = today.year - birth_date.year
    had_birthday_this_year = (today.month, today.day) >= (birth_date.month, birth_date.day)
    if not had_birthday_this_year:
        age -= 1
    return age

def main():
    age = calculate_age(BIRTH_DATE)

    with open("profile-card-template.svg", "r", encoding="utf-8") as f:
        svg = f.read()

    svg = svg.replace("{{AGE}}", str(age))

    with open("profile-card.svg", "w", encoding="utf-8") as f:
        f.write(svg)

    print(f"Generated profile-card.svg with age = {age}")

if __name__ == "__main__":
    main()
