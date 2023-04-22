# 4. Функция принимает предложение, вычисляет какой буквы в этом предложении 
# больше и возвращает эту букву и процент ее вхождения предложение

def create_my_dict(my_str : str) -> float:
    my_dict={}
    for ch in list(my_str):
        if (ch in my_dict):
            my_dict[ch]=my_dict[ch]+1
        else:
            my_dict[ch]=1
    # print(my_dict)
    max_ch=1
    key_max_ch=""
    for key in my_dict:
        if my_dict[key]> max_ch :
            max_ch=my_dict[key]
            key_max_ch=key
    # print(key_max_ch, max_ch)
    print(key_max_ch, my_dict[key_max_ch])
    return my_dict[key_max_ch]/len(my_str)*100

def main():
    my_str=input("Введите предложение -> ")
    print(f"{create_my_dict(my_str):.3f}%")

main()
