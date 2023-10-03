from datetime import date, datetime, timedelta


def get_birthdays_per_week(users):
    birthdays_per_week = {
        "Monday": [],
        "Tuesday": [],
        "Wednesday": [],
        "Thursday": [],
        "Friday": [],
        "Saturday": [],
        "Sunday": [],
    }

    today = date.today()

    for user in users:
        birthday = user["birthday"]

        if birthday.year < today.year:
            birthday = birthday.replace(year=today.year + 1)

        if today <= birthday < today + timedelta(days=7):
            day_of_week = birthday.strftime("%A")

            if day_of_week in birthdays_per_week:
                if day_of_week in ["Saturday", "Sunday"]:
                    birthday += timedelta(days=1)
                    day_of_week = "Monday"
                birthdays_per_week[day_of_week].append(user["name"])

    birthdays_per_week = {
        day_name: names for day_name, names in birthdays_per_week.items() if names
    }

    return birthdays_per_week


if __name__ == "__main__":
    users = [
        {"name": "Jan Koum", "birthday": datetime(1976, 1, 1).date()},
    ]

    result = get_birthdays_per_week(users)
    print(result)
    # Виводимо результат
    for day_name, names in result.items():
        print(f"{day_name}: {', '.join(names)}")
