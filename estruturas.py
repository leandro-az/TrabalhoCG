# -*- coding: utf-8 -*-

import math


x0=400
y0=350

Tx=5
Ty=6
Tz=8

Zp=130
Zpc=150

pontosPoli=8


matOri = [[10, 40, 0, 1], #0
          [10, 100, 0,1], #1
          [70, 170, 0,1], #2
          [140, 170, 0,1],#3
          [210, 100, 0,1],#4
          [210, 40, 0,1],#5
          [140, 0, 0,1],  #6
          [70, 0, 0,1],  #7
          [10, 40, Zp, 1],#8
          [10, 100, Zp, 1],#9
          [70, 170, Zp, 1], #10
          [140, 170, Zp, 1],#11
          [210, 100, Zp, 1],#12
          [210, 40, Zp, 1],#13
          [140, 0, Zp, 1],#14
          [70, 0, Zp, 1]]#15




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

def montaTransposta(A):
    resp=[]
    for i in range (len(A[0])):
        resp.append([" "]*len(A))

    for i in range(len(A[0])):
        for j in range(len(A)):
            resp[i][j]=A[j][i]

    return resp
# Montar a matriz MISO unindo as duas rotacoes abaixo Resolve ( Projecao paralela Isometrica )-----------------------------------------

def fazRotacaoEmX(mat,angulo):

    matRotX = [ [1, 0, 0, 0],
                [0, math.cos(angulo*math.pi/180), math.sin(angulo*math.pi/180), 0],
                [0, math.sin(angulo*math.pi/180)*(-1),math.cos(angulo*math.pi/180), 0],
                [0, 0, 0, 1]]

    return multiplicaMatriz(mat,matRotX)

def fazRotacaoEmY(mat,angulo):

    matRotY = [[math.cos(angulo*math.pi/180),0,math.sin(angulo*math.pi/180)*(-1),0],
               [0,1,0,0],
               [math.sin(angulo*math.pi/180),0,math.cos(angulo*math.pi/180),0],
               [0,0,0,1]]

    return multiplicaMatriz(mat, matRotY)

def fazRotacaoEmZ(mat,angulo):

    matRotZ = [[math.cos(angulo),math.sin(angulo),0,0],
               [math.sin(angulo)*(-1),math.cos(angulo),0,0],
               [0,0,1,0],
               [0,0,0,1]]

    return multiplicaMatriz(mat, matRotZ)

def montaMatrizMISO(Ox,Oy):

    matRotX = [ [1, 0, 0, 0],
                [0, math.cos(Ox*math.pi/180), math.sin(Ox*math.pi/180), 0],
                [0, math.sin(Ox*math.pi/180)*(-1),math.cos(Ox*math.pi/180), 0],
                [0, 0, 0, 1]]

    matRotY = [[math.cos(Oy*math.pi/180), 0, math.sin(Oy*math.pi/180) * (-1), 0],
               [0, 1, 0, 0],
               [math.sin(Oy*math.pi/180), 0, math.cos(Oy*math.pi/180), 0],
               [0, 0, 0, 1]]

    return multiplicaMatriz(matRotX,matRotY)

def montaProjecaoParalelaIsometrica(mat,Ox,Oy):

    matMISO=montaMatrizMISO(Ox,Oy)

    return multiplicaMatriz(mat,matMISO)

# --------------------------------------------------------------------------------------------------


# Projecao Obliqua Cabinet  ----------------------------------------------------

def montaProjecaoObliquaCabinet(mat,angulo):
    aux=mat
    matCab = [                 [1, 0,0, 0],  # acertar
                               [0, 1 , 0, 0],
                               [0.5*math.cos(angulo*(math.pi/180)),  0.5*math.sin(angulo*(math.pi/180)), 0, 0],
                               [0, 0, 0, 1]]
    aux[8:]=multiplicaMatriz(aux[8:],matCab)
    return aux


# falta so acertar a pespectiva  -------------------------------------------------------------------------

def fazProjecaoPespec(mat):

    aux = mat

    matPespec = [      [0.5,0,0,0],
                       [0,0.5,0,0],
                       [0,0,0,0],
                       [0,0,1,0.5]]
    '''
    matPespec2 = [[1, 0, 0, 0],
                 [0, 1, 0, 0],
                 [-1/Zpc, -1/Zpc,0, 0],
                 [0, 0, 0, 1]]

    '''
    aux[8:] = multiplicaMatriz(mat[8:],matPespec)


    return (aux)
