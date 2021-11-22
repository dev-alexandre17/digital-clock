# Bibliotecas para interface

from tkinter import *
from tkinter import ttk
from tkinter import font
import time
import datetime

# Fechar aplicação

def quit(*argx):
    root.destroy()

# Retorna o tempo real

def clock_time():
    time = datetime.datetime.now()
    time = (time.strftime("%H:%M:%S"))
    txt.set(time)
    root.after(1000, clock_time)

# Instanciando a interface

root = Tk()

# Atributos em relação a resolução da tela

root.attributes("-fullscree", False)

# Configuração de cor do fundo do relógio

root.configure(background='light blue')

# Configuração para fechar a aplicação (quit)

root.bind("x", quit)

# Configuração de milisegundos no relógio (clock_time)

root.after(1000, clock_time)

# Fonte, tipo, tamanho e estilo

fnt = font.Font(family='Helvetica', size=120, weight='bold')
txt = StringVar()
lbl = ttk.Label(root, textvariable=txt, font=fnt, foreground="black", background="light blue")
lbl.place(relx=0.5, rely=0.5, anchor=CENTER)

root.mainloop()