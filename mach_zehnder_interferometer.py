#Créé le 03 Juin 2026
from math import *
from turtle import *

#hideturtle()
speed(10)

def d(L,R,S,I):
  l=L-S
  c1=l/80
  c2=L/80
  a=asin(l*0.25/R)/pi*360
  if I:
    a=-a
  R=int(R/c2)

  penup()
  goto(-161,0)
  pendown()
  color('black')
  forward(80)

  color('red')
  circle(R,a)
  color('green')
  circle(R,-a)
  color('blue')
  forward(int(S/c1))
  color('green')
  circle(R,-a)
  color('red')
  circle(R,a)

  color('black')
  forward(80)

d(0.02,0.05,0,False)
d(0.02,0.05,0,True)
