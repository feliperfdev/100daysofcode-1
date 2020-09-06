import cv2

import numpy as np

print(cv2.__version__)
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

cv2.imshow("Inicial", imagem_reduzida)
colunas = imagem.shape[1]
linhas = imagem.shape[0]
print(colunas)
print(linhas)


# mudar para negativo e mostrar o oposto ocorrendo
#imagem_deslocada = cv2.warpAffine(imagem, np.float32([[1,0,150],[0,1,70]]), (colunas,linhas))
imagem_deslocada = cv2.warpAffine(imagem_reduzida, np.float32([[1,0,-150],[0,1,-70]]), 
(colunas,linhas))

# * valores 1 e 0

cv2.imshow('Deslocada', imagem_deslocada)
cv2.waitKey(0)
cv2.destroyAllWindows()