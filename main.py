from graphics import *
from estruturas import *

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


def desenhaPontos(janela):
    for i in range(len(vet)):
        pt= Circle(Point(vet[i][0]+x0,vet[i][1]+y0),3)
        pt.setFill("blue")
        pt.draw(janela)


def desenhaSetaE(janela):
    setaE = Polygon(Point(100, 60), Point(130, 40), Point(100, 20))
    setaE.setFill("blue")
    setaE.draw(janela)
    #click=janela.getMouse().clone()
    #if(click.getX() > 0):
    #    print(click.getX())
     #   setaE.undraw()
     #   return False

def desenhaSetaD(janela):
    setaD = Polygon(Point(70, 60), Point(40, 40), Point(70, 20))
    setaD.setFill("blue")
    setaD.draw(janela)
    #click=janela.getMouse().clone()
    #if(click.getX() > 0):
       # print(click.getX())
      #  setaE.undraw()
      #  return False

def desenhaPontoPassoAPasso():
    pass

def desenhaRetasPassoAPasso():
    pass

def desenhaPlanosPassoAPasso():
    pass

def colorePlanosPassoAPasso():
    pass

def desenhaPespectiva1PontoDeFuga():
    pass

def desenhaProjecaoIsometrica():
    pass

def desenhaProjecaoObliqua():
    pass

def desenhaTranslacao():
    pass


def main():


    janela = GraphWin("",800,600)
    janela.setBackground(color_rgb(255,255,255))


    resp=True
    while(resp):
     desenhaPontos(janela)
     desenhaSetaE(janela)
     desenhaSetaD(janela)
     click = janela.getMouse().clone()
     if (click.getX() > 0):
         print(click.getX())
         resp= False


    janela.close()









main()
