# -*- coding: utf-8 -*-
from __future__ import division
from graphics import *
from estruturas import *
import random, time, decimal



def desenhaRetasPassoAPasso(janela,matOpera):
    pontoAnt=Point(matOpera[0][0] , matOpera[0][1] )
    pontoAtual=Point(0,0)
    pt = Circle(pontoAtual, 3)
    for i in range(len(matOpera)):
        # desenha o ponto no nosso caso circulo pequeno de raio 3
        pt.setFill("yellow")
        pontoAtual=Point(matOpera[i][0] , matOpera[i][1] )
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
            pontoAnt = Point(matOpera[i - (pontosPoli - 1)][0] , matOpera[i - (pontosPoli - 1)][1] )
            reta = Line(pontoAnt, pontoAtual)
            reta.draw(janela)
            if(i+1<len(matOpera)):
             pontoAnt = Point(matOpera[i+1][0] , matOpera[i+1][1] )
    # desenha ultimas retas
    for i in range(len(matOri)):
        pontoAnt = Point(matOpera[i][0] , matOpera[i][1] )

        for j in range(i+1,len(matOri)):
            if(matOri[i][0]==matOri[j][0] and matOri[i][1]==matOri[j][1] and matOri[i][2]!=matOri[j][2]):

                  pontoAtual= Point(matOpera[j][0] , matOpera[j][1] )
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
          listaPLanos1[p1]=Point(matOpera[i][0],matOpera[i][1] )
          p1=p1+1
        else:
          listaPLanos2[p2]=Point(matOpera[i][0],matOpera[i][1])
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
        listaPLanos1[0] = Point(matOpera[i][0] , matOpera[i][1] )
        listaPLanos1[1] = Point(matOpera[i + 1][0] , matOpera[i + 1][1] )
        listaPLanos1[2] = Point(matOpera[i + 9][0] , matOpera[i + 9][1] )
        listaPLanos1[3] = Point(matOpera[i + 8][0] , matOpera[i + 8][1] )
        poli1 = Polygon(listaPLanos1)
        poli1.setFill(cor)
        poli1.draw(janela)
        time.sleep(0.4)


    r = random.randrange(256)
    b = random.randrange(256)
    g = random.randrange(256)
    cor = color_rgb(r, g, b)
    listaPLanos1 = range(4)
    listaPLanos1[0] = Point(matOpera[0][0] , matOpera[0][1] )
    listaPLanos1[1] =   Point(matOpera[7][0] , matOpera[7][1] )
    listaPLanos1[2] =Point(matOpera[15][0] , matOpera[15][1] )
    listaPLanos1[3] =  Point(matOpera[8][0] , matOpera[8][1] )
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



def desenhaCoordenadasNaTela(janela,matOpera):


     dx= 4
     dy=120
     listaP =[]
     for i in range(len(matOpera)):

       listaP.append([" "]*2)

       # desenha os quadrados para clique
       quadrado=Rectangle(Point(dx,dy),Point(dx+20,dy+20))
       quadrado.setFill("Black")
       quadrado.draw(janela)

       listaP[i][0]=Point(dx,dy)
       listaP[i][1] = Point(dx+20,dy+20)



       frase = " (" + str(float(round(matOpera[i][0]))) +"," + str(float(round(matOpera[i][1])*(-1))) + " )"
       texto=Text(Point(quadrado.getP2().x+50, dy+10),frase )
       texto.setFill("Black")
       texto.draw(janela)

       dy=dy+35

     return listaP




def trataClick(janela,LP,matOpera):
    click = janela.getMouse().clone()
    ant=Rectangle(Point(-1,-1),Point(0,0))
    for i in range(len(LP)):
        if((click.getX() >= LP[i][0].x) and (LP[i][1].x>=click.getX()) and
           (click.getY() >= LP[i][0].y) and (LP[i][1].y >= click.getY()) ):
            pontoAtual = Point(matOpera[i][0] , matOpera[i][1] )
            pt = Circle(pontoAtual,8)
            pt.setOutline("black")
            pt.setFill("yellow")
            pt.draw(janela)
            return pt


    ant.draw(janela)
    return ant


def main():


     janela = GraphWin("",1000,1000)
     janela.setBackground(color_rgb(255,255,255))


     mat = montaProjecaoParalelaIsometrica(matOri, -35.26,45)
     mat = fazTranslacao(mat)

     titulo = Text(Point(500, 30), "Projeção Isométrica")
     titulo.setSize(30)
     titulo.setFill("Black")
     titulo.draw(janela)

     desenhaRetasPassoAPasso(janela, mat)
     desenhaPlanosPassoAPasso(janela, mat)


     co = desenhaCoordenadasNaTela(janela, mat)
     resp = True
     while (resp):
        result = trataClick(janela, co, mat)
        if(result.getP1().x==-1):
           resp=False
        time.sleep(1.5)
        result.undraw()

     janela.delete("all")

     mat = montaProjecaoObliquaCabinet(matOri,25)
     mat = fazTranslacao(mat)

     titulo = Text(Point(500, 30), "Projeção Oblíqua -- Cabinet")
     titulo.setSize(30)
     titulo.setFill("Black")
     titulo.draw(janela)

     desenhaRetasPassoAPasso(janela, mat)
     desenhaPlanosPassoAPasso(janela, mat)


     co = desenhaCoordenadasNaTela(janela, mat)
     resp = True
     while (resp):
        result = trataClick(janela, co, mat)
        if (result.getP1().x == -1):
            resp = False
        time.sleep(1.5)
        result.undraw()

     janela.delete("all")


     mat= fazProjecaoPespec(matOri)
     mat = fazTranslacao(mat)

     titulo = Text(Point(500, 30), "Projeção Em Pespectiva -- 1PF")
     titulo.setSize(30)
     titulo.setFill("Black")
     titulo.draw(janela)


     desenhaRetasPassoAPasso(janela, mat)


     desenhaPlanosPassoAPasso(janela, mat)


     co = desenhaCoordenadasNaTela(janela, mat)
     resp = True
     while (resp):
          result = trataClick(janela, co, mat)
          if (result.getP1().x == -1):
              resp = False
          time.sleep(1.5)
          result.undraw()

     janela.close()









main()
