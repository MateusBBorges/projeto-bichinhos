import tkinter as tk
import defs

def main():

    janelaPrincipal = tk.Tk()
    janelaPrincipal.geometry("700x400")
    janelaPrincipal.title("ADOTE BICHINHOS")
    janelaPrincipal.configure(bg="PaleTurquoise")

    lb1 = tk.Label (janelaPrincipal, text = 'Adote um Bichinho', bg = 'PaleTurquoise', fg = 'DarkBlue', font = "Times 20 bold")
    lb1.place(x = 230, y = 10)

    lb2 = tk.Label (janelaPrincipal, text = 'Clique aqui para \nadicionar um novo bichinho:', bg = 'PaleTurquoise', fg = 'DarkBlue', font = "Times 11")
    lb2.place(x = 70, y = 60)

    adicionar = tk.Button(janelaPrincipal, text = 'Clique', bg = 'DarkBlue', fg = 'White', command =lambda: defs.adicao(janelaPrincipal))
    adicionar.place (x = 120, y = 100)

    im1 = tk.PhotoImage(file = '/home/mateusvld/aulas_programacao/aulas_algoritimo_programacao2/projeto/images/adicionar.png')
    imagem1 = im1.subsample(5, 5)
    lbimagem1 = tk.Label(janelaPrincipal, image = imagem1)
    lbimagem1.place(x = 50, y = 150)

    lb3 = tk.Label (janelaPrincipal, text = 'Clique aqui para \nadotar seu novo bichinho:', bg = 'PaleTurquoise', fg = 'DarkBlue', font = "Times 11")
    lb3.place(x = 457, y = 60)

    adotar = tk.Button(janelaPrincipal, text = 'Clique', bg = 'DarkBlue', fg = 'White', command =lambda: defs.adocao(janelaPrincipal))
    adotar.place (x = 500, y = 100)

    im2 = tk.PhotoImage(file = '/home/mateusvld/aulas_programacao/aulas_algoritimo_programacao2/projeto/images/pets.png')
    imagem2 = im2.subsample(5, 5)
    lbimagem2 = tk.Label(janelaPrincipal, image = imagem2)
    lbimagem2.place(x = 430, y = 150)  

    janelaPrincipal.mainloop()

if __name__ == "__main__":
    main()