# FİNAL PROJESİ

from vpython import *
import time
import math

#Protonlar mavi renkli,
#nötronlar mor renkli, 
#büyüklükleri sembolik.

p1= sphere(pos=vector(0,0,0),radius = 250,text="proton1",color = color.blue)
p2= sphere(pos=vector(500,0,0),radius = 250,text="proton1",color = color.blue)
p3= sphere(pos=vector(250,0,250*3**0.5),radius = 250,text="proton1",color = color.blue)
p4= sphere(pos=vector(250,0,-250*3**0.5),radius = 250,text="proton1",color = color.blue)
n1= sphere(pos=vector(250,250*3**0.5,0),radius = 250,text="proton1",color = color.purple)
n2= sphere(pos=vector(250,-250*3**0.5,0),radius = 250,text="proton1",color = color.purple)
n3= sphere(pos=vector(70,-150*3**0.5-50,-350),radius = 250,text="proton1",color = color.purple)
n4= sphere(pos=vector(250,-500,250*3**0.5),radius = 250,text="proton1",color = color.purple)
dönen = sphere(pos = vector(12000*(2**0.5)/2,0,12000*(2**0.5)/2),radius = 300,make_trail=True,trail_type="points")
dönen1 = sphere(pos = vector(-12000*(2**0.5)/2,0,12000*(2**0.5)/2),radius = 300,make_trail=True,trail_type="points")
dönen2 = sphere(pos = vector(12000*(2**0.5)/2,0,-12000*(2**0.5)/2),radius = 300,make_trail=True,color =color.red,trail_type="points")
dönen3 = sphere(pos = vector(-12000*(2**0.5)/2,0,-12000*(2**0.5)/2),radius = 300,make_trail=True,color = color.red,trail_type="points")
liste1 = []
time.sleep(2) 
liste2 = []
liste3 = []
liste4 = []
for i in range(1,90):
    liste1.append(i) 
for i in range(91,181):
    liste2.append(i)
for i in range(181,270):
    liste3.append(i)
for i in range(271,361):
    liste4.append(i)
time.sleep(2)
