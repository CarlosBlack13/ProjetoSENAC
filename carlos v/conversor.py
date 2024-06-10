from tkinter import Tk, ttk, Frame, Label, Entry, Button, NSEW, messagebox
#from PIL import ImageTk, Image  # Pillow
import requests


# Cores
cores_um = "#FFFFFF" # Cor: Branco
cores_dois = "#333333"
cores_tres = "#38576b"

class ConverterApp:
    def __init__(self, main):
        self.main = main
        self.main.title('Conversor')
        self.main.configure(bg=cores_um)
        self.main.resizable(width=False, height=False)

        style = ttk.Style(self.main)
        style.theme_use('clam')

        # Cria os widgets da aplicação
        self.create_widgets()
        # Centraliza a janela na tela
        self.center_window()

    def create_widgets(self):
        # Cria os frames para organizar os componentes
        self.frame_header = Frame(self.main, width=300, height=60, padx=0, pady=0, bg=cores_tres, relief='flat')
        self.frame_header.grid(row=0, column=0, columnspan=2)

        self.frame_footer = Frame(self.main, width=300, height=260, padx=0, pady=5, bg=cores_um, relief='flat')
        self.frame_footer.grid(row=1, column=0, columnspan=2, sticky=NSEW)

        # Configuração do label para exibir o resultado
        self.app_resultado = Label(self.frame_footer, text='', width=16, height=2, relief='solid', anchor='center',
                                   font=('Ivy 15 bold'), bg=cores_um, fg=cores_dois)
        self.app_resultado.place(x=50, y=10)

        # Cria as comboboxes para selecionar as moedas
        self.create_comboboxes()
        # Cria o campo de entrada para o valor a ser convertido
        self.create_entry()
        # Cria o botão de conversão
        self.create_button()

    def create_comboboxes(self):
        self.tipo_moeda = ['USD', 'BRL', 'EUR', 'CAD', 'AUD', 'CHF', 'JPY', 'RUB', 'INR', 'AOA']

        # Label e combobox para selecionar a moeda de origem
        self.app_de = Label(self.frame_footer, text='De:', width=8, height=1, relief='flat', anchor='nw',
                            font=("Ivy 10 bold"), bg=cores_um, fg=cores_dois)
        self.app_de.place(x=48, y=90)

        self.box_de = ttk.Combobox(self.frame_footer, width=8, justify='center', font=("Ivy 12 bold"))
        self.box_de.place(x=50, y=115)
        self.box_de['values'] = self.tipo_moeda

        # Label e combobox para selecionar a moeda de destino
        self.app_para = Label(self.frame_footer, text='Para:', width=8, height=1, relief='flat', anchor='nw',
                              font=("Ivy 10 bold"), bg=cores_um, fg=cores_dois)
        self.app_para.place(x=158, y=90)

        self.box_para = ttk.Combobox(self.frame_footer, width=8, justify='center', font=('Ivy 12 bold'))
        self.box_para.place(x=160, y=115)
        self.box_para['values'] = self.tipo_moeda

    def create_entry(self):
        # Campo de entrada para o valor a ser convertido
        self.valor =  Label(self.frame_footer, text = 'Digite o valor', bg = cores_um)
        self.valor.place(x = 50, y = 142)                           
        self.valor = Entry(self.frame_footer, width=22, justify='center', font=('Ivy 12 bold'), relief='solid')
        self.valor.place(x=50, y=160)

    def create_button(self):
        # Botão para iniciar a conversão
        self.botao = Button(self.frame_footer, command=self.converter, text='Converter', width=19, padx=5, height=1,
                            bg=cores_tres, fg=cores_um, font=('Ivy 12 bold'), relief='raised', overrelief='ridge')
        self.botao.place(x=50, y=210)

    def converter(self):
        try:
            # Obtém as moedas e o valor a ser convertido
            moeda_de = self.box_de.get()
            moeda_para = self.box_para.get()
            valor_entrada = float(self.valor.get())

            # Faz a requisição à API para obter a taxa de câmbio
            response = requests.get(f'https://api.exchangerate-api.com/v4/latest/{moeda_de}')
            cambio = response.json()['rates'][moeda_para]

            # Calcula o valor convertido
            resultado = valor_entrada * float(cambio)
            dict_moedas = {
                'USD': '$',
                'BRL': 'R$',
                'EUR': '€',
                'CAD': 'C$',
                'AUD': 'A$',
                'CHF': 'Fr',
                'JPY': '¥',
                'RUB': 'RUB',
                'INR': '₹',
                'AOA': 'Kz'
            }

            simbolo = dict_moedas[moeda_para]
            self.valor.delete(0, "end")

            # Formata o resultado no padrão brasileiro
            moeda_equivalente = simbolo + '{:_.2f}'.format(resultado)
            self.app_resultado['text'] = moeda_equivalente.replace('.', ',').replace('_', '.')

        except Exception as e:
            messagebox.showerror('Erro!', 'Verifique sua conexão com a internet e preencha todos os campos')
            print(e)

    def center_window(self):
        # Centraliza a janela na tela
        largura = 300
        altura = 320

        largura_screen = self.main.winfo_screenwidth()
        altura_screen = self.main.winfo_screenheight()

        posx = largura_screen / 2 - largura / 1.8
        posy = altura_screen / 5 - altura / 5

        self.main.geometry(f"{largura}x{altura}+{int(posx)}+{int(posy)}")

if __name__ == "__main__":
    root = Tk()
    app = ConverterApp(root)
    root.mainloop()