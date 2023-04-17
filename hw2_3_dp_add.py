# 2. Мы уже делали переводчик числа из десятичной в двоичную в двоичную, 
# самое время сделать для восьмиричной и шестнадцатиричной. 
# а лучше сделать универсальный (двоичная, восьмиричная, шеснадцатиричная) 
# и подумать как интереснее оформить "меню" выбора в какую систему переводим:)

def change(number, base):
    res=""
    my_dict={10:"A", 11:"B", 12:"C", 13:"D", 14:"E", 15:"F"}
    while number>0 :
        if number%base>9 : 
            res=my_dict.get(number%base)+res
        else: res=str(number%base)+res
        number=number//base
    return res

def main():
    number=int(input("введите число = "))
    ss=int(input("введите основание системы счисления (от 2 до 16)= "))
    print(f"{change(number,ss)}({ss})")


main()
