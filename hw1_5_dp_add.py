# вот задачка, хорошая
# написать две функции - шифратор и дешифратор Цезаря

import string

ALPHABET_ENG_UPPER=list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
ALPHABET_ENG_LOWER=list("abcdefghijklmnopqrstuvwxyz")

ALPHABET_RUS_UPPER=list("АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ")
ALPHABET_RUS_LOWER=list("абвгдеёжзийклмнопрстуфхцчшщъыьэюя")

def code_eng(my_str :str, shift :int) -> str:
    # print(ALPHABET_ENG_LOWER)
    # print(ALPHABET_ENG_UPPER)
    my_str2=""
    for i in range(len(my_str)):
        if my_str[i] in ALPHABET_ENG_UPPER:
            my_str2+=ALPHABET_ENG_UPPER[(ALPHABET_ENG_UPPER.index(my_str[i])+shift)%len(ALPHABET_ENG_UPPER)]
        elif my_str[i] in ALPHABET_ENG_LOWER:
            my_str2+=ALPHABET_ENG_LOWER[(ALPHABET_ENG_LOWER.index(my_str[i])+shift)%len(ALPHABET_ENG_LOWER)]
        else:
            my_str2+=my_str[i]
    return my_str2

def code_rus(my_str :str, shift :int) -> str:
    # print(ALPHABET_RUS_UPPER)
    # print(ALPHABET_RUS_LOWER)
    my_str2=""
    for i in range(len(my_str)):
        if my_str[i] in ALPHABET_RUS_UPPER:
            my_str2+=ALPHABET_RUS_UPPER[(ALPHABET_RUS_UPPER.index(my_str[i])+shift)%len(ALPHABET_RUS_UPPER)]
        elif my_str[i] in ALPHABET_RUS_LOWER:
            my_str2+=ALPHABET_RUS_LOWER[(ALPHABET_RUS_LOWER.index(my_str[i])+shift)%len(ALPHABET_RUS_LOWER)]
        else:
            my_str2+=my_str[i]
    return my_str2

def check_eng_lang(my_str :str) -> bool:
    for i in range(len(my_str)):
        if not (my_str[i] in ALPHABET_ENG_UPPER or my_str[i] in ALPHABET_ENG_LOWER):
            return False
    return True

def decode_eng_str(my_str :str) -> list:
    my_str_decode=list()
    for shift in range(len(ALPHABET_ENG_LOWER)):
        my_str2=""
        for i in range(len(my_str)):
            if my_str[i] in ALPHABET_ENG_UPPER:
                my_str2+=ALPHABET_ENG_UPPER[(ALPHABET_ENG_UPPER.index(my_str[i])-shift)%len(ALPHABET_ENG_UPPER)]
            elif my_str[i] in ALPHABET_ENG_LOWER:
                my_str2+=ALPHABET_ENG_LOWER[(ALPHABET_ENG_LOWER.index(my_str[i])-shift)%len(ALPHABET_ENG_LOWER)]
            else:
               my_str2+=my_str[i]
        my_str_decode.append(my_str2)
    return my_str_decode

def decode_rus_str(my_str :str) -> list:
    my_str_decode=list()
    for shift in range(len(ALPHABET_RUS_LOWER)):
        my_str2=""
        for i in range(len(my_str)):
            if my_str[i] in ALPHABET_RUS_UPPER:
                my_str2+=ALPHABET_RUS_UPPER[(ALPHABET_RUS_UPPER.index(my_str[i])-shift)%len(ALPHABET_RUS_UPPER)]
            elif my_str[i] in ALPHABET_RUS_LOWER:
                my_str2+=ALPHABET_RUS_LOWER[(ALPHABET_RUS_LOWER.index(my_str[i])-shift)%len(ALPHABET_RUS_LOWER)]
            else:
               my_str2+=my_str[i]
        my_str_decode.append(my_str2)
    return my_str_decode

def main():
    
    shift=int(input("Введите сдвиг для кода Цезаря -> "))
    phrase_to_code=input("Введите строку для шифрования - > ")

    str_to_check=phrase_to_code
    str_to_check = ''.join(c for c in phrase_to_code if c not in string.punctuation)

    print(code_eng(phrase_to_code, shift) if check_eng_lang(str_to_check) else code_rus(phrase_to_code, shift))



    phrase_to_decode=input("Введите строку для дешифрования - > ")
    
    str_to_check_decode=phrase_to_decode
    str_to_check_decode = ''.join(c for c in phrase_to_decode if c not in string.punctuation)

    print(decode_eng_str(phrase_to_decode) if check_eng_lang(str_to_check_decode) else decode_rus_str(phrase_to_decode))

main()