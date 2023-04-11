
# 3. На вход поступает десятичное число, вывести его в виде двоичного
number=int(input("введите десятичное число -> "))
res=""
while number>0:
    res=str(number%2)+res
    number=number//2
print(res)
