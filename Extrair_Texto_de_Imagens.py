import pytesseract
import cv2
from tkinter import filedialog
from tkinter import *

# Caminho de instalação do Tesseract
caminho_tesseract = r'C:\Users\joaoh\AppData\Local\Tesseract-OCR\tesseract.exe'

# Função da extração da imagem em texto
def imagem_texto():
    # Seleção do arquivo e definição do tipo
    nome_arquivo = filedialog.askopenfilename(initialdir="/", title="Selecione uma imagem",
    filetypes=(('Arquivo de imagem','*.jpg*'),('Arquivo de imagem','*.jpeg*'),('Arquivo de imagem','*.png*'),('Todos arquivos','*.*')))
    arquivo_caminho.configure(text=nome_arquivo)
    # Variável em que recebe o caminho completo do arquivo
    imagem_caminho = arquivo_caminho['text']
    print('Caminho da imagem: {}' .format(imagem_caminho))
    # Ler imagem
    imagem = cv2.imread(f'{imagem_caminho}')
    # Extrair o texto da imagem
    pytesseract.pytesseract.tesseract_cmd = caminho_tesseract
    texto = pytesseract.image_to_string(imagem, lang='por')
    texto_label = 'Texto salvo na pasta do programa.'
    # Extrair texto para TXT
    with open("Texto_Imagem.txt", "w") as arquivo:
        arquivo.write(texto)
    print(texto)
    texto_app['text'] = texto_label

# Configuração da GUI
app = Tk()
app.title('Extrair Texto de Imagens')
app.geometry('400x300')
Label(app, text='Selecione a Imagem:').grid(column=0, row=0, padx=10, pady=10)
Button(app, text='Carregar Imagem e Converter', command=imagem_texto).grid(column=0, row=1, padx=10, pady=10)

# Variáveis dos Label
arquivo_caminho = Label(app, text='')
arquivo_caminho.grid(column=0, row=2,padx=10, pady=10)
texto_app = Label(app, text='')
texto_app.grid(column=0, row=3,padx=10, pady=10)

app.mainloop()




