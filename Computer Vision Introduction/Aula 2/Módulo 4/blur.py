# Ajuda a presentar as bordas
# https://docs.opencv.org/master/d4/d13/tutorial_py_filtering.html
import cv2
import numpy

imagem = cv2.imread('clateste.jpg')
dimention = 21
color = 70
space = 10

#================================================================================================
altura = imagem.shape[0] # pega o valor da altura
largura = imagem.shape[1] # pega o valor da largura

porcentagem = 40
nova_altura = int(altura*porcentagem/100)
nova_largura = int(largura*porcentagem/100)

dimensoes = (nova_largura, nova_altura)

imagem_reduzida = cv2.resize(imagem, dimensoes, interpolation=cv2.INTER_AREA)
#================================================================================================

imagem_blur = cv2.bilateralFilter(imagem_reduzida, dimention, color, space)

cv2.imshow('Bilateral', imagem_blur)
cv2.waitKey(0)
cv2.destroyAllWindows()