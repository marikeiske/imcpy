from tkinter import *
from tkinter import messagebox 

tela = Tk()

tela.geometry("500x500")
tela.title("Tela Principal")
tela.config(background= "#154360")

peso = StringVar()
altura = StringVar()

def Calcular ():
    print("calculando")
    a = float(altura.get())
    p = float(peso.get())
    imc = p / (a*a)
    print(imc)
    messagebox.showinfo("Mensagem", imc)



LbTitle = Label(tela, text= " IMC 3.0 \n", font= "Bold 30", background= "#154360", foreground= "white")
caixaNome1 =  Entry(tela, textvariable= peso)

LbAsk = Label(tela, text= " Digite a sua altura: \n", font= "Bold 11", background= "#154360", foreground= "white")
caixaNome2 =  Entry(tela, textvariable= altura)

LbTAskk = Label(tela,text = " Digite o seu peso: \n ", font= "Bold 11", background= "#154360", foreground= "white")
btnEnviar = Button (tela,command=Calcular, text= "Calcular", font= "Bold 11",background= "#34495E", foreground= "white", activebackground= "#1C2833",  textvariable= peso )


#btn2= Button(command=Calcular , text="Teste")
LbName = Label(tela, text= "\n \n By Mari 🔢", font= "Bold 11", background= "#154360", foreground= "white")

LbTitle.pack()

LbAsk.pack()
caixaNome1.pack()

LbTAskk.pack()
caixaNome2.pack()

btnEnviar.pack(pady= 20)

LbName.pack()
#btn2.pack()
tela.mainloop()