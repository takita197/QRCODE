#Importação das bibliotecas
import tkinter as tk
from tkinter import filedialog, messagebox
import qrcode

#codigo do qr code

def gerar_qrcode():
    texto = entrada.get()
    nome_arquivo = entrada_arquivo.get()
    if not nome_arquivo.endswith(".png"):
        nome_arquivo +=".png"
    img = qrcode.make(texto)
    img.save(nome_arquivo)
    messagebox.showinfo('Sucesso',"Imagem criada com sucesso!")

#interface do programa

janela = tk.Tk()
janela.title ("Gerador de QR Code")

#rótulo

tk.Label(janela, text="Escreva o conteudo aqui", font=("Arial", 14, "bold")).pack(pady=5)
entrada = tk.Entry(janela, width=40)
entrada.pack(pady=5)

tk.Label(janela, text="Escreva o nome do arquivo aqui", font=("Arial", 14, "bold")).pack(pady=5)
entrada_arquivo = tk.Entry(janela, width=40)
entrada_arquivo.pack(pady=5)

#botão

tk.Button(janela, text="Gerar", command=gerar_qrcode).pack(pady=10)

janela.mainloop()
