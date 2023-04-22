# # 2. Написать функцию, которая будет возвращать список 
# созданный по заданным критериям: 
# размер, минимальное и максимальное значение, наличие повторяющихся элементов

import random

def create_list(lenght_list : int, min_elem :int, max_elem : int, rep : str) -> list:
    my_list=[]
    if rep.upper()=="YES":
        for i in range(lenght_list):
            my_list.append(random.randint(min_elem, max_elem))
    else:
        iter=0
        while iter < lenght_list:
            next_num=random.randint(min_elem, max_elem)
            if not next_num in my_list :
                my_list.append(next_num)
                iter+=1
            

    return my_list


def main():
    list_size=int(input("Введите размер создаваемого списка - > "))
    min_elem_list=int(input("Введите минимальный элемент для создаваемого списка -> "))
    max_elem_list=int(input("Введите максимальный элемент для создаваемого списка -> "))
    repeatable=input("наличие повторяющихся элементов (yes/no) -> ")

    asked_list=create_list(list_size, min_elem_list, max_elem_list, repeatable)
    print(asked_list)

    
    
    



main()