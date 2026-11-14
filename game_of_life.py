#Cree le 6 Fevrier 2024
from kandinsky import fill_rect,draw_string
from random import randint
from time import sleep
from ion import keydown

#La valeur minimale de m doit être de 4 sur la calculatrice Numworks
m=8
bl,wh=(0,0,0),(255,255,255)
sw,sh=320%m,222%m
interface=(255,182,57)
fill_rect(0,0,320,sh,interface)
fill_rect(0,0,sw,222,interface)


ta=[[0]*(222//m) for i in range(320//m)]
for a in range(320//m):
  for b in range(222//m):
    if randint(0,1)==1:ta[a][b]=1
tf=[[0]*(222//m) for i in range(320//m)]
def etat(x,y):
  cv,cm=0,0
  for ca in range(-1,2):
    for cb in range(-1,2):
      if ca==0 and cb==0:pass
      else:
        cx,cy=x+ca,y+cb
        if cx<0:cx+=320//m
        elif cx>320//m-1:cx-=320//m
        if cy<0:cy+=222//m
        elif cy>222//m-1:cy-=222//m
        if ta[cx][cy]==1:cv+=1
        else:cm+=1
  if ta[x][y]==0 and cv==3:tf[x][y]=1
  if ta[x][y]==1:
    if cv==2 or cv==3:tf[x][y]=1
    else:tf[x][y]=0

while True:
  for a in range(320//m):
    for b in range(222//m):
      if ta[a][b]==1:fill_rect(a*m+sw,b*m+sh,m,m,bl)
      else:fill_rect(a*m+sw,b*m+sh,m,m,wh)
  for ea in range(320//m):
    for eb in range(222//m):
      etat(ea,eb)
  ta=tf
  tf=[[0]*(222//m) for i in range(320//m)]
#  sleep(1)
