import cv2
import numpy as np

imagem = cv2.imread('imagem2.png')

#==============================================================================================
altura = imagem.shape[0]
largura = imagem.shape[1]

porcentagem = 30
nova_altura = int(altura*porcentagem/100)
nova_largura = int(largura*porcentagem/100)

dimensoes = (nova_largura, nova_altura)

imagem_reduzida = cv2.resize(imagem, dimensoes, interpolation=cv2.INTER_AREA)
#==============================================================================================

centro = (nova_largura/2,nova_altura/2)
angulo = 90
print(nova_largura)
print(nova_altura)
# mudar para negativo e mostrar o oposto ocorrendo
imagem_rotacao = cv2.warpAffine(imagem_reduzida, 
cv2.getRotationMatrix2D(centro, angulo,1), (nova_largura,nova_altura))
#imagem_deslocada = cv2.warpAffine(imagem, np.float32([[1,0,-150],[0,1,-70]]), (colunas,linhas))

cv2.imshow('Rotacao', imagem_rotacao)
cv2.waitKey(0)
cv2.destroyAllWindows()