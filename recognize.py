import os
import cv2
import pytesseract

# Defina as coordenadas da ROI
x1, y1, x2, y2 = 100, 100, 500, 300

# Defina o caminho da pasta que contém as subpastas com as imagens
base_path = "C:\\Users\\EricFerreira\\Downloads\\Imagens"

# Percorra todas as subpastas e obtenha o caminho de todas as imagens
images = []
for folder in os.listdir(base_path):
    folder_path = os.path.join(base_path, folder)
    if os.path.isdir(folder_path):
        for filename in os.listdir(folder_path):
            if filename.endswith(".jpg"):
                images.append(os.path.join(folder_path, filename))

# Crie um arquivo CSV para armazenar os números detectados
with open("detected_numbers.csv", "w") as f:
    f.write("image_name,x,y,number\n")
    
    # Percorra a lista de imagens e detecte os números na ROI de cada imagem
    for img_path in images:
        # Leia a imagem e selecione a ROI
        img = cv2.imread(img_path)
        roi = img[y1:y2, x1:x2]
        
        # Converta a ROI para escala de cinza e aplique um limiar
        gray = cv2.cvtColor(roi, cv2.COLOR_BGR2GRAY)
        _, thresh = cv2.threshold(gray, 120, 255, cv2.THRESH_BINARY)
        
        # Encontre os contornos na ROI e salve as informações do número detectado no arquivo CSV
        contours, _ = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
        for cnt in contours:
            x, y, w, h = cv2.boundingRect(cnt)
            number = gray[y:y+h, x:x+w]
            number_str = pytesseract.image_to_string(number, config='--psm 10 --oem 3 -c tessedit_char_whitelist=0123456789')
            f.write(f"{os.path.basename(img_path)},{x},{y},{number_str}\n")
            
        # Mostre a imagem com os números detectados
        cv2.imshow("Detected numbers", roi)
        cv2.waitKey(0)
        
cv2.destroyAllWindows()
