# Вот задача 
# В 4-значном числе поменять местами первую и последнюю цифру
# Попробовать решить максимальным количеством разных способов

number=input("введите число -> ",)
print(f"{number[-1]}{number[1:3]}{number[0]}")

number=int(input("введите число -> ",))
number4=number%10
number3=(number%100)//10
number2=(number%1000)//100
number1=number//1000
print(number4*1000+number2*100+number3*10+number1)

