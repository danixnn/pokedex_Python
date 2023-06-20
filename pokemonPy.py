import requests
from tkinter import *
from tkhtmlview import HTMLLabel

def funcBotao():
    pokemon = pesquisa.get()
    api = f'https://pokeapi.co/api/v2/pokemon/{pokemon}'

    res = requests.get(api)
    pokemon = res.json()  # tratamos como dic

    nomepoke = Label(janela, text=(pokemon['name']))
    nomepoke.place(x=225, y=25)

    my_label = HTMLLabel(janela,html=f"<img src = '{pokemon['sprites']['front_default']}'>")
    my_label.pack(pady=200, padx=200)

    tp = Label(janela, text="Tipo")
    tp.place(x=50, y=325)

    b = ""
    for i in pokemon['types']:
        a = i['type']['name']
        b = b + a + " "

    movs = Label(janela, text=(b))
    movs.place(x=50, y=350)

def tipo(pokemon):
    for i in pokemon['types']:
        print(i['type']['name'])

if __name__ == "__main__":

    janela = Tk()
    janela.title("Pokedex")
    janela.geometry("500x500")

    pesquisa = Entry(janela)
    pesquisa.place(width = 200, height= 20, x = 125, y = 5)

    botaoPesquisa = Button(janela, text="Pesquisar", command= funcBotao)
    botaoPesquisa.place(x = 370,y =5,width = 100, height = 20)

    janela.mainloop()
