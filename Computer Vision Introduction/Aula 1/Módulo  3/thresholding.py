import cv2
import numpy as numpy

imagem = cv2.imread('imagem2.png',0)

#==============================================================================================
altura = imagem.shape[0]
largura = imagem.shape[1]

porcentagem = 30
nova_altura = int(altura*porcentagem/100)
nova_largura = int(largura*porcentagem/100)

dimensoes = (nova_largura, nova_altura)

imagem_reduzida = cv2.resize(imagem, dimensoes, interpolation=cv2.INTER_AREA)
#==============================================================================================

threshold = 100
(T_value,binarythreshold) = cv2.threshold(imagem_reduzida, threshold, 255, cv2.THRESH_BINARY)
cv2.imshow('Binaria', binarythreshold)
cv2.waitKey(0)
cv2.destroyAllWindows()