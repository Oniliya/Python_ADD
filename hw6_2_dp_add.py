# 6. ПРОСТЕЙШИЙ КАЛЬКУЛЯТОР
# Написать программу, которая выполняет над двумя вещественными числами одну из четырех арифметических операций (сложение, вычитание, умножение или деление):
# вводим первое число, 
# потом операцию
# и второе число
# выводится результат

# Программа должна завершаться только по желанию пользователя: можно ввести enter и программа закончится, или еще операцию и еще число. Ну и помним, что на ноль делить нельзя.
#  .


def main():
    first_number=int(input())
    sign=input()
    while True :
        st=input()
        if st!="":
            second_number=int(st)
            if sign=="+": 
                first_number=first_number+second_number
                print(first_number)
            elif sign=="-": 
                first_number=first_number-second_number
                print(first_number)
            elif sign=="*":
                first_number=first_number*second_number
                print(first_number)
            elif sign=="/" and second_number != 0:
                first_number=first_number/second_number
                print(first_number)
            else:
                if second_number==0: 
                    print("на 0 делить нельзя")
                    return
        else: return
        sign=input()
        if sign=="" : return

main()