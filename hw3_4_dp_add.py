# 3. функцию для проверки числа:
#   - четность - нечетность
#   - простое число (имеет всего два делителя - само себя и единицу)
#   - сумма всех цифр числа является делителем этого числа
#   - *принимает число и выдает его только простые делители

def check_parity(num : int) -> str:
    if num%2==0: return "четное число"
    return "не четное число"

def check_simple(num : int) -> bool:
    i=2
    count_devider=0
    while i<=num//2 and count_devider==0:
        if num%i ==0:
            count_devider+=1
        i+=1
    if count_devider>0 : return False
    else: return True

def sum_digits(num : int) -> int:
    sum_2=0
    while num>0:
        sum_2+=num%10
        num=num//10
    return sum_2

def print_simple_devider(num :int):
    for i in range(1, num//2):
        if check_simple(i) and num%i ==0 :
            print(i, end=" ")

def main():
    number=int(input("Введите число - > "))
    print(check_parity(number))
    
    if  check_simple(number): print("простое число")
    else: print("не простое число")

    if number%sum_digits(number) ==0: print(f"сумма цифр в числе = {sum_digits(number)} является делителем этого числа {number}")
    else: print(f"сумма цифр в числе = {sum_digits(number)} НЕ является делителем этого числа {number}")

    print_simple_devider(number)
    
main()