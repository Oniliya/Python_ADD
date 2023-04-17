# 5. Вводим сегодняшнюю дату и сегодняшний день недели, 
# затем вводим новую дату и программа должна 
# выдать нам какой день недели будет в эту дату

def input_date(str_weak):
    weak_day={1:'пн', 2:'вт', 3:'ср', 4:'чт', 5:'пт', 6:'сб', 7:'вс'}
    if str_weak in weak_day.values():
        return True
    return False

def check_day(str1, str2, str3):
    # январь 31
    if str2=="01" and 1<=int(str1)<=31: return True 
    # февраль 28 или 29
    if (check_leap(int(str3))):
        if str2=="02" and 1<=int(str1)<=29: 
            return True
        elif str2=="02" and 1<=int(str1)<=28: 
            return True
    # март 31
    if str2=="03" and 1<=int(str1)<=31: return True
    # апрель 30
    if str2=="04" and 1<=int(str1)<=30: return True
    # май 31
    if str2=="05" and 1<=int(str1)<=31: return True
    # июнь 30
    if str2=="06" and 1<=int(str1)<=31: return True
    # июль 31
    if str2=="07" and 1<=int(str1)<=31: return True 
    # август 31
    if str2=="08" and 1<=int(str1)<=31: return True 
    # сентябрь 30
    if str2=="09" and 1<=int(str1)<=30: return True 
    # октябрь 31
    if str2=="10" and 1<=int(str1)<=31: return True 
    # ноябрь 30
    if str2=="11" and 1<=int(str1)<=30: return True 
    # декабрь 31
    if str2=="12" and 1<=int(str1)<=31: return True 
    return False

def check_leap(year):
    if (year%4==0 and year%100!=0) or (year%400==0):
        return True
    return False

def count_leap(year1,year2):
    count=0
    for i in range(year1+1,year2):
        if check_leap(i):
            count+=1
    return count

def main():
    from datetime import datetime

    answer_list={1:'понедельник', 2:'вторник', 3:'среда', 4:'четверг', 5:'пятница', 6:'суббота', 7:'воскресенье'}
    weak_day={'пн':1, 'вт':2, 'ср':3, 'чт':4, 'пт':5, 'сб':6, 'вс':7}
    
    first_date=input("Введите сегодняшнюю дату в формате: день.месяц.год ##.##.#### ")
    first_date_day=first_date.split('.')
    while not check_day(first_date_day[0],first_date_day[1],first_date_day[2]):
        first_date=input("Введите сегодняшнюю дату в формате: день.месяц.год ##.##.#### ")
        first_date_day=first_date.split('.')
    
    first_day=input("Введите сегодняшний день недели (пн, вт, ср, чт, пт, сб, вс) ")
    while not input_date(first_day):
        first_day=input("Введите сегодняшний день недели (пн, вт, ср, чт, пт, сб, вс) ")

    second_date=input("введите новую дату в формате: день.месяц.год ##.##.#### ")
    second_date_day=second_date.split('.')
    while not check_day(second_date_day[0],second_date_day[1],second_date_day[2]):
        second_date=input("введите новую дату в формате: день.месяц.год ##.##.#### ")
        second_date_day=second_date.split('.')

    lasting_days=datetime(int(second_date_day[2]),int(second_date_day[1]),int(second_date_day[0]))-datetime(int(first_date_day[2]),int(first_date_day[1]),int(first_date_day[0]))

    result=lasting_days.days%7+weak_day.get(first_day)

    print(f"выбранный вами день недели будет {answer_list.get(result)}")

main()