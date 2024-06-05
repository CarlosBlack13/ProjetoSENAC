###################################################################

# You need to install Tkinter and CustomTkinter to make it work

###################################################################

# É preciso instalar o Tkinter e o CustomTkinter para fazer funcionar

###################################################################

import customtkinter
import tkinter as tk
from tkinter import ttk


class Janela(customtkinter.CTk):
    customtkinter.set_appearance_mode("dark") #Altera a aparência da tela
    customtkinter.set_default_color_theme("dark-blue")
    
    #Cria a Janela
    janela = customtkinter.CTk()
    janela.geometry = ('600x600')

    #Cria o Nome de fazer o Login --------------------------------------------
    texto = customtkinter.CTkLabel(janela, text = 'Fazer Login')
    texto.pack(padx = 10, pady = 20)

    #Cria o E-mail --------------------------------------------
    email = customtkinter.CTkEntry(janela, placeholder_text = 'Seu E-mail')
    email.pack(padx = 10, pady = 20)

    #Cria o Senha --------------------------------------------
    senha = customtkinter.CTkEntry(janela, placeholder_text = 'Insira a senha', show = '*')
    senha.pack(padx = 10, pady = 20)

    #Cria o CheckBox --------------------------------------------
    checkbox = customtkinter.CTkCheckBox(janela, text = 'Lembrar Login')
    checkbox.pack(padx = 10, pady = 20)

    #Cria o Botão --------------------------------------------
    botão = customtkinter.CTkButton(janela, text = 'Login')
    botão.pack(padx = 10, pady = 20) 


















    janela.mainloop()