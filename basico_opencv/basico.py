# Importar a bibliotéca do OpenCV
import cv2

# Importar uma imagem
img_COR = cv2.imread("images/img.jpg")
img_PB  = cv2.imread("images/img.jpg", 0)

# Salvar uma imagem
cv2.imwrite("images/saved.jpg", img_COR)

# Plotar com OpenCV
cv2.imshow("imagem", img_COR)
cv2.waitKey(0)
cv2.destroyAllWindows()

# Rotação
linhas,colunas = img_PB.shape

angulo = 90
centro_de_rotacao = (colunas/2,linhas/2)
escala = 1

rotacao = cv2.getRotationMatrix2D(centro_de_rotacao, angulo, escala)
rotacionado = cv2.warpAffine(img_PB, rotacao, (colunas, linhas))

cv2.imshow("rotacionada", rotacionado);
cv2.waitKey(0)
cv2.destroyAllWindows()

# Inter imagem vertical e horizontal
inverte_horizontal = cv2.flip(img_COR, 1)
inverte_vertical = cv2.flip(img_PB, 0)

cv2.imshow("horizontal", inverte_horizontal)
cv2.waitKey(0)
cv2.destroyAllWindows()

cv2.imshow("vertical", inverte_vertical)
cv2.waitKey(0)
cv2.destroyAllWindows()
