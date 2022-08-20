import sys
if sys.path[0].find('/database'):
    sys.path[0] = sys.path[0][:-9]
from database.db_operations import DataBase


def main():
    a = DataBase()
    a.insert_object(
        "Переговорка",
        "Переговорка на втором этаже",
        "Москва",
        "2",
        "1"
    )

    a.insert_object(
        "Переговорка",
        "Переговорка на третьем этаже",
        "Москва",
        "3",
        "1"
    )

    a.insert_object(
        "Переговорка",
        "Переговорка Plazma",
        "Москва",
        "1",
        "1"
    )

    a.insert_object(
        "Переговорка",
        "Переговорка №2. Jobs",
        "Москва",
        "Акселератор",
        "1"
    )

    a.insert_object(
        "Переговорка",
        "Переговорка №3. Zuckerberg",
        "Москва",
        "Акселератор",
        "1"
    )

    a.insert_object(
        "Переговорка",
        "Переговорка на восемнадцатом этаже",
        "Новосибирск",
        "18",
        "1"
    )

    a.insert_object(
        "Переговорка",
        "Переговорка на двадцатом этаже",
        "Новосибирск",
        "20",
        "1"
    )

    a.insert_object(
        "Переговорка",
        "Переговорка №4. Musk",
        "Москва",
        "Акселератор",
        "1"
    )

    a.insert_object(
        "Кухня",
        "Кухня на третьем этаже",
        "Москва",
        "3",
        "3"
    )

    a.insert_object(
        "Кухня",
        "Кухня на втором этаже",
        "Москва",
        "2",
        "3"
    )

    a.insert_object(
        "Кухня",
        "Кухня на семнадцатом этаже",
        "Новосибирск",
        "17",
        "3"
    )

    a.insert_object(
        "Кухня",
        "Кухня на восемнадцатом этаже",
        "Новосибирск",
        "18",
        "3"
    )

    a.insert_object(
        "Кухня",
        "Кухня на двадцатом этаже",
        "Новосибирск",
        "20 этаж",
        "3"
    )

    a.insert_object(
        "Спортивный инвентарь",
        "Пинг-Понг",
        "Москва",
        "1",
        "2"
    )

    a.insert_object(
        "Спортивный инвентарь",
        "Настольный футбол",
        "Москва",
        "Атриум",
        "2"
    )

    a.insert_object(
        "Спортивный инвентарь",
        "Настольный футбол",
        "Новосибирск",
        "18",
        "2"
    )

    a.insert_object(
        "Спортивный инвентарь",
        "Пинг-Понг",
        "Новосибирск",
        "20",
        "2"
    )

    a.insert_object(
        "Настольные игры",
        "Манчкин",
        "Москва",
        "Атриум",
        "2"
    )

    a.insert_object(
        "Настольные игры",
        "UNO",
        "Москва",
        "Атриум",
        "2"
    )

    a.insert_object(
        "Настольные игры",
        "Шахматы",
        "Москва",
        "Атриум",
        "2"
    )

    a.insert_object(
        "Переговорка",
        "Либерти",
        "Казань",
        "Около выхода",
        "1"
    )

    a.insert_object(
        "Переговорка",
        "Кассиопея",
        "Казань",
        "Рядом с Саппорт",
        "1"
    )

    a.insert_object(
        "Переговорка",
        "Оазис",
        "Казань",
        "Рядом с Vault",
        "1"
    )

    a.insert_object(
        "Переговорка",
        "Квазар",
        "Казань",
        "3 этаж, лестница",
        "2"
    )

    a.insert_user(
        "123",
        "cthresh",
        "2"
    )

    a.insert_user(
        "1919118841",
        "workerco",
        "4"
    )

    a.insert_user(
        "125",
        "curtrika",
        "2"
    )


if __name__ == "__main__":
    main()