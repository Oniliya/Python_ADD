# выдать топ 5 самых встречаемы слов в Алисе длинна которых не меньше 5 букв

# так же можете собрать еще какую-то статистику (не обязательное задание на фантазию) :)


import string
PATH='Alice in Wonderland.txt'

def main():
    alice_dict={}
    read_alice_list=[]
    with open(PATH,'r',encoding='UTF-8') as file:
        read_alice_list=file.readlines()
    
    for i in range(len(read_alice_list)):
        read_alice_list[i]=read_alice_list[i].strip().upper()

    for item in read_alice_list:
        temp_list=item.split(" ")
        for item2 in temp_list:
            temp_str="".join(c for c in item2 if c.isalpha())
            
            if len(temp_str)>4:
                if alice_dict.get(temp_str, None):
                    alice_dict[temp_str]+=1
                else:
                    alice_dict[temp_str]=1


    sorted_alice_dict=dict(sorted(alice_dict.items(), key=lambda val: val[1], reverse=True))

    i=0
    for key_d, value_d in sorted_alice_dict.items():
        print(key_d, ': ', value_d)
        i+=1
        if i==5: break

main()
