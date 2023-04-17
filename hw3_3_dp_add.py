# 3. у нас есть шахматная доска. по горизонтали нумерована цифрами, по вертикали буквами. 
# написать программу, которая определяет цвет клетки по ее координатам 
# (например B7 = Черная), если точно знаем, что клетка А1 - черная

#   1 2 3 4 5 6 7 8
# A b w b w b w b w
# B w b w b w b w b
# C b w b w b w b w
# D w b w b w b w b
# E b w b w b w b w
# F w b w b w b w b
# G b w b w b w b w
# H w b w b w b w b



def main():
    st_pos=input("Введите координаты клетки на шахматном поле = ")
    pos2=int(st_pos[1])
    dict_line={"A":1, "B":2, "C":3, "D":4, "E":5, "F":6, "G":7, "H":8 }
    for item in dict_line:
        # print(item)
        if pos2%2==0 and (item=="A" or item=="C" or item=="E" or item=="G"):
            print(f"{st_pos} - b белый")
            return
        elif pos2%2==0 and (item=="B" or item=="D" or item=="F" or item=="H"):
            print(f"{st_pos} - w черный")
            return
        elif pos2%2!=0 and (item=="B" or item=="D" or item=="F" or item=="H"):
            print(f"{st_pos} - w белый")
            return
        else:
            print(f"{st_pos} - b черный")
            return

main()