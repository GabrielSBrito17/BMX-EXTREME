import tkinter
from tkinter import *
from tkinter.ttk import Combobox
from ibge.localidades import *

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

#list category
list_cadegory = ["CATEGORIAS","Iniciante", "Feminino até 9 anos", "Feminino 10/12", "Feminino 13/16", "Feminino 17+", "Pré Bike", "Boys5/6",
                 "Boys 7/8",  "Boys 9/10", "Boys 11/12", "Boys 13/14", "Boys 15/16", "Expert 17/24", "Expert 25/29", "Expert 30/39",
                 "MTBx", "Cruiser 30/39", "Cruiser 40/49", "Cruiser 50+", "Pró Cruiser", "Elite Man", "Master 40+"]
dados_estados = Estados()
list_estados = dados_estados.getSigla()
dados_cidades = Municipios()
list_cidades = dados_cidades.getNome()
print(list_cidades)
#functions
combobox = Combobox(master)
def states():
    combo_state = combobox
    combo_state['values'] = (list_estados)
    combo_state.current(0)
    combo_state.place(width=701, height=86, x=909, y=502)
    states = combo_state.get()
    return states
def city():
    combo_city = combobox
    if states():
        combo_city['values'] = (list_cidades)
        combo_city.current(0)
        combo_city.place(width=701, height=86, x=909, y=502)
        city = combo_city.get()
        return city
    else:
        print("None")
def categoria():
    combo_categoria = combobox
    combo_categoria['values'] = (list_cadegory)
    combo_categoria.current(0)
    combo_categoria.place(width=700, height=87, x=96, y=361)
    categoria = combo_categoria.get()
    return categoria


def clique_esquerdo_mouse(arg):
    global flag, x1, y1
    flag = not flag

    if flag:
        x1 = arg.x
        y1 = arg.y

    else:
        print(f'width={arg.x - x1}, height={arg.y - y1}, x={x1}, y={y1}')

#create buttons
nome_piloto = Entry(master, text="NOME DO PILOTO", font="Arial 30", justify=CENTER)
categoria = Button(master, text="CATEGORIA", command=categoria, font="Arial 50", justify=CENTER)
idade = Entry(master, text="IDADE", font="Arial 30", justify=CENTER)
cidade = Button(master, text="CIDADE", font="Arial 30", command=city, justify=CENTER)
estado = Button(master, text="ESTADO", font="Arial 30", command=states, justify=CENTER)
placa = Entry(master, text="PLACA", font="Arial 30", justify=CENTER)
button_cadastro = Button(master, text="CADASTRAR", command=categoria, font="Arial 30")
button_elite = Button(master, text="ELITE-MAN", font="Arial 30")

#positions buttons
nome_piloto.place(width=1516, height=84, x=96, y=244)
categoria.place(width=700, height=87, x=96, y=361)
idade.place(width=699, height=85, x=911, y=363)
cidade.place(width=700, height=84, x=96, y=503)
estado.place(width=701, height=86, x=909, y=502)
placa.place(width=679, height=67, x=500, y=613)
button_cadastro.place(width=699, height=144, x=496, y=709)
button_elite.place(width=267, height=72, x=1321, y=677)




#combo_box



#global variables
flag = x1 = y1 = x = 0

#eventos
master.bind("<Button-1>", clique_esquerdo_mouse)
master.mainloop()