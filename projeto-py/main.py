import os 
from tkinter.filedialog import askdirectory 

## aq para escolher a pasta
caminho = askdirectory(title="selecione uma pasta")
## o print foi usado p testar o funcionamento por partes
##print(caminho)

##aq vai exibir os tipos dos arquivos
lista_arqv = os.listdir(caminho)
##print(lista_arqv)

## aq vai servir como uma especie de "dicionario" as extensões
locais = {
    "imagens": [".png", ".jpg", ".jpeg"],
    "planilhas": [".xlsx", ".xlsm"],
    "pdfs": [".pdf"],
    "csv": [".csv"],
}

for arquivo in lista_arqv:
    #01 arquvivo pdf
    nome, extensao = os.path.splitext(f"{caminho}/{arquivo}")
    for pasta in locais:
        if extensao in locais[pasta]:
            if not os.path.exists(f"{caminho}/{pasta}"):
                os.mkdir(f"{caminho}/{pasta}")
            os.rename(f"{caminho}/{arquivo}", f"{caminho}/{pasta}/{arquivo}") 

## a var pasta é composta basicamente por img, planilhas, pdfs, csv
