# -*- coding: utf-8 -*-

from graphics import *
from estruturas import *
import random, time


def desenhaPontos(janela):
    for i in range(len(matOri)):
        pt= Circle(Point(matOri[i][0] + x0, matOri[i][1] + y0), 3)
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

def desenhaRetasPassoAPasso(janela,matOpera):
    pontoAnt=Point(matOpera[0][0] + x0, matOpera[0][1] + y0)
    pontoAtual=Point(0,0)
    pt = Circle(pontoAtual, 3)
    for i in range(len(matOpera)):
        # desenha o ponto no nosso caso circulo pequeno de raio 3
        pt.setFill("yellow")
        pontoAtual=Point(matOpera[i][0] + x0, matOpera[i][1] + y0)
        pt= Circle(pontoAtual,3)
        if(i>0):
           pt.setFill("red")
        pt.draw(janela)
        time.sleep(0.4)
        #desenha reta somente se entre pontos do mesmo plano
        if(i!=0 ):
            reta=Line(pontoAnt,pontoAtual)
            reta.draw(janela)
            time.sleep(0.4)
            pontoAnt=pontoAtual
        #se ja chegou no ultimo vértice desenhado do plano, fecha o plano com a ultima reta
        if (i > 0 and ((i + 1) % pontosPoli == 0)):
            pt.setFill("yellow")
            pontoAnt = Point(matOpera[i - (pontosPoli - 1)][0] + x0, matOpera[i - (pontosPoli - 1)][1] + y0)
            reta = Line(pontoAnt, pontoAtual)
            reta.draw(janela)
            if(i+1<len(matOpera)):
             pontoAnt = Point(matOpera[i+1][0] + x0, matOpera[i+1][1] + y0)
    # desenha ultimas retas
    for i in range(len(matOri)):
        pontoAnt = Point(matOpera[i][0] + x0, matOpera[i][1] + y0)

        for j in range(i+1,len(matOri)):
            if(matOri[i][0]==matOri[j][0] and matOri[i][1]==matOri[j][1] and matOri[i][2]!=matOri[j][2]):

                  pontoAtual= Point(matOpera[j][0] + x0, matOpera[j][1] + y0)
                  reta = Line(pontoAnt, pontoAtual)
                  reta.draw(janela)
                  time.sleep(0.4)


def desenhaPlanosPassoAPasso(janela,matOpera):


    listaPLanos1=range(pontosPoli)
    listaPLanos2 = range(pontosPoli)
    p1=0
    p2=0
    for i in range(len(matOpera)):
        if(i<pontosPoli):
          listaPLanos1[p1]=Point(matOpera[i][0]+ x0,matOpera[i][1]  + y0)
          p1=p1+1
        else:
          listaPLanos2[p2]=Point(matOpera[i][0]+ x0,matOpera[i][1]  + y0)
          p2=p2+1

#------------------------------- desenha o plano superior -----------------------------------------------------------------------------------

    r = random.randrange(256)
    b = random.randrange(256)
    g = random.randrange(256)
    cor = color_rgb(r, g, b)
    poli1=Polygon(listaPLanos1)
    poli1.setFill(cor)
    poli1.draw(janela)
    time.sleep(0.4)

# ------------------------------- desenha os planos em volta ------------------------------------------------------------------------

    for i in range(pontosPoli - 1):
        r = random.randrange(256)
        b = random.randrange(256)
        g = random.randrange(256)
        cor = color_rgb(r, g, b)
        listaPLanos1 = range(4)
        listaPLanos1[0] = Point(matOpera[i][0] + x0, matOpera[i][1] + y0)
        listaPLanos1[1] = Point(matOpera[i + 1][0] + x0, matOpera[i + 1][1] + y0)
        listaPLanos1[2] = Point(matOpera[i + 9][0] + x0, matOpera[i + 9][1] + y0)
        listaPLanos1[3] = Point(matOpera[i + 8][0] + x0, matOpera[i + 8][1] + y0)
        poli1 = Polygon(listaPLanos1)
        poli1.setFill(cor)
        poli1.draw(janela)
        time.sleep(0.4)


    r = random.randrange(256)
    b = random.randrange(256)
    g = random.randrange(256)
    cor = color_rgb(r, g, b)
    listaPLanos1 = range(4)
    listaPLanos1[0] = Point(matOpera[0][0] + x0, matOpera[0][1] + y0)
    listaPLanos1[1] =   Point(matOpera[7][0] + x0, matOpera[7][1] + y0)
    listaPLanos1[2] =Point(matOpera[15][0] + x0, matOpera[15][1] + y0)
    listaPLanos1[3] =  Point(matOpera[8][0] + x0, matOpera[8][1] + y0)
    poli1 = Polygon(listaPLanos1)
    poli1.setFill(cor)
    poli1.draw(janela)
    time.sleep(0.4)


# ------------------------------- desenha o plano inferior -----------------------------------------------------------------------------

    r = random.randrange(256)
    b = random.randrange(256)
    g = random.randrange(256)
    cor = color_rgb(r, g, b)
    poli2 = Polygon(listaPLanos2)
    poli2.setFill(cor)
    poli2.draw(janela)






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
    # mat=fazRotacaoEmX(matOri,20)
    # mat = fazRotacaoEmY(mat, 90)
     mat=montaCabinetModificada(matOri,25)

     desenhaRetasPassoAPasso(janela,mat)

     desenhaPlanosPassoAPasso(janela,mat)



     desenhaSetaE(janela)
     desenhaSetaD(janela)
     click = janela.getMouse().clone()
     if (click.getX() > 0):
         print(click.getX())
         resp= False

    janela.close()









main()
