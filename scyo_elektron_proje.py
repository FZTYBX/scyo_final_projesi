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
p5= sphere(pos=vector(650,-300,250*3**0.5-70),radius = 250,text="proton1",color = color.blue)