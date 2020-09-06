import numpy as np
import cv2 as cv
from matplotlib import pyplot as plt

img = cv.imread('imagem2.png',0)

#================================================================================================
altura = img.shape[0] # pega o valor da altura
largura = img.shape[1] # pega o valor da largura

porcentagem = 40
nova_altura = int(altura*porcentagem/100) # 800
nova_largura = int(largura*porcentagem/100) # 800

print(f'Altura: {nova_altura}\nLargura: {nova_largura}')

dimensoes = (nova_largura, nova_altura)

imagem_reduzida = cv.resize(img, dimensoes, interpolation=cv.INTER_AREA)
#================================================================================================

#cv.rectangle(imagem_reduzida, (100,100), (200,200), (135,100,0),30, lineType=8, shift=0)

cv.putText(imagem_reduzida, 'Texto Felipe', (300, 70), cv.FONT_HERSHEY_COMPLEX, 1.4, 
(0, 0, 0), thickness=3)
# cor preta --> (0, 0, 0)

cv.imshow('Imagem', imagem_reduzida)
plt.hist(imagem_reduzida.ravel(),256,[0,256])
plt.title('Histograma Escalas de Cinza')
plt.show()
cv.waitKey(0)
cv.destroyAllWindows()