import cv2
import numpy

imagem = cv2.imread('imagem3.png')
matriz = (15,15)

#================================================================================================
altura = imagem.shape[0] # pega o valor da altura
largura = imagem.shape[1] # pega o valor da largura

porcentagem = 30
nova_altura = int(altura*porcentagem/100)
nova_largura = int(largura*porcentagem/100)

dimensoes = (nova_largura, nova_altura)

imagem_reduzida = cv2.resize(imagem, dimensoes, interpolation=cv2.INTER_AREA)
#================================================================================================

imagem_blur = cv2.GaussianBlur(imagem_reduzida, matriz, 0)
cv2.imshow('Gaussian', imagem_blur)
cv2.waitKey(0)
cv2.destroyAllWindows()