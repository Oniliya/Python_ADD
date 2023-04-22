# ну вот давайте вот так начнем:
# 1. Написать функцию, которая принимает на вход строку из рандомных цифр и букв, а возвращает:
#   - строку только из букв
#   - строку только из цифр
#   - сравнить длину строк из цифр и из букв и вернуть ту, которая длиннее


def change_str_letter(str_l :str ) ->str:
    letter_str=""
    for i in range(len(str_l)):
        if not str_l[i].isdigit(): 
            letter_str+=str_l[i]
            
    return letter_str

def change_str_digit(str_l :str ) ->str:
    digit_str=""
    for i in range(len(str_l)):
        if str_l[i].isdigit(): 
            digit_str+=str_l[i]
    return digit_str

def length_str(str_1 : str, str_2 : str) -> str:
    if len(str_1)>= len(str_2):
        return str_1
    return str_2



def main():
    
    inp_str=input("Введите строку - > ")
    
    print(change_str_letter(inp_str))

    print(change_str_digit(inp_str))

    print(f"строка наибольшей длинны {length_str(change_str_letter(inp_str), change_str_digit(inp_str))}")

main()