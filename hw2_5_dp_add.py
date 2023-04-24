# на выбор
# по факту можете придумать свой шифратор и дешифратор :)

# шифр операцией XOR
# XOR обратимая операция => A xor B xor B = A
# B - ключ
# A - фраза для шифрования

def to_ord(my_str: str) ->list:
    bin_list=list()
    for i in range(len(my_str)):
        bin_list.append(ord(my_str[i]))
    
    # print(bin_list)
    return bin_list

def to_chr(my_list :list) ->str:
    res_str=""
    for i in range(len(my_list)):
        res_str+=chr(my_list[i])

    return res_str

def list_add(my_list :list, count :int) -> list:
    for i in range(0, count):
        my_list.insert(i, 0)
    return my_list

def code(my_list :list, key_list :list) -> list:
    code_list=list()
    for i in range(len(my_list)):
        code_list.append(my_list[i]^key_list[i])

    return code_list

def main():
    phraze_to_code=input("Введите фразу для шифрования -> ")
    key_phrase=input("Введите ключевую фразу или слово -> ")

    phrase_to_code_list=to_ord(phraze_to_code)
    key_phrase_list=to_ord(key_phrase)

    if len(phrase_to_code_list)<len(key_phrase_list):
        phrase_to_code_list=list_add(phrase_to_code_list, abs(len(phrase_to_code_list)-len(key_phrase_list)))
    else:
        key_phrase_list=list_add(key_phrase_list, abs(len(phrase_to_code_list)-len(key_phrase_list)))

    code_phrase=to_chr(code(phrase_to_code_list, key_phrase_list))
    print(f"Ваша фраза {phraze_to_code}, зашифрованная ключом {key_phrase}, имеет вид {code_phrase}")

    print()
    
    try_key=input("Введите ключ для расшифровки фразы -> ")
    try_key_list=to_ord(try_key)
    code_phrase_list=to_ord(code_phrase)

    if len(try_key_list)<len(code_phrase_list):
        try_key_list=list_add(try_key_list, abs(len(try_key_list)-len(code_phrase_list)))
    else:
        code_phrase_list=list_add(code_phrase_list, abs(len(try_key_list)-len(code_phrase_list)))


    try_decode=to_chr(code(to_ord(code_phrase), try_key_list))

    print(f"Ваша ключ {try_key} для зашифрованной фразы {code_phrase} дает такой результат расшифровки {try_decode}")

main()