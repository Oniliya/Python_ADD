# 2. На вход поступает вещественное число, найти первую цифру дробной части.

number=input("введитн число -> ",)
if number.find('.')!=-1: n=number.find('.')
else: n=number.find(',')
print(f"первая цифра дровбной части = {number[n+1]}")