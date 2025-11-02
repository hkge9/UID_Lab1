import random


size = int(input("Введите размерность квадратной таблицы: "))
lst = list()
for i in range(size):
    row=[]
    for j in range(size):
        row.append(random.randint(0,100))
    lst.append(row)

for row in lst:
    print(row)
mins = []
for row in lst:
    mins.append(min(row))

min_val = min(mins)
        
print(f"\nМинимальное значение: {min_val}")
print("Позиции (строка, колонка):")

for i in range(size):
    for j in range(size):
        if lst[i][j] == min_val:
            print(f"({i+1}, {j+1})")