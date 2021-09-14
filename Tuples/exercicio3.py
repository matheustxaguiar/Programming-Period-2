"""
Para verificar se trˆes pontosp1= (x1, y1),p2= (x2, y2),p3= (x3, y3) no planocartesiano est ̃ao alinhados, podemos
verificar se o determinante da matriz a seguir ́eigual a zero:
    M = x1  y1  1
        x2  y2  1
        x3  y3  1

    M = [ [x1 , y1 , 1], [x2 , y2 , 1], [x3 , y3 , 1] ]


A funcao a seguir recebe tres tuplas como parametros (os tres pontos), cria a matriz e utiliza a funcao criada
anteriormente para calcular o determinante da matriz.
"""