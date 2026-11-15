#Cree le 6 Fevrier 2024
from kandinsky import fill_rect,draw_string,get_pixel
from random import randint
from time import sleep
from ion import keydown

c=[(255,)*3,(0,)*3]

#Minimal's value for resolution (m) is now 2 instead of 4 on a Numworks calculator
m=6
w,h=320//m,222//m
sw,sh=320%m,222%m

interface=(255,182,57)
fill_rect(0,0,320,sh,interface)
fill_rect(0,0,sw,222,interface)

#t is the value of the sub-grid we compute at each frame
#instead of prossessing all of the screen
#And its optimal value is calculated like that :
#(it's rounded and bounded to stay in decents values)
t=max(8,min(round((w*h)**(1/3)-1),40))

#If we have a rest of 1, at the end, we won't be able
#to do one more list since we need at least 2 pixels to
#do a grid of 1 pixel large
#So if it isn't right, we must change the t value
pt,st=t,False
while w%(t+1)==1 or h%(t+1)==1:
  #At the beginning we try reducing t
  if t>8 and not st:t-=1
  #If it's too small we try increasing it
  elif not st:t,st=pt+1,True
  else:t+=1
del pt,st


gp=lambda x,y:0 if get_pixel(sw+x*m,sh+y*m)==c[0]else 1
def gst(x1,y1,x2,y2): #Get Screen Table
  table=[]
  for y in range(y1-1,y2+1):
    y,row=y%h,[]
    for x in range(x1-1,x2+1):
      x=x%w
      row.append(gp(x,y))
    table.append(row)
  return table
def gsft(ta): #Get States From Table
  tf=[[0]*(len(ta[0])-2)for _ in range(len(ta)-2)]
  for y in range(1,len(ta)-1):
    for x in range(1,len(ta[y])-1):
      b0,b1=0,0
      for ca in range(-1,2):
        for cb in range(-1,2):
          if ca==0 and cb==0:pass
          else:
            cx,cy=x+ca,y+cb
            #Wrapping around screen's values
            #if cx<1:cx+=len(ta[y])-1
            #elif cx>len(ta[y])-2:cx-=len(ta[y])+1
            #if cy<1:cy+=len(ta)-1
            #elif cy>len(ta)-2:cy-=len(ta)+1

            if ta[cy][cx]==1:b1+=1
            else:b0+=1
      #adapted values of x and y for tf since it doesn't have borders
      ax,ay=x-1,y-1
      if ta[y][x]==0 and b1==3:tf[ay][ax]=1
      if ta[y][x]==1:
        if b1==2 or b1==3:tf[ay][ax]=1
        else:tf[ay][ax]=0
  return tf

def gc(ta): #Get Contour
  #The contour of the table is to compute all inside values
  #Then we'll need to compute these contour values
  #So we save the last layer of these previous values
  #to compute our future values
  tf=[]
  for x in ta[1]:tf.append(x)
  for y in range(len(ta)):tf.append(ta[y][len(ta[y])-2])
  for x in reversed(ta[len(ta)-2]):tf.append(x)
  for y in reversed(range(len(ta))):tf.append(ta[y][1])
  return tf

def cns(): #Calculate New States
  tw,th=(w-1)//(t+1)+1,(h-1)//(t+1)+1
  cts=[]
  for b in range(th):
    rct=[]
    for a in range(tw):
      #We remove 1 point from w and h for the max values
      #because we need to let the last values untouched
      #because the first values wrap around the screen
      #and use these values
      st=gst(a*(t+1),b*(t+1),min(a*(t+1)+t,w-1),min(b*(t+1)+t,h-1))
      ct=gc(st)
      rct.append(ct)
      st=gsft(st)
      for y in range(len(st)):
        for x in range(len(st[0])):
          fill_rect(sw+a*(t+1)*m+x*m,sh+b*(t+1)*m+y*m,m,m,c[st[y][x]])
    cts.append(rct)
  crn=[]
  for b in range(th):
    for a in range(tw):
      x1,y1=a*(t+1),b*(t+1)
      x2,y2=min(x1+t,w-1),min(y1+t,h-1)
      W,H=x2-x1+2,y2-y1+2
      nb,na=(b+1)%th,(a+1)%tw
      nW=min(na*(t+1)+t,w-1)-na*(t+1)+2
      ht=[cts[b][a][W+H:2*W+H][::-1],[gp(x%w,y2)for x in range(x1-1,x2+1)],cts[nb][a][:W]]
      st=gsft(ht)
      for x in range(len(st[0])):
        fill_rect(sw+(x1+x)*m,sh+y2*m,m,m,c[st[0][x]])
      c0,c1,c2=cts[b][a][W:W+H],[gp(x2,y%h)for y in range(y1-1,y2+1)],cts[b][na][2*nW+H:][::-1]
      st=gsft([[c0[i],c1[i],c2[i]]for i in range(H)])
      for y in range(len(st)):
        fill_rect(sw+x2*m,sh+(y1+y)*m,m,m,c[st[y][0]])
      st=gsft([[ht[0][-2],ht[0][-1],c2[-2]],[c0[-1],c1[-1],c2[-1]],[ht[2][-2],ht[2][-1],cts[nb][na][1]]])
      crn.append((x2,y2,st[0][0]))
  for x2,y2,v in crn:
    fill_rect(sw+x2*m,sh+y2*m,m,m,c[v])


glider="010;001;111"
lightweight_spaceship="01111;10001;00001;10010"
koks_galaxy="0000000000000;0000000000000;0011011111100;0011011111100;0011000000000;0011000001100;0011000001100;0011000001100;0000000001100;0011111101100;0011111101100;0000000000000;0000000000000"
def decode(char):
 rows=char.split(';')
 return[[int(c)for c in row]for row in rows]
glider=decode(glider)
lightweight_spaceship=decode(lightweight_spaceship)
koks_galaxy=decode(koks_galaxy)

def init_random():
  for x in range(w):
    for y in range(h):
      s=randint(0,1)
      fill_rect(sw+x*m,sh+y*m,m,m,c[s])

def init_form(x,y,ta):
  for cy in range(len(ta)):
    for cx in range(len(ta[cy])):
      fill_rect(sw+(x+cx)%w*m,sh+(y+cy)%h*m,m,m,c[ta[cy][cx]])

#init_random()
init_form(17,17,glider)
init_form(30,8,lightweight_spaceship)
init_form(3,23,koks_galaxy)
while True:
  cns()
  #sleep(0.1)
