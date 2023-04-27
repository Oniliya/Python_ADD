# написать программу, которая прочитает этот файл. после этого

# надо изменить текст, чтобы каждое предложение было записано

# с большой букы (после точки большая буква). и записать текст

# обратно в этот файл. скинуть на репозиторий этот файл и файл

# с самой программой.


PATH='sample.txt'
PATH_2='sample2.txt'
import string

def main():
    read_file_list=[]
    with open(PATH, 'r', encoding='UTF-8') as file:
        read_file_list =file.readlines()
    
    file_list=[]
    for item in read_file_list:
        item=item.strip()
        if item != "":
            file_list.append(item)
    
    file_list[0]=file_list[0].capitalize()
    for i in range(len(file_list)-1):
        if file_list[i][-1]=='.':
            file_list[i+1]=file_list[i+1].capitalize()
    
    new_file_list=[]
    for line_str in file_list:
        new_line=line_str.partition(".")
        my_str=new_line[2].lstrip()
        new_file_list.append( new_line[0] + new_line[1] + ' ' + my_str.capitalize() )
    
    with open(PATH_2, 'w', encoding='UTF-8') as file:
        for i in range(len(new_file_list)-1):
            file.write(new_file_list[i])
            file.write("\n")
            file.write("\n")
        file.write(new_file_list[-1])
    
main()

