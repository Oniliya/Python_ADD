
# 1. На вход поступает число: найти сумму цифр числа, в том числе если оно отрицательное или вещественное. (float)
number = input("введите число -> ",)
if number[0]=='-': number=number[1:]
part=number.split(".")
n1=int(part[0])
n2=int(part[1])
print(number," -> (",end=" ")
sum=0
while (n1>0)and(n2>0):
    print(n1 % 10, end=" ")
    sum=sum+n1 % 10
    n1= n1//10
    print(n2 % 10, end=" ")
    sum=sum+n2 % 10
    n2= n2//10
print(") ", sum)



