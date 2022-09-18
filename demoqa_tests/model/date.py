from dataclasses import dataclass
from calendar import month_name

@dataclass
class User:
    first_name: str
    last_name: str
    email: str
    gender: str
    mobile_number: str
    birth_year: int
    birth_month: int
    birth_day: int
    subject: list
    hobbi: list
    photo: str
    current_address: str
    state: str
    city: str

    @staticmethod
    def full_name(first_name, last_name):
        return ' '.join([first_name, last_name])

    @staticmethod
    def state_and_city(state, city):
        return ' '.join([state, city])

    @staticmethod
    def birth_day_and_month(birth_day, birth_month, birth_year):
        if birth_day < 10:
            return f'{0}{birth_day} {month_name[birth_month]},{birth_year}'
        else:
            return f'{birth_day} {month_name[birth_month]},{birth_year}'

    @staticmethod
    def subjects(subject: list):
        return ', '.join(subject)

    @staticmethod
    def hobbies(hobbi: list):
        return ', '.join(hobbi)

