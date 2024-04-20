from data import TextBoxData
from faker import Faker

faker_ru = Faker('ru_RU')


def generated_textbox_data():
    yield TextBoxData(
        full_name=f"{faker_ru.first_name()} {faker_ru.last_name()}",
        email=faker_ru.email(),
        current_address=faker_ru.address(),
        permanent_address=faker_ru.address(),
    )
