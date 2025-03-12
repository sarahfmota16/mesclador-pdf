import PyPDF2 #biblioteca de pdf
import os #biblioteca para leitura de arquivos

merger = PyPDF2.PdfMerger() #criei um mesclador de pdf

lista_arquivos = os.listdir("arquivos")
lista_arquivos.sort()
print(lista_arquivos)

for arquivo in lista_arquivos: #verificar se todos os arquivos mesclados serão pdf
    if ".pdf" in arquivo: #se o houver um arquivo pdf
        merger.append(f"arquivos/{arquivo}") #então ele será adicionado ao mesclador

merger.write("Poemas.pdf") #criei um arquivo pdf que terá todos os pdf da pasta mesclados
