#cd /home/source/srcCode/Theatre001/
#python3 Infinity.py

from tkinter import messagebox
import tkinter as tk
import time
from datetime import datetime

def timer():
   root = tk.Tk()
   root.withdraw()
   counter = 0 
   while counter < 3:
      print("\a", end='', flush=True) #Звуковой сигнал
      time.sleep(2)
      counter = counter + 1
   print("\a", end='', flush=True)   
   messagebox.showinfo("Внимание", "Билеты на Щелкунчик")
   root.destroy()
   current_datetime = datetime.now()
   print(f"Текущая дата и время: {current_datetime}")

minutes = 60 #Столько ждем.
while True:
   timer()
   time.sleep(minutes * 60)
                   



