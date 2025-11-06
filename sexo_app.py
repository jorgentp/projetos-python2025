from tkinter import *
def selecao_sexo1():
    texto_orient.config(text="Você é mulher")
def selecao_sexo2():
    texto_orient.config(text="Você é homem")

janela = Tk()
janela.title("Seleção de Sexo")

texto_orient = Label(janela, text ="Clique nos botões abaixo (M) ou (F)")
texto_orient.grid(column=0, row=0, padx=60, pady = 20)

botao = Button(janela, text="Clique aqui se você é Mulher", command=selecao_sexo1)
botao2 = Button(janela, text="Clique aqui se você é Homem", command=selecao_sexo2)

botao.grid(column=0, row=1, padx= 60, pady = 10)
botao2.grid(column= 0, row=2, padx = 60, pady = 10)

texto_orient2 = Label(janela, text ="")
texto_orient2.grid(column=0, row=3, padx=15, pady = 20)

janela.mainloop()