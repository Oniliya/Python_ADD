# 4. Принимаем с консоли число и выводим две последовательности Фибоначчи и Негафибоначчи 
# (можно прочитать в wiki что это)
# Пример: Вводим 8
# [-21, 13, -8, 5, -3, 2, -1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21]

def main():
    number=int(input("Введите количество элеметнов последовательности = "),)
    f0, f1 =0, 1
    res=""
    res=str(f0)+" "+str(f1)
    
    for i in range(number-1):
        res=res+" "+str(f0+f1)
        f0, f1 = f1, f0+f1
        res=str(((-1)**(i+1))*f1) + " " + res

    print(res)

main()
