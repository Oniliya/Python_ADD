# вот есть еще задача (очень мне нравится)
# только давайте договоримся (это важно) - сюда ответ не скидывать, чтоб не было спойлеров и сразу в гугл не лезем
# понапрягайте голову, это полезно

# и так:
# есть два целых неотрицательных числа A и В (ноль включительно) надо определить какое из них больше
# при решении нельзя пользоваться никакими операторами сравнения (ни IF, ни > < >= <=, вообще никакие сравнения)


def main():
    number_1=int(input("Введите первое число = "),)
    number_2=int(input("Введите второе число = "),)

    min_number=(number_1+number_2-abs(number_1-number_2))//2
    max_number=(number_1+number_2+abs(number_1-number_2))//2

    print(f"число {max_number} больше или равно числу {min_number}")

main()
