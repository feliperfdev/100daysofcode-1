# Importando as bibliotecas
import numpy as np
import cv2

quadro = np.zeros((500,500,3), dtype = 'uint8')

cv2.putText(quadro, "Clarissa Lima Tech", (50,250), 
cv2.FONT_HERSHEY_DUPLEX,1.3,(255,51,153),3, cv2.LINE_AA)

cv2.imshow('Quadro', quadro)
cv2.waitKey(0)
cv2.destroyAllWindows()