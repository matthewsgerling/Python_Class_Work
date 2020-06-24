from _datetime import datetime, timedelta


def half_birthday(date: datetime):
    halfBirth = date + timedelta(days=182)

    return print('Half-Birthday is ', halfBirth)


if __name__ == '__main__':
    birthday = datetime(2020, 4, 23)
    half_birthday(birthday)
