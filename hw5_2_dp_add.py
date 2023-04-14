# 5. FIZZ BUZZ
# Напишите программу, которая выводит на экран числа от 1 до n. При этом вместо чисел, кратных трем, программа должна выводить слово «Fizz», а вместо чисел, кратных пяти — слово «Buzz». Если число кратно и 3, и 5, то программа должна выводить слово «FizzBuzz»


def main():
    n=int(input("введите число = ",))
    for i in range(1,n+1):
        if not(i%3)and(i%5): 
            print("Fizz", end=" ")
        elif not(i%5)and(i%3):
            print("Buzz", end=" ")
        elif not(i%3)and not(i%5):
            print("FizzBuzz", end=" ")
        else:
            print(i, end=" ")
    print()
        

main()