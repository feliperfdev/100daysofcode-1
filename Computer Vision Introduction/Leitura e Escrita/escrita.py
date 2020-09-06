import cv2
import matplotlib.pyplot as plt

imagem = cv2.imread('Computer Vision Introduction/imagem2.jpg', 0)
# Passando como segundo argumento o '0', colocamos a imagem em escala de cinza

altura = imagem.shape[0]
largura = imagem.shape[1]

porcentagem = 20
nova_altura = int(altura*porcentagem/100)
nova_largura = int(largura*porcentagem/100)

dimensoes = (nova_largura, nova_altura)

imagem_reduzida = cv2.resize(imagem, dimensoes, interpolation=cv2.INTER_AREA)

cv2.imwrite('imagem2_cinza.png', imagem_reduzida)