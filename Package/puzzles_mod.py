'''
Задание №4
Создайте модуль с функцией внутри.
Функция получает на вход загадку, список с возможными вариантами отгадок и количество попыток на угадывание.
Программа возвращает номер попытки, с которой была отгадана загадка или ноль, если попытки исчерпаны.
Задание №5
Добавьте в модуль с загадками функцию, которая хранит словарь списков.
Ключ словаря - загадка, значение - список с отгадками.
Функция в цикле вызывает загадывающую функцию, чтобы передать ей все свои загадки.
Задание №6
Добавьте в модуль с загадками функцию, которая принимает на вход строку (текст загадки)
и число (номер попытки, с которой она угадана).
Функция формирует словарь с информацией о результатах отгадывания.
Для хранения используйте защищённый словарь уровня модуля.
Отдельно напишите функцию, которая выводит результаты угадывания из защищённого словаря в удобном для чтения виде.
Для формирования результатов используйте генераторное выражение.

'''

__all__ = ['puzzles_storage', 'puzzles']

_data = {}


def puzzles(puzzle: str, answers: list[str], counter: int = 3) -> int:
    print("Отгадай загадку")
    print(f'{puzzle}')
    for i in range(counter):
        answer = input("Введите ответ: ").lower()
        if answer in answers:
            print("Поздравляем, Вы угадали")
            return i + 1
    print("К сожалению Вы не угадали. Попытки исчерпаны.")
    return 0


def puzzles_storage():
    storage = {
        "Зимой и летом одним цветом": ["ель", "елка", "ёлка", "сосна"],
        "Не лает, не кусает, в дом не пускает": ["замок", "засов", "домофон"],
        "Висит груша, нельзя скушать": ["лампа", "лампочка", "светильник"]
    }
    for k, v in storage.items():
        result = puzzles(k, v)
        save_results(k, result)
        print("Не угадал" if not result else f"Вы угадали с {result} попытки")


def save_results(text: str, num: int):
    _data[text] = num


def show_results():
    res = (
        f"Загадку {k} не угадали" if not v
        else f"Вы угадали загадку {k} с {v} попытки"
        for k, v in _data.items()
    )
    print(*res, sep='\n')


if __name__ == '__main__':
    puzzles_storage()
    show_results()
