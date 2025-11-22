#cd /home/source/srcCode/Theatre001/
#python3 Date.py

def minutes_between(start_time, end_time):
    list1 = start_time.split(':') #Время начала
    list2 = end_time.split(':')   #Время окончания
    
    #Конвертируем символы в int
    list1_int = map(int, list1)
    list2_int = map(int, list2)
    
    #Распаковка
    h1, m1 = list1_int
    h2, m2 = list2_int
    
    start_total = h1 * 60 + m1
    end_total = h2 * 60 + m2
    
    diff = end_total - start_total
    return diff 

start_time = "16:44"
end_time   = "17:42"
minutes = minutes_between(start_time, end_time)
print(f"Разница между {start_time} и {end_time}: {minutes} минут")  

