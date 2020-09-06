# Ajuda a presentar as bordas
# https://docs.opencv.org/master/d4/d13/tutorial_py_filtering.html
import cv2 as cv
import numpy

img = cv.imread('imagem3.png')
dimention = 15
color = 90
space = 100

#================================================================================================
altura = img.shape[0] # pega o valor da altura
largura = img.shape[1] # pega o valor da largura

porcentagem = 35
nova_altura = int(altura*porcentagem/100)
nova_largura = int(largura*porcentagem/100)

dimensoes = (nova_largura, nova_altura)

imagem_reduzida = cv.resize(img, dimensoes, interpolation=cv.INTER_AREA)
#================================================================================================

imagem_blur = cv.bilateralFilter(imagem_reduzida, dimention, color, space)

cv.imshow('Bilateral', imagem_blur)
cv.waitKey(0)
cv.destroyAllWindows()