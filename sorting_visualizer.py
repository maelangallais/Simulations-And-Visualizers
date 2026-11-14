from math import floor
from kandinsky import fill_rect
from random import choice
from time import sleep

ent=lambda n:floor(n)if n-floor(n)<0.5 else floor(n)+1

pl=[i+1 for i in range(80)]
vl=[]
for i in range(80):
  num=choice(pl)
  pl.remove(num)
  vl.append(num)

n=40

def new():
  global running
  fill_rect(0,0,320,2,(255,181,59))
  fill_rect(0,2,320,220,(255,)*3)
  for i in range(80):
    fill_rect(i*4,222,4,ent(-vl[i]*2.75),(vl[i]*3,0,0))
  for i in range(80):
    if vl[i]!=i+1:break
    elif i==79:running=False
  sleep(.001)

def bs():
  global n
  if vl[n]>vl[n+1]:vl[n],vl[n+1]=vl[n+1],vl[n];new()
  n=n+1 if n<78 else 0

def mid(lv,hv):
  md=(lv+hv)//2
  if vl[lv]>vl[md]:vl[lv],vl[md]=vl[md],vl[lv]
  if vl[lv]>vl[hv]:vl[lv],vl[hv]=vl[hv],vl[lv]
  if vl[md]>vl[hv]:vl[md],vl[hv]=vl[hv],vl[md]
  return md
def pt(lv,hv):
  px=mid(lv,hv);new()
  vl[px],vl[hv]=vl[hv],vl[px];new()
  pv,i=vl[hv],lv-1
  for n in range(lv,hv):
    if vl[n]<=pv:i+=1;vl[i],vl[n]=vl[n],vl[i];new()
  vl[i+1],vl[hv]=vl[hv],vl[i+1];new()
  return i+1
def qs(lv,hv):
  if lv<hv:
    pi=pt(lv,hv)
    qs(lv,pi-1)
    qs(pi+1,hv)

bubble_sort=False
quick_sort=True
running=True
while running:
  if bubble_sort:bs()
  if quick_sort:qs(0,79)
