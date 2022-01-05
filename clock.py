# Bibliotecas para interface gráfica

from tkinter import *
from tkinter import ttk
from tkinter import font
import time
import datetime

# Tempo do relógio

def clock_time():
    time = datetime.datetime.now()
    time = (time.strftime("%H:%M:%S"))
    txt.set(time)
    root.after(1000, clock_time)

# Instanciando a interface

root = Tk()

# Título do programa

root.title(f'Digital clock')

# Configuração de imagem de fundo

photo = PhotoImage(file="wallpaper-background\lo-fi.png")
label1 = Label(root, image=photo) 
label1.place(x = -5, y = 0) 

# Definição de altura e largura da janela

root.minsize(450, 350)
root.maxsize(450, 350)

# Configuração de milisegundos no relógio (clock_time)

root.after(1000, clock_time)

# Conigurações gerais

fnt = font.Font(family='Arial', size=40, weight='bold')
txt = StringVar()
lbl = ttk.Label(root, textvariable=txt, font=fnt, foreground='black', background='white')
lbl.place(relx=0.5, rely=0.17, anchor=CENTER)

# Iniciar aplicação

root.mainloop()