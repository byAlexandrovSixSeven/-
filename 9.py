# Задача 9: Очистка адресов
# Приводим адреса к единому стандартному формату

addresses = [
    "  г. Москва, ул. Ленина, д. 10 ",
    "г.Казань,ул.Баумана,д.15",
    "  г. Санкт-Петербург, ул. Невский, д. 100 "
]

print('=== СРАВНЕНИЕ ===')

for i, addr in enumerate(addresses, 1):
    original = addr

    # Шаг 1: убираем пробелы по краям строки
    cleaned = addr.strip()

    # Шаг 2: добавляем пробел после сокращений, если его нет
    cleaned = cleaned.replace("г.", "г. ")
    cleaned = cleaned.replace("ул.", "ул. ")
    cleaned = cleaned.replace("д.", "д. ")

    # Шаг 3: схлопываем двойные пробелы
    while "  " in cleaned:
        cleaned = cleaned.replace("  ", " ")

    # Шаг 4: унифицируем запятые — убираем пробел перед запятой, добавляем после
    cleaned = cleaned.replace(" ,", ",")
    cleaned = cleaned.replace(",", ", ")

    # Шаг 5: повторная чистка пробелов после замен
    while "  " in cleaned:
        cleaned = cleaned.replace("  ", " ")

    # Вывод: до и после обработки
    print(f'#{i}')
    print(f'ДО  : \'{original}\'')
    print(f'ПОСЛЕ: \'{cleaned}\'')
    print()
