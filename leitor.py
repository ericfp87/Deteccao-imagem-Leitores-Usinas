import os
import datetime
from PIL import Image
import pytesseract
import openpyxl


pytesseract.pytesseract.tesseract_cmd = 'C:/Program Files/Tesseract-OCR/tesseract.exe' 

pasta_principal = r'C:\Users\EricFerreira\Downloads\Imagens'
pasta_excel = r'C:\Users\EricFerreira\Downloads'


nome_arquivo_excel = os.path.join(pasta_excel, 'numeros_imagens.xlsx')
workbook = openpyxl.Workbook()
worksheet = workbook.active
worksheet.title = 'Numeros'


for pasta, subpastas, arquivos in os.walk(pasta_principal):
    
    for arquivo in arquivos:
        if arquivo.endswith('.jpg') or arquivo.endswith('.png') or arquivo.endswith('.jpeg'):
            
            caminho_arquivo = os.path.join(pasta, arquivo)
            imagem = Image.open(caminho_arquivo)
            numeros = pytesseract.image_to_string(imagem, lang='eng', config='--psm 6')

            
            nome_subpasta = os.path.basename(pasta)
            data_hora = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            linha = [nome_subpasta, data_hora, arquivo, numeros]
            worksheet.append(linha)


workbook.save(nome_arquivo_excel)
