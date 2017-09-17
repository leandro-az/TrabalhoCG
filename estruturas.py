import math

matOri = [[10, 40, 0, 1], #0
          [10, 100, 0,1], #1
          [70, 170, 0,1], #2
          [140, 170, 0,1],#3
          [210, 100, 0,1],#4
          [210, 40, 0,1],#5
          [140, 0, 0,1],  #6
          [70, 0, 0,1],  #7
          [10, 40, 30, 1],#8
          [10, 100, 30, 1],#9
          [70, 170, 30, 1], #10
          [140, 170, 30, 1],#11
          [210, 100, 30, 1],#12
          [210, 40, 30, 1],#13
          [140, 0, 30, 1],#14
          [70, 0, 30, 1]]#15
x0=300
y0=200

pontosPoli=8

matProPZ=[[1,0,0,0],
          [0,1,0,0],
          [0,0,0,0],
          [0,0,0,1]]

def multiplicaMatriz(A,B):
    linhaA=len(A)
    colunaA=len(A[0])
    linhaB = len(B)
    colunaB= len(B[0])
    resp = []
    if(colunaA != linhaB):
        print("Impossivel Multiplicar Matrizes colunaA dif linhaB")
        return resp
    for l in range(linhaA):
        resp.append([])
        for c in range(colunaB):
            resp[l].append(0)
            for k in range(colunaA):
                resp[l][c]+=A[l][k]*B[k][c]

    return resp

def fazRotacaoEmX(mat,angulo):

    matRotX = [ [1, 0, 0, 0],
                [0, math.cos(angulo), math.sin(angulo), 0],
                [0, math.sin(angulo)*(-1),math.cos(angulo), 0],
                [0, 0, 0, 1]]

    return multiplicaMatriz(mat,matRotX)

def fazRotacaoEmY(mat,angulo):

    matRotY = [[math.cos(angulo),0,math.sin(angulo)*(-1),0],
               [0,1,0,0],
               [math.sin(angulo),0,math.cos(angulo),0],
               [0,0,0,1]]

    return multiplicaMatriz(mat, matRotY)

def fazRotacaoEmZ(mat,angulo):

    matRotZ = [[math.cos(angulo),math.sin(angulo),0,0],
               [math.sin(angulo)*(-1),math.cos(angulo),0,0],
               [0,0,1,0],
               [0,0,0,1]]

    return multiplicaMatriz(mat, matRotZ)


