from math import sin, cos, tan, pi

def trigonometry(iteravel):
    
    for e in iteravel:
        e = float(e)

    seno = list(map(lambda x: sin(x), iteravel))
    cosseno = list(map(lambda x: cos(x), iteravel))
    tangente = list(map(lambda x: tan(x), iteravel))

    for i in range(0, len(iteravel)):
        print(f'\nSeno de {iteravel[i]}: {seno}\nCosseno de {iteravel[i]}: {cosseno}\nTangente de {iteravel[i]}: {tangente}\n')

print(trigonometry([30, 60, 90]))