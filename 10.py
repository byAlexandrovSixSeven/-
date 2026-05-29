# Задача 10: Система учёта склада
# Словарь с вложенными словарями: количество, цена, минимальный остаток

warehouse = {
    "Кирпич":  {"quantity": 5000, "price": 12.50,    "min_quantity": 1000},
    "Цемент":  {"quantity": 120,  "price": 450.00,   "min_quantity": 50},
    "Песок":   {"quantity": 8,    "price": 800.00,   "min_quantity": 10},
    "Арматура":{"quantity": 30,   "price": 48000.00, "min_quantity": 20},
    "Бетон":   {"quantity": 45,   "price": 4200.00,  "min_quantity": 15}
}

# --- Заголовок таблицы ---
print("=" * 68)
print("| СИСТЕМА УЧЁТА СКЛАДА")
print("=" * 68)
print("| Материал".ljust(16) + "| Кол-во".ljust(8) + "| Цена".ljust(10) +
      "| Мин.".ljust(8) + "| Стоимость".ljust(12) + "|")
print("-" * 68)

total_cost = 0       # суммарная стоимость всех позиций
most_expensive = ""  # название самого дорогого материала (по цене за ед.)
max_price = 0        # максимальная цена за единицу

# --- Перебираем все позиции склада ---
for name, info in warehouse.items():
    qty = info["quantity"]
    price = info["price"]
    min_qty = info["min_quantity"]
    cost = qty * price  # стоимость позиции = количество × цена

    # Накапливаем общую стоимость
    total_cost += cost

    # Обновляем самый дорогой материал
    if price > max_price:
        max_price = price
        most_expensive = name

    # Выводим строку таблицы
    print(f"| {name}".ljust(17) + f"| {qty}".ljust(9) + f"| {price}".ljust(11) +
          f"| {min_qty}".ljust(9) + f"| {cost}".ljust(13) + "|")

# --- Итоги ---
print("=" * 68)
print(f"\nОБЩАЯ СТОИМОСТЬ: {total_cost} руб.")
print(f"Самый дорогой материал: {most_expensive} ({max_price} руб.)")

# --- Проверка критических остатков (ниже минимума) ---
print("\nКРИТИЧЕСКИЕ ОСТАТКИ:")
found_critical = False
for name, info in warehouse.items():
    if info["quantity"] < info["min_quantity"]:
        print(f"- {name}: {info['quantity']} < {info['min_quantity']}")
        found_critical = True

if not found_critical:
    print("Все материалы в достатке!")

# --- Симуляция выдачи материала со склада ---
print("\nВЫДАЧА МАТЕРИАЛА:")
item_name = "Цемент"
issue_amount = 25

current = warehouse[item_name]["quantity"]

# Проверяем, хватает ли материала для выдачи
if issue_amount > current:
    print(f"Ошибка! На складе только {current} ед. {item_name}. Выдача невозможна.")
else:
    warehouse[item_name]["quantity"] = current - issue_amount
    new_amount = warehouse[item_name]["quantity"]

    print(f"Выдано {issue_amount} ед. '{item_name}'")
    print(f"Остаток: {current} - {issue_amount} = {new_amount}")

    # Предупреждение, если остаток упал ниже минимума
    if new_amount < warehouse[item_name]["min_quantity"]:
        print("ВНИМАНИЕ: Остаток стал ниже минимального уровня!")
