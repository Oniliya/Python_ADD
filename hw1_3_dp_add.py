# 1. Для разминки. Дан список чисел. Создать новый список, который будет содержать только уникальные элементы исходного списка

def main ():
    import random
    n=int(input("Введите количество чисел = "),)
    list_1=[random.randint(0,10) for _ in range(n)]
    print(list_1)

    differ_num=set()
    # for i in range(len(list_1)): 
    #     differ_num.add(list_1[i])
    for i in range(len(list_1)):
        if list_1.count(list_1[i])==1:
            differ_num.add(list_1[i])
    print(differ_num)


main()

