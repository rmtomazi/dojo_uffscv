import cv2
import numpy as np
import matplotlib as mpl
mpl.use('TkAgg')
import matplotlib.pyplot as plt

#Pegar os tempos de abertura de câmera
times = np.array([1/30, 0.25, 2.5, 15.0], dtype = np.float32)

filenames = ["img_0.033.jpg", "img_0.25.jpg", "img_2.5.jpg", "img_15.jpg"]
images = []
hdr = []

#Importando as Imagens
for filename in filenames:
    img = cv2.imread("images/" + filename)
    images.append(img)

print("Alinhando a mediada do limite de bitmaps")
alignMTB = cv2.createAlignMTB()
alignMTB.process(images, images)

print("Calibrando CRF")
calibrateDebevec = cv2.createCalibrateDebevec()
responseDevec = calibrateDebevec.process(images, times)

print("Unindo as  Imagens")
mergeDevec = cv2.createMergeDebevec()
hdrDevec = mergeDevec.process(images, times, responseDevec
)

# Metodos de HDR
# Drago
print("Gerando HDR Drago")
tonemapDrago = cv2.createTonemapDrago(1.0, 0.7)
hdrDrago = tonemapDrago.process(hdrDevec)
hdrDrago = 3 * hdrDrago
hdrDrago = hdrDrago * 255

cv2.imwrite("images/hdrDrago.jpg", hdrDrago)
hdr.append(hdrDrago)

# Durand
print("Gerando HDR Durand")
tonemapDurand = cv2.createTonemapDurand(1.4, 4, 1.0, 1, 1)
hdrDurand = tonemapDurand.process(hdrDevec)
hdrDurand = 3 * hdrDurand
hdrDurand = 255 * hdrDurand

cv2.imwrite("images/hdrDurand.jpg", hdrDurand)
hdr.append(hdrDurand)

# Reinhard
print("Gerando HDR Reinhard")
tonemapReinhard = cv2.createTonemapReinhard(1.5, 0, 0, 0)
hdrReinhard = tonemapReinhard.process(hdrDevec)
hdrReinhard = 255 * hdrReinhard

cv2.imwrite("images/hdrReinhard.jpg", hdrReinhard)
hdr.append(hdrReinhard)

# Mantiuk
print("Gerando HDR Mantiuk")
tonemapMantiuk = cv2.createTonemapMantiuk(2.2, 0.85, 1.2)
hdrMantiuk = tonemapMantiuk.process(hdrDevec)
hdrMantiuk = 255 * hdrMantiuk

cv2.imwrite("images/hdrMantiuk.jpg", hdrMantiuk)
hdr.append(hdrMantiuk)

fig=plt.figure(figsize=(10, 10))
fig.canvas.set_window_title("Imagens Capturadas")
columns,rows = 2, 2
times_labels = [ "0.033", "0.25", "2.5", "15.0" ]
for i in range(1, columns*rows +1):
    img = images[i-1]
    fig.add_subplot(rows, columns, i)
    plt.axis('off')
    plt.title("Exposição de {} segundos".format(times_labels[i-1]))

    plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))

plt.show()

# Resultados Finais
print("Gerando resultados Finais")
fig=plt.figure(figsize=(10, 10))
fig.canvas.set_window_title("Resultado da aplicação de HDR")
columns,rows = 2, 2
hdr_method = ["Draco","Durand","Reinhard","Matiuk"]
for i in range(1, columns*rows +1):
    img = hdr[i-1]
    fig.add_subplot(rows, columns, i)
    plt.axis('off')
    plt.title(hdr_method[i-1])

    plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB).astype(np.uint8))

plt.show()
