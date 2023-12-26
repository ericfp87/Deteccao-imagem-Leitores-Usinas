import cv2
import pytesseract
import numpy as np
import argparse

# Argumentos de linha de comando
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image C:\\Users\\EricFerreira\\Downloads\\Imagens\\example.jpeg", required=True, help="caminho da imagem de entrada")
ap.add_argument("-r", "--roi", nargs='+', type=int, default=[100, 100, 200, 50], help="região de interesse (x y largura altura)")
args = vars(ap.parse_args())

# Carregue a imagem de entrada e defina a região de interesse
img = cv2.imread("C:\\Users\\EricFerreira\\Downloads\\Imagens\\example.jpeg")
roi = args["roi"]
if roi is not None:
    x, y, w, h = roi
    img = img[y:y+h, x:x+w]

# Converta a imagem para tons de cinza e aplique a operação de limiarização
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
_, thresh = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY_INV+cv2.THRESH_OTSU)

# Encontre os contornos dos números na imagem limiarizada e extraia as regiões correspondentes
contours, hierarchy = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
rois = []
for cnt in contours:
    x, y, w, h = cv2.boundingRect(cnt)
    roi = img[y:y+h, x:x+w]
    rois.append(roi)

# Use a biblioteca PyTesseract para extrair o texto dos números de cada região extraída
numbers = []
for roi in rois:
    text = pytesseract.image_to_string(roi, config='--psm 6 outputbase digits')
    numbers.append(text)

# Imprima os números detectados no terminal
print("Números detectados:", numbers)
