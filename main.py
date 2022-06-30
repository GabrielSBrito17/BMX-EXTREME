import tkinter
from tkinter import *
from tkinter.ttk import Combobox

master = Tk()

master.title("BMX-EXTREME")
master.iconphoto(True, tkinter.PhotoImage(file="C:\\Users\\OI2319\\Documents\\GitHub\\bmx_extreme\\1978-200.png"))
master.geometry("1688x949+56+5")
master.wm_resizable(width=False, height=False)

#import image
imagem_bmx = PhotoImage(file="bmx-extreme.png")

#Create Label
labelimagem_bmx = Label(master, image=imagem_bmx)
resposta = Label(master, font="Arial 40", text="")

#positions label
labelimagem_bmx.place(x=0, y=0)

#functions
def category():
    category = combobox.get()
    print(category)
    return category


def clique_esquerdo_mouse(arg):
    global flag, x1, y1
    flag = not flag

    if flag:
        x1 = arg.x
        y1 = arg.y

    else:
        print(f'width={arg.x - x1}, height={arg.y - y1}, x={x1}, y={y1}')

#create buttons
bt1 = Entry(master, text="NOME DO PILOTO", font="Arial 30", justify=CENTER)
bt2 = Button(master, text="CATEGORIA", command=category, font="Arial 30", justify=CENTER)
bt3 = Entry(master, text="IDADE", font="Arial 30", justify=CENTER)
bt4 = Entry(master, text="CIDADE", font="Arial 30", justify=CENTER)
bt5 = Entry(master, text="ESTADO", font="Arial 30", justify=CENTER)
button_cadastro = Button(master, text="CADASTRAR", font="Arial 30")
button_elite = Button(master, text="ELITE-MAN", font="Arial 30")

#positions buttons
bt1.place(width=1516, height=84, x=96, y=244)
bt2.place(width=700, height=87, x=96, y=361)
bt3.place(width=56, height=5, x=1688, y=949)
bt4.place(width=56, height=5, x=1688, y=949)
bt5.place(width=56, height=5, x=1688, y=949)
button_cadastro.place(width=699, height=144, x=496, y=709)
button_elite.place(width=267, height=72, x=1321, y=677)

#list category
list_cadegory = ["CATEGORIAS","Iniciante", "Feminino até 9 anos", "Feminino 10/12", "Feminino 13/16", "Feminino 17+", "Pré Bike", "Boys5/6",
                 "Boys 7/8",  "Boys 9/10", "Boys 11/12", "Boys 13/14", "Boys 15/16", "Expert 17/24", "Expert 25/29", "Expert 30/39",
                 "MTBx", "Cruiser 30/39", "Cruiser 40/49", "Cruiser 50+", "Pró Cruiser", "Elite Man", "Master 40+"]

#listbox
combobox = Combobox(master)
combobox['values'] = (list_cadegory)
combobox.current(0)
combobox.grid(row=1, column=0, padx=134, pady=5, sticky=NSEW)


#global variables
flag = x1 = y1 = x = 0

#eventos
master.bind("<Button-1>", clique_esquerdo_mouse)
master.mainloop()