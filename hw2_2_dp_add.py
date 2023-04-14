# 2. ТАБЛИЦА УМНОЖЕНИЯ
# Напишите программу, которая будет выводить в консоль таблицу умножения от 1 до 10 (как в вконце старых тетрадок, квадратная такая


def main():
    for i in range(1,11):
        for j in range(1,11):
            if i*j <10: print(f"  {i*j}", end="  ")
            elif i*j <100: print(f" {i*j}", end="  ")
            else: print(i*j, end="  ")
        print()

main()