import cv2
import matplotlib.pyplot as plt

imagem = cv2.imread('Computer Vision Introduction/imagem2.jpg')
# Copy Relative Path --> retorna o caminho 'encurtado' (funciona melhor)

'''
imagem = cv2.imread('Computer Vision Introduction/imagem2.jpg', 0)
Passando como segundo argumento o '0', colocamos a imagem em escala de cinza
'''

print(imagem.shape) # ---> (2552, 3840, 3)
altura = imagem.shape[0] # pega o valor da altura
largura = imagem.shape[1] # pega o valor da largura

porcentagem = 20
nova_altura = int(altura*porcentagem/100)
nova_largura = int(largura*porcentagem/100)

dimensoes = (nova_largura, nova_altura)

imagem_reduzida = cv2.resize(imagem, dimensoes, interpolation=cv2.INTER_AREA)

imagem_RGB = cv2.cvtColor(imagem_reduzida, cv2.COLOR_BGR2RGB) # convertendo imagem para escala RGB
plt.imshow(imagem_RGB)
plt.title('Galaxy'.upper())
plt.show()

'''
cv2.imshow('Galaxy'.upper(), imagem_reduzida)
cv2.waitKey(0)
cv2.destroyAllWindows()
'''