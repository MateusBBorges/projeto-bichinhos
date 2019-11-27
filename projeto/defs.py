import tkinter as tk
from bichinhos import main

def criaJanela ():
    arquivo = open("/home/mateusvld/aulas_programacao/aulas_algoritimo_programacao2/projeto/banco.txt", "r")
    for e in arquivo:
        if (e[0] == '#' or e[0] == '-' or e[0:4] == 'Nome'):
            pass
        else:
            j = e.split()
            nomeDog = j[0]
            name = {}
            name[nomeDog] = tk.Tk()
            name[nomeDog].geometry("700x400")
            name[nomeDog].title(nomeDog)
            name[nomeDog].configure(bg = "PaleTurquoise")

            name[nomeDog].mainloop()

    arquivo.close()


def checkDog(janelaAdicao, nome, idade, peso, vacina, local):
    a = 0

    if (nome.get() == ''):
        nome["background"]="Tomato"
    else:
        a += 1
        
    if (local.get() == ''):
        local["background"]="Tomato"
    else:
        a += 1

    if (a == 2):
        setDog(janelaAdicao, nome, idade, peso, vacina, local)
    else:
        pass

def setDog(janelaAdicao, nome, idade, peso, vacina, local):
    nome["background"]="White"
    local["background"]="White"
    
    arquivo = open("/home/mateusvld/aulas_programacao/aulas_algoritimo_programacao2/projeto/banco.txt", "r")
    conteudo = arquivo.readlines()

    j = conteudo[0]
    j = j.replace('#','')
    j = int(j)
    j += 1
    conteudo[0] = '#'+str(j)+'\n'

    conteudo.append("\n")
    conteudo.append(nome.get())
    conteudo.append(" | ")
    if idade.get()=='':
        conteudo.append('Nenhum')
        conteudo.append(" | ")
    else:
        conteudo.append(idade.get())
        conteudo.append(" | ")
    if peso.get() == '':
        conteudo.append('Nenhum')
        conteudo.append(" | ")
    else:
        conteudo.append(peso.get())
        conteudo.append(" | ")
    if vacina.get() == '':
        conteudo.append('Nenhuma')
        conteudo.append(" | ")
    else:
        conteudo.append(vacina.get())
        conteudo.append(" | ")
    conteudo.append(local.get())

    arquivo = open("/home/mateusvld/aulas_programacao/aulas_algoritimo_programacao2/projeto/banco.txt", "w")
    arquivo.writelines(conteudo)

    arquivo.close()

    nome.delete(0, 'end')
    idade.delete(0, 'end')
    peso.delete(0, 'end')
    vacina.delete(0, 'end')
    local.delete(0, 'end')

    lb1 = tk.Label (janelaAdicao, text = 'bichinho adicionado com sucesso!', bg = 'PaleTurquoise', fg = 'DarkBlue', font = "Times 15")
    lb1.place(x = 60, y = 300)

def kill_adicao(janelaAdicao):
    janelaAdicao.destroy()
    main()
    
