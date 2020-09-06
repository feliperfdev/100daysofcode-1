import numpy as np
import cv2 as cv
from matplotlib import pyplot as plt


img = cv.imread('clateste.jpg')

#================================================================================================
altura = img.shape[0] # pega o valor da altura
largura = img.shape[1] # pega o valor da largura

porcentagem = 30
nova_altura = int(altura*porcentagem/100)
nova_largura = int(largura*porcentagem/100)

dimensoes = (nova_largura, nova_altura)

imagem_reduzida = cv.resize(img, dimensoes, interpolation=cv.INTER_AREA)
#================================================================================================
#        [0,  1,  2]
color = ('b','g','r')

for i,col in enumerate(color):
    histr = cv.calcHist([imagem_reduzida],[i],None,[256],[0,256])
    plt.plot(histr,color = col)
    plt.xlim([0,256])
plt.hist(imagem_reduzida.ravel(),256,[0,256]) # plota o histograma resultado da soma dos valores BGR
#... da imagem

#================================================================================================
'''
for i in range(3):
    histr = cv.calcHist([imagem_reduzida],[i],None,[256],[0,256])
    plt.plot(histr,color = 'black')
    plt.xlim([0,256])
    plt.show()
'''
#================================================================================================

cv.imshow('Imagem', imagem_reduzida)
plt.title('Histograma Escala BGR -> Blue, Green, Red')
plt.show()
cv.waitKey(0)
cv.destroyAllWindows()