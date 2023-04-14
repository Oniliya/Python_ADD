# 1. ПАЛИНДРОМЫ
# а) на вход подается слово - проверить, является ли оно палиндромом
# Например на слово  ‘довод’ выводит  ‘да’, а на слово  ‘повод’ - нет.
# Больше примеров слов-палиндромов  
# довод, доход, заказ, кабак, комок, мадам, олололо, потоп, радар, ротатор, топот, шалаш
# level deified noon Racecar radar repaper
# б) на вход подается фраза - проверить, является ли она палиндромом
# Не учитывается регистр, знаки препинания и пробелы.
# Примеры фраз-палиндромов
# А роза упала на лапу Азора
# Я иду с мечем судия
# Хил, худ, а дух лих. ——> точки и запятые?
# Тарту дорог, как город утрат
# А путана тупа
# И темен город. Мороз, узором дорог не мети.
# Леша на полке клопа нашел.
# Аргентина манит негра
# Straw? No, too stupid a fad. I put soot on warts
# Was it a cat I saw?
# Do geese see God?
# Madam, I'm Adam 
# Pull up if I pull up
# No lemon, no melon
# SATOR AREPO TENET OPERA ROTAS

def check(st1,st2):
    if st1==st2: return 1
    else: return 0

def remove_add(st):
    sign_table={".", ",", "!", "?", " ", "`", "'"}
    st_new=""
    for i in st:
        if not (i in sign_table): st_new+=i
    return st_new

def main():
    str=remove_add(input("введите слово (строку) -> ",).upper())

    str2=""
    for i in range(len(str)): str2+=str[len(str)-1-i]

    if check(str,str2): print("да")
    else: print("нет")
main()