def adicao(janelaPrincipal):
    janelaPrincipal.destroy()

    janelaAdicao = tk.Tk()
    janelaAdicao.geometry("700x400")
    janelaAdicao.title("ADICIONAR BICHINHOS")
    janelaAdicao.configure(bg = "PaleTurquoise")
    
    lb1 = tk.Label (janelaAdicao, text = '*Obrigatório ', bg = 'PaleTurquoise', fg = 'Red', font = "Times 11")
    lb1.place(x = 10, y = 10)
    
    lb2 = tk.Label (janelaAdicao, text = 'Digite o nome do bichinho: ', bg = 'PaleTurquoise', fg = 'DarkBlue', font = "Times 15")
    lb2.place(x = 60, y = 60)
    ast2 = tk.Label (janelaAdicao, text = '*', bg = 'PaleTurquoise', fg = 'Red', font = "Times 15")
    ast2.place(x = 290, y = 60)
    nome = tk.Entry(janelaAdicao)
    nome.place(x=320,y=60)
    nome["background"]="White"

    lb3 = tk.Label (janelaAdicao, text = 'Digite a idade do bichinho: ', bg = 'PaleTurquoise', fg = 'DarkBlue', font = "Times 15")
    lb3.place(x = 60, y = 90)
    idade = tk.Entry(janelaAdicao)
    idade.place(x=320,y=90)
    idade["background"]="White"

    lb4 = tk.Label (janelaAdicao, text = 'Digite o peso do bichinho: ', bg = 'PaleTurquoise', fg = 'DarkBlue', font = "Times 15")
    lb4.place(x = 60, y = 120)
    peso = tk.Entry(janelaAdicao)
    peso.place(x=320,y=120)
    peso["background"]="White"

    lb5 = tk.Label (janelaAdicao, text = 'Digite as vacinas do bichinho: ', bg = 'PaleTurquoise', fg = 'DarkBlue', font = "Times 15")
    lb5.place(x = 60, y = 150)
    vacina = tk.Entry(janelaAdicao)
    vacina.place(x=320,y=150)
    vacina["background"]="White"

    lb6 = tk.Label (janelaAdicao, text = 'Digite o local do bichinho: ', bg = 'PaleTurquoise', fg = 'DarkBlue', font = "Times 15")
    lb6.place(x = 60, y = 180)
    ast6 = tk.Label (janelaAdicao, text = '*', bg = 'PaleTurquoise', fg = 'Red', font = "Times 15")
    ast6.place(x = 290, y = 180)
    local = tk.Entry(janelaAdicao)
    local.place(x=320,y=180)
    local["background"]="White"

    adicionar = tk.Button(janelaAdicao, text = 'Adicionar', bg = 'DarkBlue', fg = 'White', command = lambda: checkDog(janelaAdicao, nome, idade, peso, vacina, local))
    adicionar.place (x = 600, y = 360)

    voltar = tk.Button(janelaAdicao, text = 'Voltar', bg = 'DarkBlue', fg = 'White', command = lambda: kill_adicao(janelaAdicao))
    voltar.place (x = 10, y = 360)

    janelaAdicao.mainloop()

def kill_adocao(janelaAdocao):
    janelaAdocao.destroy()
    main()

def adocao(janelaPrincipal):
    janelaPrincipal.destroy()

    arquivo = open("/home/mateusvld/aulas_programacao/aulas_algoritimo_programacao2/projeto/banco.txt", "r")
    busca = '#'
    for e in arquivo:
        if busca in e:
            qtdDogs = e
            qtdDogs = qtdDogs.replace('#','')

    arquivo.close()

    janelaAdocao = tk.Tk()
    janelaAdocao.geometry("700x400")
    janelaAdocao.title("ADOTAR BICHINHOS")
    janelaAdocao.configure(bg = "PaleTurquoise")

    lb1 = tk.Label (janelaAdocao, text = 'Bichinhos para adoção: '+str(qtdDogs), bg = 'PaleTurquoise', fg = 'DarkBlue', font = "Times 15")
    lb1.place(x = 60, y = 50)
    lb2 = tk.Label (janelaAdocao, text = 'Leve um bichinho para casa!!!\nPara adotar clique no botão abaixo:',justify = 'left', bg = 'PaleTurquoise', fg = 'DarkBlue', font = "Times 15")
    lb2.place(x = 60, y = 100)

    adote = tk.Button(janelaAdocao, text = 'Adotar', bg = 'DarkBlue', fg = 'White', command = criaJanela)
    adote.place (x = 170, y = 190)

    im1 = tk.PhotoImage(file = '/home/mateusvld/aulas_programacao/aulas_algoritimo_programacao2/projeto/images/penoso.png')
    imagem1 = im1.subsample(2, 2)
    lbimagem1 = tk.Label(janelaAdocao, image = imagem1)
    lbimagem1.place(x = 370, y = 50)

    voltar = tk.Button(janelaAdocao, text = 'Voltar', bg = 'DarkBlue', fg = 'White', command = lambda: kill_adocao(janelaAdocao))
    voltar.place (x = 10, y = 360)

    janelaAdocao.mainloop()