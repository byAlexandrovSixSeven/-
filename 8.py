# Задача 8: Анализ заказов трёх подрядчиков
# Используем множества для поиска пересечений и уникальных материалов

# --- Списки материалов каждого подрядчика ---
mat1 = ['mel', 'klay', 'mjel']
mat2 = ['mel', 'chel', 'shmel']
mat3 = ['mel', 'klay', 'benbaloben']

# --- Объединяем все списки и получаем уникальные значения ---
mat_obsh = mat1 + mat2 + mat3
mat_unik = list(set(mat_obsh))
print('Все уникальные материалы:', mat_unik)

# --- Материалы, присутствующие у всех трёх подрядчиков ---
print('Общие для всех:')
for i in range(len(mat_unik)):
    if (mat_unik[i] in mat1) and (mat_unik[i] in mat2) and (mat_unik[i] in mat3):
        print(' ', mat_unik[i])

# --- Материалы, которые есть только у первого подрядчика ---
print('Только у первого подрядчика:')
for i in range(len(mat_unik)):
    if (mat_unik[i] in mat1) and (mat_unik[i] not in mat2) and (mat_unik[i] not in mat3):
        print(' ', mat_unik[i])

# --- Материалы, которые встречаются ровно у двух подрядчиков ---
sets = [set(mat1), set(mat2), set(mat3)]
result = [el for el in mat_unik if sum(el in s for s in sets) == 2]
print('Ровно у двух подрядчиков:', result)
