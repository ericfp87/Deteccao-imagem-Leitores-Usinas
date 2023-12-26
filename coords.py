import cv2

image = cv2.imread("C//Users//EricFerreira//Downloads//Imagens//example.png")
cv2.imshow("Imagem", image)
roi = cv2.selectROI("Imagem", image, fromCenter=False, showCrosshair=True)

print("Coordenadas da ROI: ", roi)
cv2.waitKey(0)
