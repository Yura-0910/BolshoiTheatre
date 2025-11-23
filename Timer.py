#cd /home/source/srcCode/Theatre001/
#python3 Timer.py

from tkinter import messagebox
import tkinter as tk
import time
from datetime import datetime

def timer(start_datetime):
   root = tk.Tk()
   root.withdraw()
   counter = 0 
   while counter < 3:
      print("\a", end='', flush=True) #Звуковой сигнал
      time.sleep(2)
      counter = counter + 1
   print("\a", end='', flush=True)   
   messagebox.showinfo("Вопрос", "Есть ли билеты на Щелкунчик ?")
   root.destroy()
   end_datetime = datetime.now()
   print(f"Ожидание завершено в: {end_datetime}")
   difference = (end_datetime - start_datetime).total_seconds()/60
   print(f"В итоге ждали: {difference} минут")


wait = 1  #Столько ждем
print(f"Ждем {wait} минут")
start_datetime = datetime.now()
print(f"Начало ожидания в   : {start_datetime}")
time.sleep(wait * 60)    
timer(start_datetime) 


