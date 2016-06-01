import numpy as np
import os
from tkinter import *
import sys
import RImp

app = Tk()
app.geometry("1400x650+00+0")
app.config(background="white")
app.title("Selección de Medidas")

"/////////////////////////////////////////////////////////////////////////////////////"

#Frames para cada programa de manejo
frm1 = Frame(bg="white",width=1400,height=650)
frm2 = Frame(bg="white",width=1400,height=650)
frm3 = Frame(bg="white",width=1400,height=650)
frm4 = Frame(bg="white",width=1400,height=650)
frm5 = Frame(bg="white",width=1400,height=650)
frm6 = Frame(bg="white",width=1400,height=650)
frm7 = Frame(bg="white",width=1400,height=650)
frm8= Frame(bg="white",width=1400,height=650)
frm82 = Frame(bg = "white", width = 1400, height = 650)
frm83 = Frame(bg = 'white', width = 1400, height = 650)
frm9= Frame(bg="white",width=1400,height=650)
frm92 = Frame(bg = 'white', width = 1400, height = 650)
frm10 = Frame(bg="white",width=1400,height=650)
frm11= Frame(bg="white",width=1400,height=650)
frm12 = Frame(bg="white",width=1400,height=650)
frm13 = Frame(bg="white",width=1400,height=650)
frm132 = Frame(bg = "white", width = 1400, height = 650)
frm14= Frame(bg="white",width=1400,height=650)
frm142 = Frame(bg = "white", width = 1400, height = 650)
frm15 = Frame(bg = 'white', width = 1400, height = 650)


"//////////////////////////////////////////////////////////////////////////////////////////////////////"
#Funciones para mostrar cada frame
def m1():
	frm1.grid()
	frm2.grid_remove()
	frm3.grid_remove()
	frm4.grid_remove()
	frm5.grid_remove()
	frm6.grid_remove()
	frm7.grid_remove()
	frm8.grid_remove()
	frm9.grid_remove()
	frm10.grid_remove()
	frm11.grid_remove()
	frm12.grid_remove()
	frm13.grid_remove()
	frm14.grid_remove()
	frm15.grid_remove()
	frm92.grid_remove()
	frm132.grid_remove()


def m2():
	frm1.grid_remove()
	frm2.grid()
	frm3.grid_remove()
	frm4.grid_remove()
	frm5.grid_remove()
	frm6.grid_remove()
	frm7.grid_remove()
	frm8.grid_remove()
	frm9.grid_remove()
	frm10.grid_remove()
	frm11.grid_remove()
	frm12.grid_remove()
	frm13.grid_remove()
	frm14.grid_remove()
	frm15.grid_remove()
	frm92.grid_remove()
	frm132.grid_remove()

def m3():
	frm1.grid_remove()
	frm2.grid_remove()
	frm3.grid()
	frm4.grid_remove()
	frm5.grid_remove()
	frm6.grid_remove()
	frm7.grid_remove()
	frm8.grid_remove()
	frm9.grid_remove()
	frm10.grid_remove()
	frm11.grid_remove()
	frm12.grid_remove()
	frm13.grid_remove()
	frm14.grid_remove()
	frm15.grid_remove()
	frm92.grid_remove()
	frm132.grid_remove()

def m4():
	frm1.grid_remove()
	frm2.grid_remove()
	frm3.grid_remove()
	frm4.grid()
	frm5.grid_remove()
	frm6.grid_remove()
	frm7.grid_remove()
	frm8.grid_remove()
	frm9.grid_remove()
	frm10.grid_remove()
	frm11.grid_remove()
	frm12.grid_remove()
	frm13.grid_remove()
	frm14.grid_remove()
	frm15.grid_remove()
	frm82.grid_remove()
	frm83.grid_remove()
	frm92.grid_remove()
	frm132.grid_remove()

def m5():
	frm1.grid_remove()
	frm2.grid_remove()
	frm3.grid_remove()
	frm4.grid_remove()
	frm5.grid()
	frm6.grid_remove()
	frm7.grid_remove()
	frm8.grid_remove()
	frm9.grid_remove()
	frm10.grid_remove()
	frm11.grid_remove()
	frm12.grid_remove()
	frm13.grid_remove()
	frm14.grid_remove()
	frm15.grid_remove()
	frm82.grid_remove()
	frm83.grid_remove()
	frm92.grid_remove()
	frm132.grid_remove()

def m6():
	frm1.grid_remove()
	frm2.grid_remove()
	frm3.grid_remove()
	frm4.grid_remove()
	frm5.grid_remove()
	frm6.grid()
	frm7.grid_remove()
	frm8.grid_remove()
	frm9.grid_remove()
	frm10.grid_remove()
	frm11.grid_remove()
	frm12.grid_remove()
	frm13.grid_remove()
	frm14.grid_remove()
	frm15.grid_remove()
	frm82.grid_remove()
	frm83.grid_remove()
	frm92.grid_remove()
	frm132.grid_remove()

def m7():
	frm1.grid_remove()
	frm2.grid_remove()
	frm3.grid_remove()
	frm4.grid_remove()
	frm5.grid_remove()
	frm6.grid_remove()
	frm7.grid()
	frm8.grid_remove()
	frm9.grid_remove()
	frm10.grid_remove()
	frm11.grid_remove()
	frm12.grid_remove()
	frm13.grid_remove()
	frm14.grid_remove()
	frm15.grid_remove()
	frm82.grid_remove()
	frm83.grid_remove()
	frm92.grid_remove()
	frm132.grid_remove()

def m8():
	frm1.grid_remove()
	frm2.grid_remove()
	frm3.grid_remove()
	frm4.grid_remove()
	frm5.grid_remove()
	frm6.grid_remove()
	frm7.grid_remove()
	frm8.grid()
	frm9.grid_remove()
	frm10.grid_remove()
	frm11.grid_remove()
	frm12.grid_remove()
	frm13.grid_remove()
	frm14.grid_remove()
	frm15.grid_remove()
	frm82.grid_remove()
	frm83.grid_remove()
	frm92.grid_remove()
	frm132.grid_remove()

def m82():
	frm1.grid_remove()
	frm2.grid_remove()
	frm3.grid_remove()
	frm4.grid_remove()
	frm5.grid_remove()
	frm6.grid_remove()
	frm7.grid_remove()
	frm8.grid_remove()
	frm82.grid()
	frm9.grid_remove()
	frm10.grid_remove()
	frm11.grid_remove()
	frm12.grid_remove()
	frm13.grid_remove()
	frm14.grid_remove()
	frm15.grid_remove()
	frm83.grid_remove()
	frm92.grid_remove()
	frm132.grid_remove()

def m83():
	frm1.grid_remove()
	frm2.grid_remove()
	frm3.grid_remove()
	frm4.grid_remove()
	frm5.grid_remove()
	frm6.grid_remove()
	frm7.grid_remove()
	frm8.grid_remove()
	frm83.grid()
	frm9.grid_remove()
	frm10.grid_remove()
	frm11.grid_remove()
	frm12.grid_remove()
	frm13.grid_remove()
	frm14.grid_remove()
	frm15.grid_remove()
	frm82.grid_remove()
	frm92.grid_remove()
	frm132.grid_remove()


def m9():
	frm1.grid_remove()
	frm2.grid_remove()
	frm3.grid_remove()
	frm4.grid_remove()
	frm5.grid_remove()
	frm6.grid_remove()
	frm7.grid_remove()
	frm8.grid_remove()
	frm9.grid()
	frm10.grid_remove()
	frm11.grid_remove()
	frm12.grid_remove()
	frm13.grid_remove()
	frm14.grid_remove()
	frm15.grid_remove()
	frm82.grid_remove()
	frm83.grid_remove()
	frm92.grid_remove()
	frm132.grid_remove()


def m92():
	frm1.grid_remove()
	frm2.grid_remove()
	frm3.grid_remove()
	frm4.grid_remove()
	frm5.grid_remove()
	frm6.grid_remove()
	frm7.grid_remove()
	frm8.grid_remove()
	frm9.grid_remove()
	frm10.grid_remove()
	frm11.grid_remove()
	frm12.grid_remove()
	frm13.grid_remove()
	frm14.grid_remove()
	frm15.grid_remove()
	frm82.grid_remove()
	frm83.grid_remove()
	frm92.grid()
	frm132.grid_remove()


def m10():
	frm1.grid_remove()
	frm2.grid_remove()
	frm3.grid_remove()
	frm4.grid_remove()
	frm5.grid_remove()
	frm6.grid_remove()
	frm7.grid_remove()
	frm8.grid_remove()
	frm9.grid_remove()
	frm10.grid()
	frm11.grid_remove()
	frm12.grid_remove()
	frm13.grid_remove()
	frm14.grid_remove()
	frm15.grid_remove()
	frm82.grid_remove()
	frm83.grid_remove()
	frm92.grid_remove()
	frm132.grid_remove()

def m11():
	frm1.grid_remove()
	frm2.grid_remove()
	frm3.grid_remove()
	frm4.grid_remove()
	frm5.grid_remove()
	frm6.grid_remove()
	frm7.grid_remove()
	frm8.grid_remove()
	frm9.grid_remove()
	frm10.grid_remove()
	frm11.grid()
	frm12.grid_remove()
	frm13.grid_remove()
	frm14.grid_remove()
	frm15.grid_remove()
	frm82.grid_remove()
	frm83.grid_remove()
	frm92.grid_remove()
	frm132.grid_remove()

def m12():
	frm1.grid_remove()
	frm2.grid_remove()
	frm3.grid_remove()
	frm4.grid_remove()
	frm5.grid_remove()
	frm6.grid_remove()
	frm7.grid_remove()
	frm8.grid_remove()
	frm9.grid_remove()
	frm10.grid_remove()
	frm11.grid_remove()
	frm12.grid()
	frm13.grid_remove()
	frm14.grid_remove()
	frm15.grid_remove()
	frm82.grid_remove()
	frm83.grid_remove()
	frm92.grid_remove()
	frm132.grid_remove()

def m13():
	frm1.grid_remove()
	frm2.grid_remove()
	frm3.grid_remove()
	frm4.grid_remove()
	frm5.grid_remove()
	frm6.grid_remove()
	frm7.grid_remove()
	frm8.grid_remove()
	frm9.grid_remove()
	frm10.grid_remove()
	frm11.grid_remove()
	frm12.grid_remove()
	frm13.grid()
	frm14.grid_remove()
	frm15.grid_remove()
	frm82.grid_remove()
	frm83.grid_remove()
	frm92.grid_remove()
	frm132.grid_remove()

def m132():
	frm1.grid_remove()
	frm2.grid_remove()
	frm3.grid_remove()
	frm4.grid_remove()
	frm5.grid_remove()
	frm6.grid_remove()
	frm7.grid_remove()
	frm8.grid_remove()
	frm9.grid_remove()
	frm10.grid_remove()
	frm11.grid_remove()
	frm12.grid_remove()
	frm13.grid_remove()
	frm14.grid_remove()
	frm15.grid_remove()
	frm82.grid_remove()
	frm83.grid_remove()
	frm92.grid_remove()
	frm132.grid()

def m14():
	frm1.grid_remove()
	frm2.grid_remove()
	frm3.grid_remove()
	frm4.grid_remove()
	frm5.grid_remove()
	frm6.grid_remove()
	frm7.grid_remove()
	frm8.grid_remove()
	frm9.grid_remove()
	frm10.grid_remove()
	frm11.grid_remove()
	frm12.grid_remove()
	frm13.grid_remove()
	frm14.grid()
	frm15.grid_remove()
	frm142.grid_remove()
	frm82.grid_remove()
	frm83.grid_remove()
	frm92.grid_remove()
	frm132.grid_remove()

def m142():
	frm1.grid_remove()
	frm2.grid_remove()
	frm3.grid_remove()
	frm4.grid_remove()
	frm5.grid_remove()
	frm6.grid_remove()
	frm7.grid_remove()
	frm8.grid_remove()
	frm9.grid_remove()
	frm10.grid_remove()
	frm11.grid_remove()
	frm12.grid_remove()
	frm13.grid_remove()
	frm14.grid_remove()
	frm15.grid_remove()
	frm142.grid()
	frm82.grid_remove()
	frm83.grid_remove()
	frm92.grid_remove()
	frm132.grid_remove()

def m15():
	frm1.grid_remove()
	frm2.grid_remove()
	frm3.grid_remove()
	frm4.grid_remove()
	frm5.grid_remove()
	frm6.grid_remove()
	frm7.grid_remove()
	frm8.grid_remove()
	frm9.grid_remove()
	frm10.grid_remove()
	frm11.grid_remove()
	frm12.grid_remove()
	frm13.grid_remove()
	frm14.grid_remove()
	frm15.grid()
	frm82.grid_remove()
	frm83.grid_remove()
	frm92.grid_remove()
	frm132.grid_remove()



"//////////////////////////////////////////////////////////////////////////////////////////////////////"
#Variables de los checkbuttons

#Frm1 AGUAS DE LLUVIAS - 16 CHECK

f1c1 = IntVar()
f1c2 = IntVar()
f1c3 = IntVar()
f1c4 = IntVar()
f1c5 = IntVar()
f1c6 = IntVar()
f1c7 = IntVar()
f1c8 = IntVar()
f1c9 = IntVar()
f1c10 = IntVar()
f1c11 = IntVar()
f1c12 = IntVar()
f1c13 = IntVar()
f1c14 = IntVar()
f1c15 = IntVar()
f1c16 = IntVar()

#Frm2 AGUA PARA CONSUMO - 3

f2c1 = IntVar()
f2c2 = IntVar()
f2c3 = IntVar()

#Frm3 RESIDUOS LÍQUIDOS DOMÉSTICOS Y NO DOMÉSTICOS Y OTROS - 12
f3c1 = IntVar()
f3c2 = IntVar()
f3c3 = IntVar()
f3c4 = IntVar()
f3c5 = IntVar()
f3c6 = IntVar()
f3c7 = IntVar()
f3c8 = IntVar()
f3c9 = IntVar()
f3c10 = IntVar()
f3c11= IntVar()
f3c12 = IntVar()

#frm4  RESIDUOS DE EXCAVACIÓN Y DEMOLICIÓN - 14

f4c1 = IntVar()
f4c2 = IntVar()
f4c3 = IntVar()
f4c4 = IntVar()
f4c5 = IntVar()
f4c6 = IntVar()
f4c7 = IntVar()
f4c8 = IntVar()
f4c9 = IntVar()
f4c10 = IntVar()
f4c11 = IntVar()
f4c12 = IntVar()
f4c13 = IntVar()
f4c14 = IntVar()

#frm5 	RESIDUOS SÓLIDOS Y LODOS - 8

f5c1 = IntVar()
f5c2 = IntVar()
f5c3 = IntVar()
f5c4 = IntVar()
f5c5 = IntVar()
f5c6 = IntVar()
f5c7 = IntVar()
f5c8 = IntVar()

#frm6 	RESIDUOS PELIGROSOS - 3

f6c1 = IntVar()
f6c2 = IntVar()
f6c3 = IntVar()

#frm7 	FAUNA - 4

f7c1 = IntVar()
f7c2 = IntVar()
f7c3 = IntVar()
f7c4 = IntVar()

#frm8	FLORA - 43

f8c1 = IntVar()
f8c2 = IntVar()
f8c3 = IntVar()
f8c4 = IntVar()
f8c5 = IntVar()
f8c6 = IntVar()
f8c7 = IntVar()
f8c8 = IntVar()
f8c9 = IntVar()
f8c10 = IntVar()
f8c11= IntVar()
f8c12 = IntVar()
f8c13 = IntVar()
f8c14 = IntVar()
f8c15 = IntVar()
f8c16 = IntVar()
f8c17 = IntVar()
f8c18 = IntVar()
f8c19 = IntVar()
f8c20 = IntVar()
f8c21 = IntVar()
f8c22 = IntVar()
f8c23 = IntVar()
f8c24 = IntVar()
f8c25 = IntVar()
f8c26 = IntVar()
f8c27 = IntVar()
f8c28 = IntVar()
f8c29 = IntVar()
f8c30 = IntVar()
f8c31 = IntVar()
f8c32 = IntVar()
f8c33 = IntVar()
f8c34 = IntVar()
f8c35 = IntVar()
f8c36 = IntVar()
f8c37 = IntVar()
f8c38 = IntVar()
f8c39 = IntVar()
f8c40 = IntVar()
f8c41 = IntVar()
f8c42 = IntVar()
f8c43 = IntVar()

#frm9 	PAISAJÍSTICO 24

f9c1 = IntVar()
f9c2 = IntVar()
f9c3 = IntVar()
f9c4 = IntVar()
f9c5 = IntVar()
f9c6 = IntVar()
f9c7 = IntVar()
f9c8 = IntVar()
f9c9 = IntVar()
f9c10 = IntVar()
f9c11 = IntVar()
f9c12 = IntVar()
f9c13 = IntVar()
f9c14 = IntVar()
f9c15 = IntVar()
f9c16 = IntVar()
f9c17 = IntVar()
f9c18 = IntVar()
f9c19 = IntVar()
f9c20 = IntVar()
f9c21 = IntVar()
f9c22 = IntVar()
f9c23 = IntVar()
f9c24 = IntVar()


#frm10 ADQUISICIÓN DE SERVIDUMBRE 10

f10c1 = IntVar()
f10c2 = IntVar()
f10c3 = IntVar()
f10c4 = IntVar()
f10c5 = IntVar()
f10c6 = IntVar()
f10c7 = IntVar()
f10c8 = IntVar()
f10c9 = IntVar()
f10c10 = IntVar()

#frm11	COMUNICACIÓN Y PARTICIPACIÓN, EDUCACIÓN AMBIENTAL, RESCATE Y MONITOREO 18

f11c1 = IntVar()
f11c2 = IntVar()
f11c3 = IntVar()
f11c4 = IntVar()
f11c5 = IntVar()
f11c6 = IntVar()
f11c7 = IntVar()
f11c8 = IntVar()
f11c9 = IntVar()
f11c10 = IntVar()
f11c11 = IntVar()
f11c12 = IntVar()
f11c13 = IntVar()
f11c14 = IntVar()
f11c15 = IntVar()
f11c16 = IntVar()
f11c17 = IntVar()
f11c18 = IntVar()

#frm12	ADECUACIÓN DE INTERIORES Y EXTERIORES 10

f12c1 = IntVar()
f12c2 = IntVar()
f12c3 = IntVar()
f12c4 = IntVar()
f12c5 = IntVar()
f12c6 = IntVar()
f12c7 = IntVar()
f12c8 = IntVar()
f12c9 = IntVar()
f12c10 = IntVar()


#frm13	VIAL Y SEÑALIZACIÓN	33

f13c1 = IntVar()
f13c2 = IntVar()
f13c3 = IntVar()
f13c4 = IntVar()
f13c5 = IntVar()
f13c6 = IntVar()
f13c7 = IntVar()
f13c8 = IntVar()
f13c9 = IntVar()
f13c10 = IntVar()
f13c11 = IntVar()
f13c12= IntVar()
f13c13= IntVar()
f13c14= IntVar()
f13c15 = IntVar()
f13c16 = IntVar()
f13c17 = IntVar()
f13c18 = IntVar()
f13c19= IntVar()
f13c20 = IntVar()
f13c21 = IntVar()
f13c22 = IntVar()
f13c23 = IntVar()
f13c24 = IntVar()
f13c25 = IntVar()
f13c26 = IntVar()
f13c27 = IntVar()
f13c28 = IntVar()
f13c29 = IntVar()
f13c30 = IntVar()
f13c31 = IntVar()
f13c32 = IntVar()
f13c33 = IntVar()

#frm14 "SEGURIDAD INDUSTRIAL Y SALUD OCUPACIONAL" 36

f14c1 = IntVar()
f14c2 = IntVar()
f14c3 = IntVar()
f14c4 = IntVar()
f14c5 = IntVar()
f14c6 = IntVar()
f14c7 = IntVar()
f14c8 = IntVar()
f14c9 = IntVar()
f14c10 = IntVar()
f14c11= IntVar()
f14c12= IntVar()
f14c13= IntVar()
f14c14= IntVar()
f14c15= IntVar()
f14c16= IntVar()
f14c17= IntVar()
f14c18= IntVar()
f14c19= IntVar()
f14c20= IntVar()
f14c21= IntVar()
f14c22= IntVar()
f14c23= IntVar()
f14c24= IntVar()
f14c25= IntVar()
f14c26= IntVar()
f14c27= IntVar()
f14c28= IntVar()
f14c29= IntVar()
f14c30= IntVar()
f14c31= IntVar()
f14c32= IntVar()
f14c33= IntVar()
f14c34= IntVar()
f14c35= IntVar()
f14c36= IntVar()

#FRAME 15 PERMISOS Y LICENCIAS AMBIENTALES 11
f15c1 = IntVar()
f15c2 = IntVar()
f15c3 = IntVar()
f15c4 = IntVar()
f15c5 = IntVar()
f15c6 = IntVar()
f15c7 = IntVar()
f15c8 = IntVar()
f15c9 = IntVar()
f15c10 = IntVar()
f15c11= IntVar()

#


"//////////////////////////////////////////////////////////////////////////////////////////////////////"

#RADIOBUTTONS PARA DISPLAY DE FRAMES

menubar = Menubutton(app, text = "Click aquí para ver desplegar menú de Programas de Manejo Asociado", relief = RAISED, width = 64)
menubar.place(x = 50, y = 20)

menubar.menu = Menu(menubar, tearoff = 0)
menubar['menu'] = menubar.menu

menubar.menu.add_checkbutton(label = "Aguas de lluvias, escorrentía y cauces naturales", command = m1)
menubar.menu.add_checkbutton(label = "Agua para consumo", command = m2)
menubar.menu.add_checkbutton(label = "Residuos líquidos domésticos", command = m3)
menubar.menu.add_checkbutton(label = "Residuos de excavación y demolición", command = m4)
menubar.menu.add_checkbutton(label = "Residuos sólidos y lodos", command = m5)
menubar.menu.add_checkbutton(label = "Residuos peligrosos", command = m6)
menubar.menu.add_checkbutton(label = "Fauna", command = m7)
menubar.menu.add_checkbutton(label = "Flora", command = m8)
menubar.menu.add_checkbutton(label = "Paisajístico y morfológico", command = m9)
menubar.menu.add_checkbutton(label = "Adquisición de servidumbre y/o daños en infraestructura y mejoras", command = m10)
menubar.menu.add_checkbutton(label = "Comunicación y participación comunitaria", command = m11)
menubar.menu.add_checkbutton(label = "Adecuación de interiores y exteriores", command = m12)
menubar.menu.add_checkbutton(label = "Vial y Señalización", command = m13)
menubar.menu.add_checkbutton(label = "Seguridad industrial y salud ocupacional", command = m14)
menubar.menu.add_checkbutton(label = "Permisos y licencias ambientales", command = m15)

titlefont = ("Calibri", 13, 'bold')

text1 = Label(app, text = "Por favor, seleccione las medidas de manejo que tendrá el proyecto, cuando haya finalizado, de click en 'Hacer Presupuesto'", background = 'white', font = titlefont)
text1.place(x = 50, y = 50)

app.config(menu = menubar)

"//////////////////////////////////////////////////////////////////////////////////////////////////////"

"FRAME NÚMERO 1"

c1f1 = Checkbutton(frm1, text = "Construcción de cuneta lateral, en concreto de 21 Mpa, la cual tiene un espesor de 15 cm y un desarrollo de 0,60 m incluyendo llaves de confinamiento y recebos."
								+"Incluye refuerzo según detalle de diseño, además incluye excavación,\ncargue, botada, entresuelo base granular o similar, según diseño", onvalue = 1, offvalue = 0, 
								variable = f1c1, background = 'white', justify = 'left')
c1f1.place(x = 50, y = 80)

c2f1 = Checkbutton(frm1, text = "Construcción de cuneta trapezoidal en concreto de 21 Mpa, con espesor de 15 cm, base de 40 cm, incluye llaves de confinamiento y recebos. Incluye refuerzo"
	+"según detalle de diseño, excavación, nivelación,botada, entresuelo en base\ngranular o similar.", onvalue = 1, offvalue = 0, variable = f1c2, background = 'white', justify = 'left')
c2f1.place(x = 50, y = 120)

c3f1 = Checkbutton(frm1, text = "Construcción de rondas de coronación en sacos de polipropileno (suelo cemento 5:1, 60 cm x 70 cm). Este trabajo consiste en el transporte, suministro, "
	+"elaboración, manejo, almacenamiento y colocación de los materiales de construcción\nde rondas utilizando sacos de polipropileno o similar. También incluye las operaciones de "
	"alineamiento, excavación, conformación de la sección, suministro del material de relleno necesario y compactación del suelo de soporte.", onvalue = 1, offvalue = 0, variable = f1c3, background = 'white', justify = 'left')
c3f1.place(x = 50, y = 160)

c4f1  = Checkbutton(frm1, text = "Construcción de rondas de coronación trapezoidal en Geomembrana. Este trabajo consiste en el transporte, suministro, elaboración, manejo, almacenamiento "
	+"y colocación de los materiales de construcción de rondas utilizando Geomembrana\n HDPE o similar. También incluye las operaciones de alineamiento, excavación, conformación de la sección,"
	 +"suministro del material de relleno necesario y compactación del suelo de soporte.", onvalue = 1, offvalue = 0, variable = f1c4, background = 'white', justify = 'left')
c4f1.place(x = 50, y = 200)

c5f1 = Checkbutton(frm1,text = "Suministro, transporte e instalación de filtros para abatimiento de nivel freático con tubería perforada con un diámetro de 100 mm., con una sección de 0.5 '"
	+"x 0.5 m. Incluye geotextil NT 1600 y triturado de 1' y todos los demás elementos\npara su correcta construcción y funcionamiento.", onvalue = 1, offvalue = 0, variable = f1c5, background = 'white', justify = 'left')
c5f1.place(x = 50, y = 240)

c6f1 = Checkbutton(frm1, text = "Colocación de bolsacretos, concreto clase E.", onvalue = 1, offvalue = 0, variable = f1c6, background = 'white')
c6f1.place(x = 50, y = 280)

c7f1 = Checkbutton(frm1, text = "Colocación de costales de polipropileno con lleno de 10*20*60 cm, para protección de sumideros u obras de drenaje", onvalue = 1, offvalue = 0, variable = f1c7, background = 'white', justify = 'left')
c7f1.place(x = 50, y = 310)

c8f1 = Checkbutton(frm1, text = "Colocación de cuneta prefabricada en 'v' en concreto de 21 Mpa. 0.30 X 0.25 , modulada cada 0,80 m. Según ficha U180 del MEP según diseño OOPP Municipio de"
 +"Medelliín. Incluye suministro, transporte y colocación de los materiales,\nentresuelo 15 cm de piedra y 5 cm de arenilla y todos lo demás elementos necesario para su correcta construcción."
  +" No incluye refuerzo.", onvalue = 1, offvalue = 0, variable = f1c8, background = 'white', justify = 'left')
c8f1.place(x = 50, y = 340)

c9f1 = Checkbutton(frm1, text = "Desvío de la quebrada y manejo de aguas incluye transporte hasta la bocatoma.", onvalue = 1, offvalue = 0, variable = f1c9, background = 'white', justify = 'left')
c9f1.place(x = 50, y = 380)

c10f1 = Checkbutton(frm1, text = "Desvío de la quebrada, incluye excavaciones y colocación de sacos llenos de arena y tuberías PVC-alcantarillado de 12'' para encausar agua", onvalue = 1, offvalue = 0, variable = f1c10, background = 'white', justify = 'left')
c10f1.place(x = 50, y = 410)

c11f1 = Checkbutton(frm1, text = "Instalación de geotextil no tejido 1600", onvalue = 1, offvalue = 0, variable = f1c11, background = 'white', justify = 'left')
c11f1.place(x = 50, y = 440)

c12f1 = Checkbutton(frm1, text = "Limpieza de cauces, incluye retiro de todos los sedimentos, escombros, material vegetal y demás elementos extraños que se encuentren obstruyendo la sección del puente.", onvalue = 1, offvalue = 0, variable = f1c12, background = 'white', justify = 'left')
c12f1.place(x = 50, y = 470)

c13f1 = Checkbutton(frm1, text = "Manejo de aguas mediante el uso de sacos llenos con material de préstamo, para cruce subfluvial", onvalue = 1, offvalue = 0, variable = f1c13, background = 'white', justify = 'left')
c13f1.place(x = 50, y = 500)

c14f1 = Checkbutton(frm1, text = "Reparación de gaviones, reutilizando piedra existente.", onvalue = 1, offvalue = 0, variable = f1c14, background = 'white', justify = 'left')
c14f1.place(x = 50, y = 530)

c15f1 = Checkbutton(frm1, text = "Suministro, transporte y colocación de colchogavión.", onvalue = 1, offvalue = 0, variable = f1c15, background = 'white', justify = 'left')
c15f1.place(x = 50, y = 560)

c16f1 = Checkbutton(frm1, text = "Suministro, transporte y construcción de Gaviones, incluye transporte material.", onvalue = 1, offvalue = 0, variable = f1c16, background = 'white', justify = 'left')
c16f1.place(x = 50, y = 590)

"//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////"

#CHECKBUTTONS FRAME 2

c1f2 = Checkbutton(frm2, text = "Instalación de Planta de tratamiento en PRFV presurizada de 1 l/s, incluye, floculadores, sedimentadores, filtros, clarificación y todos los accesorios "
	+"necesarios para su adecuado funcionamiento.", onvalue = 1, offvalue = 0, variable = f2c1, background = 'white', justify = 'left')
c1f2.place(x = 50, y = 80)

c2f2 = Checkbutton(frm2, text = "Instalación de dispositivos para el ahorro y uso eficiente del agua", onvalue = 1, offvalue = 0, variable = f2c2, background = 'white', justify = 'left')
c2f2.place(x = 50, y = 110)

c3f2 = Checkbutton(frm2, text = "Suministro de agua potable para trabajadores", onvalue = 1, offvalue = 0, variable = f2c3, background = 'white', justify = 'left')
c3f2.place(x = 50, y = 140)

"//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////"

#CHECKBUTTONS FRAME 3

c1f3 = Checkbutton(frm3, text = "Alquiler de baño portátil tipo estándar (sin mantenimiento)", onvalue = 1, offvalue = 0, variable = f3c1, background = 'white', justify = 'left')
c1f3.place(x = 50, y = 80)

c2f3 = Checkbutton(frm3, text = "Alquiler de baño portátil tipo estándar (para 16 personas + 2 mantenimientos/semana)", onvalue = 1, offvalue = 0, variable = f3c2, background = 'white', justify = 'left')
c2f3.place(x = 50, y = 110)

c3f3 = Checkbutton(frm3, text = "Construcción de banño fijo para campamento (Según R.2400 de 1979: sanitario, lavamanos, orinal, ducha)", onvalue = 1, offvalue = 0, variable = f3c3, background = 'white', justify = 'left')
c3f3.place(x= 50, y = 140)

c4f3 = Checkbutton(frm3, text = "Construcción de baño provisional en ladrillo (4m2).", onvalue = 1, offvalue = 0, variable = f3c4, background = 'white', justify = 'left')
c4f3.place(x = 50, y = 170)

c5f3 = Checkbutton(frm3, text = "Compra de baño portátil tipo estándar", onvalue = 1, offvalue = 0, variable = f3c5, background = 'white', justify = 'left')
c5f3.place(x = 50, y = 200)

c6f3 = Checkbutton(frm3, text = "Mantenimiento y limpieza semanal de baño portátil tipo estándar", onvalue = 1, offvalue = 0, variable = f3c6, background = 'white', justify = 'left')
c6f3.place(x = 50, y = 230)

c7f3 = Checkbutton(frm3, text = "Suministro, transporte e instalación de tanque en fibra de vidrio con capacidad para 10 m3 con dimensiones de diámetro 2.60 metros, altura de 2 metros"
			+"tapa plana en la parte superior del tanque, fabricado en Resina poliéster semiflexible.\nFibra de vidrio Tela Matt 700 de 450 gramos/m2 y Woven Roving de 800, cilindro vertical"
			+"de fondo plano. Norma de fabricación 2888 Icontec. Incluye las perforaciones para succión, purga, rebose, llenado y según diseños hidráulicos.", onvalue = 1, offvalue = 0, variable = f3c7, background = 'white', justify = 'left')
c7f3.place(x = 50, y = 260)

c8f3 = Checkbutton(frm3, text = "Suministro, transporte e instalación de tanque Séptico con filtro anaerobio en P.R.F.V (Poliéster Reforzado con Fibra de Vidrio) de 1500 litros", onvalue = 1, offvalue = 0, variable = f3c8, background = 'white', justify = 'left')
c8f3.place(x = 50, y = 300)

c9f3 = Checkbutton(frm3, text = "Suministro, transporte y colocación de filtro perimetral de 0,40 metros de ancho (incluye triturado de diámetro de 25mm y tubería PVC novafort o similar"
								+" de diámetro de 160 mm.", onvalue = 1, offvalue = 0, variable = f3c9, background = 'white', justify = 'left')
c9f3.place(x= 50, y = 330)

c10f3 = Checkbutton(frm3, text = "Entrega a gestor de residuos líquidos (alcantarillado)", onvalue = 1, offvalue = 0, variable = f3c10, background = 'white', justify = 'left')
c10f3.place(x = 50, y = 360)

c11f3 = Checkbutton(frm3, text = "Construcción de lavadero de llantas en losa de concreto de 20 cm de espesor, de 3,0 metros x 1,50 metros con pendiente transversal hacia el centro y "
	+"pendiente longitudinal hacia un extremo, mínima del 2% apoyado en una capa de\nbase de 0,20 m compactada al 95% del proctor modificado . Incluye acero de refuerzo, excavación, cargue "
	+"y botada de material sobrante, tubería PVC de 4'' para desagüe y todos los demás materiales necesarios para su correcta construcción\ny funcionamiento según diseño. (Residuo líquido no domestico)", onvalue = 1, offvalue = 0, variable = f3c11, background = 'white', justify = 'left')
c11f3.place(x = 50, y = 390)

c12f3 = Checkbutton(frm3, text = "Otros - manejo de fuentes emisoras y receptoras de ruido y olores ofensivos", onvalue = 1, offvalue = 0, variable = f3c12, background = 'white', justify = 'left')
c12f3.place(x = 50, y = 440)

"//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////"

#CHECKBUTTONS FRAME 4

c1f4 = Checkbutton(frm4, text = "Pago de derecho de depósito particular", onvalue = 1, offvalue = 0, variable = f4c1, background = 'white', justify = 'left')
c1f4.place(x = 50, y = 80)

c2f4 = Checkbutton(frm4, text = "Retiro de aparatos sanitarios, incluye el cargue, transporte, botada o recuperación de aparatos sanitarios, lavamanos, lavaderos, orinales."
	+" Incluye botada en botaderos oficiales y la recuperación de los materiales aprovechables \ny/o su transporte hasta la bodega o el sitio que indique la interventoría.", onvalue = 1, offvalue = 0, variable = f4c2, background = 'white', justify = 'left')
c2f4.place(x = 50, y = 110)

c3f4 = Checkbutton(frm4, text = "RETIRO DE CANOAS, RUANAS, BAJANTES y TUBERÍAS. Incluye el cargue, transporte, botada escombros en botaderos oficiales, recuperación de los"
	+" materiales aprovechables y su transporte hasta el sitio que lo indique la interventoría.", onvalue = 1, offvalue = 0, variable = f4c3, background = 'white', justify = 'left')
c3f4.place(x = 50, y = 150)

c4f4 = Checkbutton(frm4, text = "Retiro de cerchas y estructura techo en lámina galvanizada. Incluye el cargue, transporte, botada escombros en botaderos autorizados por el "
	+"municipio, recuperación de los materiales aprovechables y su transporte hasta el sitio que lo\nindique la interventoría.", onvalue = 1, offvalue = 0, variable = f4c4, background = 'white', justify = 'left')
c4f4.place(x = 50, y = 180)

c5f4 = Checkbutton(frm4, text = "Retiro de cerramiento en malla eslabonada. Incluye el retiro, cargue y transporte de los materiales, recuperación de los materiales aprovechables"
	+" como tubería, malla eslabonada y alambre de púas y su transporte hasta el sitio que indique\n la interventoría, demolición de concreto, cargue, transporte y botada de escombros"
	+" provenientes de este retiro en botaderos autorizados por el municipio o donde indique la interventoría.", onvalue = 1, offvalue = 0, variable = f4c5, background = 'white', justify = 'left')
c5f4.place(x = 50, y = 220)

c6f4 = Checkbutton(frm4, text = "Retiro de cubierta en teja de asbesto-cemento, teja plástica o teja similar. Incluye cargue, transporte, botada o recuperación de cerchas o componentes"
		+ " metálicos de soporte del sistema, cargue, transporte y botada de escombros\nen botaderos destinados por el municipio, recuperación de los materiales aprovechables o su transporte"
		"hasta el sitio que lo indique la interventoría. Medido en proyección horizontal.", onvalue = 1, offvalue = 0, variable = f4c6, background = 'white', justify = 'left')
c6f4.place(x = 50, y = 260)

c7f4 = Checkbutton(frm4, text = "RETIRO DE CUBIERTA EN TEJA DE BARRO. Incluye el cargue, transporte, botada o recuperación de fieltro, tablilla, alfardas, cargueras y soleras, cargue,"
+" transporte y botada de escombros, recuperación de los materiales aprovechables\no su transporte hasta el sitio que lo indique la interventoría. Su medida es en proyección horizontal", onvalue = 1, offvalue = 0, variable = f4c7, background = 'white', justify = 'left')
c7f4.place(x = 50, y = 300)

c8f4 = Checkbutton(frm4, text = "Retiro de pasamanos metálico en cualquier diseño, metal y peso. Incluye demolición base de anclaje y todos los demás elementos necesarios para su"
+ " efectivo retiro, recuperación del material aprovechable y su transporte hasta el\nsitio que indique la interventoría, cargue, transporte y botada del material proveniente de la "
+"demolición y que no se pueda recuperar, en botaderos destinado por el municipio o donde indique la interventoría.", onvalue = 1, offvalue = 0, variable = f4c8, background = 'white', justify = 'left')
c8f4.place(x = 50, y = 340)

c9f4 = Checkbutton(frm4, text = "RETIRO DE PLACA INSIGNE EXISTENTE. Incluye cargue, transporte hasta el sitio que lo indique la interventoría, cargue, transporte y botada de escombros"
+" y materiales sobrantes en botaderos oficiales o donde lo indique la interventoría.", onvalue = 1, offvalue = 0, variable = f4c9, background = 'white', justify = 'left')
c9f4.place(x = 50, y = 380)

c10f4 = Checkbutton(frm4, text = "Retiro de puertas (marco y ala) metálicas, en aluminio, en madera o puerta reja. Incluye el retiro, cargue, transporte, botada de escombros en botaderos"
+" autorizados por el municipio y recuperación de los materiales aprovechables y su \ntransporte hasta la bodega o el sitio que lo indique la interventoría. Ancho variable desde 0,60 a 1,20 m.", onvalue = 1, offvalue = 0, variable = f4c10, background = 'white', justify = 'left')
c10f4.place(x = 50, y = 410)

c11f4 = Checkbutton(frm4, text = "RETIRO DE TUBERÍA DE CUALQUIER DIÁMETRO Y TIPO enterradas y/o colgadas. Incluye el cargue y transporte de los materiales aprovechables hasta la bodega"
	+" o donde lo indique la interventoría, el cargue transporte y botada de los\nescombros generados en botaderos oficiales o donde lo indique la interventoría.", onvalue = 1, offvalue = 0, background = 'white', variable = f4c11, justify= 'left')
c11f4.place(x = 50, y = 450)

c12f4 = Checkbutton(frm4, text = "Retiro de ventanas con vidrio, metálicas, en aluminio, en madera o ventana reja. Incluye botada de escombros en botaderos autorizados por el municipio"
+" y recuperación de los materiales aprovechables y su transporte hasta el sitio\nque lo indique la interventoría. Dimensión variable.", onvalue = 1, offvalue = 0, variable = f4c12, background = 'white', justify = 'left')
c12f4.place(x = 50, y = 490)

c13f4 = Checkbutton(frm4, text = "Retiro, cargue, transporte y botada de escombros, incluye, el cargue con maquina, transporte interno y externo y botada de material tipo escombro en "
	+"los sitios autorizados por el municipio o donde lo indique la interventoría y su\nmedida será en el sitio.", onvalue = 1, offvalue = 0, variable = f4c13, background = 'white', justify = 'left')
c13f4.place(x = 50, y = 530)

c14f4 = Checkbutton(frm4, text = "Retiro, cargue, transporte, botada de Tubería en PVC de aguas lluvias y/o residuales. Incluye transporte y botada del material.", onvalue = 1, offvalue = 0, variable = f4c14, background = 'white', justify = 'left')
c14f4.place(x = 50, y = 570)

"//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////"

c1f5 = Checkbutton(frm5, text = "Canecas de 5 galones", onvalue = 1, offvalue = 0, variable = f5c1, background = 'white', justify = 'left')
c1f5.place(x = 50, y = 80)

c2f5 = Checkbutton(frm5, text = "Caneca con tapa de 37 litros", onvalue = 1, offvalue = 0, variable = f5c2, background = 'white', justify = 'left')
c2f5.place(x = 50, y = 110)

c3f5 = Checkbutton(frm5, text = "Canecas de 55 galones para campamento", onvalue = 1, offvalue = 0, variable = f5c3, background = 'white', justify = 'left')
c3f5.place(x = 50, y = 140)

c4f5 = Checkbutton(frm5, text = "Construcción de juego de tanques sedimentadores en concreto de 21 Mpa, apoyado sobre el terreno, compuesto de dos tanques de concreto de 0,50 m de ancho"
+" x 0,50 m de largo x 0,4 m de profundidad (medidas internas) \ncon un espesor de 0,07m, separados 1,0 m entre las caras internas mas cercanas, incluye excavación, cargue y botada de material"
+" sobrante, losa pendentada perimetral a cada tanque de 0,5 m de ancho x 0,07 m de espesor,\n tubería PVC 4'' entre tanques y 15 m entre el segundo tanque y el sitio de disposición final de las "
+"aguas. Incluye acero de refuerzo, materiales y todo lo necesario para su correcta construcción y funcionamiento según diseño.", onvalue = 1, offvalue = 0, variable = f5c4, background = 'white', justify = 'left')
c4f5.place(x = 50, y = 170)

c5f5 = Checkbutton(frm5, text = "Juego de tres recipientes para campamento (punto ecológico)", onvalue = 1, offvalue = 0, variable = f5c5, background = 'white', justify = 'left')
c5f5.place(x = 50, y = 230)

c6f5 = Checkbutton(frm5, text = "Kit de bolsas de color azul, verde y gris (50 unidades de cada color)", onvalue = 1, offvalue = 0, variable = f5c6, background = 'white', justify = 'left')
c6f5.place(x = 50, y = 260)

c7f5 = Checkbutton(frm5, text = "Limpieza y mantenimiento del area de abastecimiento, limpieza manual externa y superficial del embalse existente y disposición final del material extraído", onvalue = 1, offvalue = 0, variable = f5c7, background = 'white', justify = 'left')
c7f5.place(x = 50, y = 290)

c8f5 = Checkbutton(frm5, text = "Plástico negro calibre 4 ancho de 2 m", onvalue = 1, offvalue = 0, variable = f5c8, background = 'white', justify = 'left')
c8f5.place(x = 50, y = 320
	)
"//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////"

#FRAME 6

c1f6 = Checkbutton(frm6, text = "Bolsas plásticas color rojo", onvalue = 1, offvalue = 0, variable = f6c1, background = 'white', justify = 'left')
c1f6.place(x = 50, y = 80)

c2f6 = Checkbutton(frm6, text = "Retiro de limunarias fluorescentes. Incluye cargue, transporte, botada en botaderos autorizados por el municipio y recuperación de los materiales "
	+"aprovechables y su transporte hasta el sitio que lo indique la interventoría.", onvalue = 1, offvalue = 0, variable = f6c2, background = 'white', justify = 'left')
c2f6.place(x = 50, y = 110)

c3f6 = Checkbutton(frm6, text = "Pago por transporte, tratamiento y disposición final a empresa gestora de RESPEL", onvalue = 1, offvalue = 0, variable = f6c3, background = 'white', justify = 'left')
c3f6.place(x = 50, y = 140)

"//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////"

#FRAME 7

c1f7 = Checkbutton(frm7, text = "Instalación de señales de alerta para la protección de la fauna (p.e. desviadores de vuelo en líneas de transmisión o grandes ventanales)", onvalue = 1, offvalue = 0, variable = f7c1, background = 'white', justify = 'left')
c1f7.place(x = 50, y = 80)

c2f7 = Checkbutton(frm7, text = "Construcción de pasos para fauna", onvalue = 1, offvalue = 0, variable = f7c2, background = 'white', justify = 'left')
c2f7.place(x = 50, y = 110)

c3f7 = Checkbutton(frm7, text = "Repoblamiento de fauna", onvalue = 1, offvalue = 0, variable = f7c3, background = 'white', justify = 'left')
c3f7.place(x = 50, y = 140)

c4f7 = Checkbutton(frm7, text = "Salvamento de fauna", onvalue = 1, offvalue = 0, variable = f7c4, background = 'white', justify = 'left')
c4f7.place(x = 50, y = 170)

"//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////"

#FRAME 8

next1 = Button(frm8, text = "Siguiente Página", command = m82, width = 20)
next1.place(x = 1200, y = 25)

next2 = Button(frm82, text = "Siguiente Página", command = m83, width = 20)
next2.place(x= 1200, y = 55)

back2 = Button(frm83, text = "Página anterior", command = m82, width = 20)
back2.place(x = 1200, y = 25)

back = Button(frm82, text = "Página anterior", command = m8, width = 20)
back.place(x = 1200, y = 25)

c1f8 = Checkbutton(frm8, text = "Plantación de arbustos ornamentales de 1 m de altura, cobertura en coleo, incluye excavación, tierra abonada.", onvalue = 1, offvalue = 0, variable = f8c1, background = 'white', justify = 'left')
c1f8.place(x = 50, y = 80)

c2f8 = Checkbutton(frm8, text = "Poda de individuos arbóreos", onvalue = 1, offvalue = 0, variable = f8c2, background = 'white', justify = 'left')
c2f8.place(x = 50, y = 110)

c3f8 = Checkbutton(frm8, text = "Revegetalización y protección con biomortero de espesor 2,4 cms y semilla B.D + Rg (Braquiaria Decomeus + Ray Grass), semilla Kk + E (Kikuyo + Estrella Africana)", onvalue = 1, offvalue = 0, variable = f8c3, background = 'white', justify = 'left')
c3f8.place(x = 50, y = 140)

c4f8 = Checkbutton(frm8, text = "Revegetalización de taludes con agromanto de fique con brachiaria decumbens para sembrar en sitios hasta 2000 m de altura snm. Consiste en la recuperación"
+" de la estabilidad del talud mediante la siembra de gramíneas (pasto) y leguminosas.\nEl trabajo incluye la preparación de la superficie, la revegetalización y el mantenimiento de las zonas"
+" intervenidas hasta el recibo definitivo de las obras.", onvalue = 1, offvalue = 0, variable = f8c4, background = 'white', justify = 'left')
c4f8.place(x = 50, y = 170)

c5f8 = Checkbutton(frm8, text = "Revegetalización de taludes con agromanto de fique con Reygrass pasares, para sembrar en sitios con alturas mayores de 2.000 mts de altura snm", onvalue = 1, offvalue = 0, variable = f8c5, background = 'white', justify = 'left')
c5f8.place(x = 50, y = 210)

c6f8 = Checkbutton(frm8, text = "Revegetalización de taludes con hidrosiembra manual", onvalue = 1, offvalue = 0, variable = f8c6, background = 'white', justify = 'left')
c6f8.place(x = 50, y = 240)

c7f8 = Checkbutton(frm8, text = "Revegetalización de taludes con hidrosiembra mecánica, el producto se aplica en capas de 2cm de espesor", onvalue = 1, offvalue = 0, variable = f8c7, background = 'white', justify = 'left')
c7f8.place(x = 50, y = 270)

c8f8 = Checkbutton(frm8, text = "Revegetalización de zonas planas y/o zonas de depósito con estolones de pasto de la zona. Este trabajo consiste en la plantación de estolones de pasto"
+" o semillas sobre depósitos de material o (zonas planas) sobrante de explanaciones \no de extracción de derrumbes (botaderos), taludes de terraplenes, en los sitios indicados por el "
+"Interventor. El trabajo incluye además, la conservación de las áreas empradizadas hasta el recibo definitivo de los trabajos.", onvalue = 1, offvalue = 0, variable = f8c8, background = 'white', justify = 'left')
c8f8.place(x = 50, y = 300)

c9f8 = Checkbutton(frm8, text = "Revegetalización de zonas planas y/o zonas de depósito con semilla certificada de gramíneas.", onvalue = 1, offvalue = 0, variable = f8c9, background = 'white', justify = 'left')
c9f8.place(x = 50, y = 340)

c10f8 = Checkbutton(frm8, text = "Revegetalización y estabilización con vetiver, 6 plántulas por m2, incluye abono orgánico y fertilizante para dos mantenimientos. Incluye riego y resiembra a los 30 días.", onvalue = 1, offvalue = 0, variable = f8c10, background = 'white', justify = 'left')
c10f8.place(x = 50, y = 370)

c11f8 = Checkbutton(frm8, text = "Suministro de Cisco de Arroz por pacas", onvalue = 1, offvalue = 0, variable = f8c11, background = 'white', justify = 'left')
c11f8.place(x = 50, y = 400)

c12f8 = Checkbutton(frm8, text = "Suministro de pulpa descompuesta por bultos", onvalue = 1, offvalue = 0, variable = f8c12, background = 'white', justify = 'left')
c12f8.place(x = 50, y = 430)

c13f8 = Checkbutton(frm8, text = "Suministro de plantas tipo LLUVIA DE ORO", onvalue = 1, offvalue = 0, variable = f8c13, background = 'white', justify = 'left')
c13f8.place(x = 50, y = 460)

c14f8 = Checkbutton(frm8, text = "Suministro de plantas tipo COPA DE ORO", onvalue = 1, offvalue = 0, variable = f8c14, background = 'white', justify = 'left')
c14f8.place(x = 50, y = 490)

c15f8 = Checkbutton(frm8, text = "Suministro de plantas tipo TUMBERQUIAS", onvalue = 1, offvalue = 0, variable = f8c15, background = 'white', justify = 'left')
c15f8.place(x = 50, y = 520)

c16f8 = Checkbutton(frm8, text = "Suministro y colocación de Engramado con cespedones en gramalote maní forrajero", onvalue = 1, offvalue = 0, variable = f8c16, background = 'white', justify = 'left')
c16f8.place(x = 50, y = 550)

c17f8 = Checkbutton(frm82, text = "Suministro de plantas tipo PALMA BAMBÚ", onvalue = 1, offvalue = 0, variable = f8c17, background = 'white', justify = 'left')
c17f8.place(x = 55, y = 80)

c18f8 = Checkbutton(frm82, text = "Suministro y siembra de GRAMAS CULTIVADAS TIPO Césped San Agustín, grama Bermuda, grama pennisetum enano, entre otras, según especificaciones. "
	+"Se debe garantizar prendimiento con mantenimiento inicial y riego constante durante \ntres meses. Incluye nivelación hasta 10 cms.", onvalue = 1, offvalue = 0, variable = f8c18, background = 'white', justify = 'left')
c18f8.place(x = 50, y = 110)

c19f8 = Checkbutton(frm82, text = "Suministro y siembra de árboles de especies nativas, incluye limpieza y adecuación del terreno, trazado, plateo, ahoyado y fertilización. "
	+"Árboles nativos de altura promedio entre 0,6 y 1,2 metros", onvalue = 1, offvalue = 0, variable = f8c19, background = 'white', justify = 'left')
c19f8.place(x = 50, y = 150)

c20f8 = Checkbutton(frm82, text = "Suministro, transporte e instalación de grama tipo macana, de 1.0 - 2000 m2, para conformación de zonas verdes. Incluye conformación, "
	+"nivelación de la superficie, regado y todo lo necesario hasta su total prendimiento.", onvalue = 1, offvalue = 0, variable = f8c20, background = 'white', justify = 'left')
c20f8.place(x = 50, y = 180)

c21f8 = Checkbutton(frm82, text = "Establecimiento de cercos: Suministro, transporte e instalación de cerco en alambre de púas con postes de madera.", onvalue = 1, offvalue = 0, variable = f8c21, background = 'white', justify = 'left')
c21f8.place(x = 50, y = 210)

c22f8 = Checkbutton(frm82, text = "Suministro, transporte y siembra de especies forestales, con una altura mínima de 2 a 2,50 m. Comprende las actividades de amarre, transporte, mano de "
	+"obra, 50 gramos de triple 15, 10 gramos de bórax y 15 gramos de estockosor.\nLa excavación se pagara en el Ítem respectivo. Si la siembra se realiza en época de verano, se debe "
	+"suministrar riego diario hasta que se garantice su total prendimiento, en caso de mortalidad, se debe reponer el árbol por parte del contratista.", onvalue = 1, offvalue = 0, variable = f8c22, background = 'white', justify = 'left')
c22f8.place(x = 50, y = 240)

c23f8 = Checkbutton(frm82, text = "Suministro, transporte y siembra de PALMA REAL con una altura mínima 3.50 m a 4.00 m. Comprende las actividades de amarre, transporte, mano de obra, "
	+"50 gramos de triple 15, 10 gramos de bórax y 15 gramos de estockosor.\nLa excavación se pagara en el Ítem respectivo. Si la siembra se realiza en época de verano, se debe suministrar"
	+" riego diario hasta que se garantice su total prendimiento, en caso de mortalidad, se debe reponer el árbol sin \nque ello sea un costo adicional.", onvalue = 1, offvalue = 0, variable = f7c4, background = 'white', justify = 'left')
c23f8.place(x = 50, y = 280)

c24f8 = Checkbutton(frm82, text = "Suministro, transporte y siembra de arboles h=1.5 m tales como ARAUCARIA, GUAYACÁN ROSADO o PALO BONITO, incluye tierra abonada y todo lo requerido para 2"
	+"la correcta siembra. Si la siembra se realiza en época de verano, \nse debe suministrar riego diario hasta que se garantice su prendimiento. en caso de mortalidad, se debe reponer el árbol"
	+" sin que ello sea un costo adicional.", onvalue = 1, offvalue = 0, variable = f8c24, background = 'white', justify = 'left')
c24f8.place(x = 50, y = 330)

c25f8 = Checkbutton(frm82, text = "Suministro, transporte y siembra de árboles de porte mediano (Níspero de Japón, Carbonero, pero de agua) h=3, metros, Incluye tierra abonada y "
	+"todo lo requerido para la correcta siembra. Se debe suministrar riesgo diario hasta que\nse garantice su prendimiento. En caso de mortalidad, se debe reponer el árbol.", onvalue = 1, offvalue = 0, variable = f8c25, background = 'white', justify = 'left')
c25f8.place(x= 50, y = 370)

c26f8 = Checkbutton(frm82, text = "Suministro, transporte y siembra de Acacia Amarilla, de 1.8 metros de altura. Incluye actividades de excavación en hoyos de 40x40 cm, preparación "
	+"de materiales, tutores, transporte, acarreo interno, mano de obra. Se debe\nsuministrar riego diario hasta que se gerantice su supervivencia.", onvalue = 1, offvalue = 0, variable = f8c26, background = 'white', justify = 'left')
c26f8.place(x= 50, y = 410)

c27f8 = Checkbutton(frm82, text = "Suministro, transporte y siembra de Azahar de la India, de 1,5 metros de altura. Incluye actividades de excavación en hoyos de 40x40 cm, preparación"
+" de materiales, tutores, transporte, acarreo interno, mano de obra. Se debe suministrar\nriego diario hasta que se gerantice su supervivencia.", onvalue = 1, offvalue = 0, variable = f8c27, background = 'white', justify = 'left')
c27f8.place(x= 50, y = 450)

c28f8 = Checkbutton(frm82, text = "Suministro, transporte y siembra de Azuceno de la India, de 1,5 metros de altura. Incluye actividades de excavación en hoyos de 40x40 cm, preparación "
	+"de materiales, tutores, transporte, acarreo interno, mano de obra. Se debe suministrar\n riego diario hasta que se gerantice su supervivencia.", onvalue = 1, offvalue = 0, variable = f8c28, background = 'white', justify = 'left')
c28f8.place(x= 50, y = 490)

c29f8 = Checkbutton(frm82, text = "Suministro, transporte y siembra de Carbonero, de 1,5 metros de altura. Incluye actividades de excavación en hoyos de 40x40 cm, preparación de materiales,"
	+" tutores, transporte, acarreo interno, mano de obra. Se debe suministrar\nriego diario hasta que se gerantice su supervivencia.", onvalue = 1, offvalue = 0, variable = f8c29, background = 'white', justify = 'left')
c29f8.place(x= 50, y = 530)

c30f8 = Checkbutton(frm83, text = "Suministro, transporte y siembra de Flor de Cera, de 1,5 metros de altura. Incluye actividades de excavación en hoyos de 40x40 cm, preparación de "
	+"materiales, tutores, transporte, acarreo interno, mano de obra. Se debe suministrar\n riego diario hasta que se gerantice su supervivencia.", onvalue = 1, offvalue = 0, variable = f8c30, background = 'white', justify = 'left')
c30f8.place(x= 55, y = 80)

c31f8 = Checkbutton(frm83, text = "Suministro, transporte y siembra de Fragipan, de 1,5 metros de altura. Incluye actividades de excavación en hoyos de 40x40 cm, preparación de materiales,"
	+" tutores, transporte, acarreo interno, mano de obra. Se debe suministrar\n riego diario hasta que se gerantice su supervivencia.", onvalue = 1, offvalue = 0, variable = f8c31, background = 'white', justify = 'left')
c31f8.place(x= 50, y = 120)

c32f8 = Checkbutton(frm83, text = "Suministro, transporte y siembra de Galán de Noche, de 1,5 metros de altura. Incluye actividades de excavación en hoyos de 40x40 cm, preparación de "
	+"materiales, tutores, transporte, acarreo interno, mano de obra. Se debe suministrar\n riego diario hasta que se gerantice su supervivencia.", onvalue = 1, offvalue = 0, variable = f8c32, background = 'white', justify = 'left')
c32f8.place(x= 50, y = 160)

c33f8 = Checkbutton(frm83, text = "Suministro, transporte y sembra de arboles GUAYACÁN, CARBONEROS h=3,0 metros. Comprende actividades piloneo, encostalado o entablidllado, amarre, "
	+"transporte, mano e obra, 50 gramos de stocksorb, 200 gramos de triple 15, \n40 gramos de bórax, excavación, tierra abonada y todo lo requerido para la correcta siembra.", onvalue = 1, offvalue = 0, variable = f8c33, background = 'white', justify = 'left')
c33f8.place(x= 50, y = 200)

c34f8 = Checkbutton(frm83, text = "Suministro, transporte y sembra de árbol tipo CEIBA VERDE de una altura de 4,0 metros apróximadamente. Incluye tierra abonada y todolo requerido para "
	+"la correcta siembra. Se debe suministrar riesgo diario hasta que se garantice\n su prendimiento. En caso de mortalidad, se debe reponer el árbol.", onvalue = 1, offvalue = 0, variable = f8c34, background = 'white', justify = 'left')
c34f8.place(x= 50, y = 240)

c35f8 = Checkbutton(frm83, text = "Tala de árboles diámetro menor de 20 cm - altura hasta 5 mt. Incluye motosierra, retiro de raíces completas, transporte y disposición del material "
	+"resultante al sitio que indiquen la interventoría (incluye cargue y retiro)", onvalue = 1, offvalue = 0, variable = f8c35, background = 'white', justify = 'left')
c35f8.place(x= 50, y = 280)

c36f8 = Checkbutton(frm83, text = "Tala de árboles con diámetro mayor a 20 cm (incluye cargue y retiro)", onvalue = 1, offvalue = 0, variable = f8c36, background = 'white', justify = 'left')
c36f8.place(x= 50, y = 310)

c37f8 = Checkbutton(frm83, text = "Tala de árboles bajo cualquier condición, ALTURA de 1 a 3 m. Incluye trozado, chipiado, retiro de raíces completas, transporte y disposición del material"
+" resultante al sitio que indiquen las autoridades \ncompetentes y la interventoría(incluye cargue y retiro)", onvalue = 1, offvalue = 0, variable = f8c37, background = 'white', justify = 'left')
c37f8.place(x= 50, y = 340)

c38f8 = Checkbutton(frm83, text = "Tala de árboles bajo cualquier condición, ALTURA de 3 a 6 m. Incluye trozado, chipiado, retiro de raíces completas, transporte y disposición del material"
+" resultante al sitio que indiquen las autoridades \ncompetentes y la interventoría (incluye cargue y retiro)", onvalue = 1, offvalue = 0, variable = f8c38, background = 'white', justify = 'left')
c38f8.place(x= 50, y = 380)

c39f8 = Checkbutton(frm83, text = "Tala de árboles bajo cualquier condición, ALTURA de 6 a 8 m. Incluye trozado, chipiado, retiro de raíces completas, transporte y disposición del material"
+" resultante al sitio que indiquen las autoridades \ncompetentes y la interventoría (incluye cargue y retiro)", onvalue = 1, offvalue = 0, variable = f8c39, background = 'white', justify = 'left')
c39f8.place(x= 50, y = 420)

c40f8 = Checkbutton(frm83, text = "Tala de árboles bajo cualquier condición, ALTURA de 10,0 a 15,0 m. Incluye trozado, retiro de raíces completas, transporte y disposición del material"
+" resultante al sitio que indiquen las autoridades \ncompetentes y la interventoría. Se realizará en aquellos arboles que dada su ubicación interfieren con el proyecto o que ofrezcan algún riesgo para la comunidad y que no justifique su trasplante (incluye cargue y retiro)", onvalue = 1, offvalue = 0, variable = f8c40, background = 'white', justify = 'left')
c40f8.place(x= 50, y = 460)

c41f8 = Checkbutton(frm83, text = "Tala de árboles, se realizará en aquellos árboles que dada su ubicación son interferidos por el proyecto o que a partir de la autorización de la autoridad"
+" ambiental competente, ofrezcan algún tipo deriesgo\n para la comunidad y en donde el trasplante sea inviable.", onvalue = 1, offvalue = 0, variable = f8c41, background = 'white', justify = 'left')
c41f8.place(x= 50, y = 500)

c42f8 = Checkbutton(frm83, text = "TRASPLANTE, CARGUE Y TRANSPORTE de ARBOLES bajo cualquier condición, para arboles con una ALTURA entre 3.0 a 4.9. Para recorridos MENORES A 3 KM. "
	+"Incluye prepiloneo, piloneo, amarre con costales de fique o entablillado,\n cicatrizante, hidroretenedor, fertilización liquida que permita la asimilación rápida de los nutrientes," 
	+"transporte interno del árbol, tierra abonada en el lugar de su nueva ubicación\n y disposición del material resultante al sitio que indiquen las autoridades competentes y la"
	+"interventoría. Se realizará en aquellos arboles que dada su ubicación interfieren con el proyecto y que justifique su trasplante.", onvalue = 1, offvalue = 0, variable = f8c42, background = 'white', justify = 'left')
c42f8.place(x= 50, y = 540)

c43f8 = Checkbutton(frm83, text = "Transporte y mano de obra calificada para la siembra y capacitación de personal en jardinería por un día", onvalue = 1, offvalue = 0, variable = f8c43, background = 'white', justify = 'left')
c43f8.place(x= 50, y = 590)


"//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////"

#FORMULARIO 9

next9 = Button(frm9, text = "Siguiente Página", command = m92)
next9.place(x = 1200, y = 50)

back92 = Button(frm92, text = "Página Anterior", command = m9)
back92.place(x = 1200, y = 50)

c1f9 = Checkbutton(frm9, text = "Adecuación del terreno, incluye: mano de obra, herramienta, disposición del material sobrante y todo lo necesario para su correcta ejecución", onvalue = 1, offvalue = 0, background = 'white', justify = 'left', variable = f9c1 )
c1f9.place(x = 50, y = 80)

c2f9 = Checkbutton(frm9, text = "Aseo general de obra. Incluye hidrolavadora, detergente, acido y lo todo lo que se requiera para su correcta ejecución.", onvalue = 1, offvalue = 0, background = 'white', justify = 'left', variable = f9c2 )
c2f9.place(x = 50, y = 110)

c3f9 = Checkbutton(frm9, text = "Agromanto fique y fibra sintética, incluye: suministro, transporte, instalación, material vegetal, abono, semillas e hidroretenedores ( con una resistencia a la tensión de 1,8 kN/m y elogación máxima del 15%. Incluye traslapos donde se consideren pertinentes y todo lo necesario para su correcta construcción).", onvalue = 1, offvalue = 0, background = 'white', justify = 'left', variable = f9c3 )
c3f9.place(x = 50, y = 140)

c4f9 = Checkbutton(frm9, text = "Construcción de disipadores de energía y sedimentador en gaviones con recubrimiento. Esta actividad consiste en el suministro de materiales y equipos, así como la colocación de formaletas, preparación y vaciado de mezclas de concreto y mortero, colocación de gaviones, acabado y curado de las obras y, en general, todas las operaciones requeridas para su terminación, de acuerdo con los planos, y las instrucciones del interventor.", onvalue = 1, offvalue = 0, background = 'white', justify = 'left', variable = f9c4 )
c4f9.place(x = 50, y = 170)

c5f9 = Checkbutton(frm9, text = "Construcción de muro de contención en gaviones, incluye cantaste triple torsión, alambre galvanizado, tensores, piedra para gavión, asesoría técnica y demás materiales para su ejecución, según diseños y especificaciones técnicas exigidas por INVIAS", onvalue = 1, offvalue = 0, background = 'white', justify = 'left', variable = f9c5 )
c5f9.place(x = 50, y = 200)

c6f9 = Checkbutton(frm9, text = "Construcción de muro de contención en muro reforzado con geotextil", onvalue = 1, offvalue = 0, background = 'white', justify = 'left', variable = f9c6 )
c6f9.place(x = 50, y = 230)

c7f9 = Checkbutton(frm9, text = "Empedrado para taludes.", onvalue = 1, offvalue = 0, background = 'white', justify = 'left', variable = f9c7 )
c7f9.place(x = 50, y = 260)

c8f9 = Checkbutton(frm9, text = "Excavaciones para estabilizacion de taludes", onvalue = 1, offvalue = 0, background = 'white', justify = 'left', variable = f9c8 )
c8f9.place(x = 50, y = 290)

c9f9 = Checkbutton(frm9, text = "Instalación de malla gallinero", onvalue = 1, offvalue = 0, background = 'white', justify = 'left', variable = f9c9 )
c9f9.place(x = 50, y = 320)

c10f9 = Checkbutton(frm9, text = "Instalación de mortero ecológico", onvalue = 1, offvalue = 0, background = 'white', justify = 'left', variable = f9c10)
c10f9.place(x = 50, y = 350)

c11f9 = Checkbutton(frm9, text = "Instalación de trinchos en madera. Esta actividad consiste en el suministro, transporte, colocación, amarre y aseguramiento de los tacos de madera. Está constituida por una pantalla de máximo 1,50 m de ancho, tacos de madera de 0,05 a 0,10 m de diámetro, y de 1,20 a 1,30 m de longitud, tablas de madera común o esterilla de guadua y una cobertura de geotextil no tejido NT 2000 en la parte posterior del trincho que actúa como pantalla para evitar el paso de finos.", onvalue = 1, offvalue = 0, background = 'white', justify = 'left', variable = f9c11)
c11f9.place(x = 50, y = 380)

c12f9 = Checkbutton(frm9, text = "Perfilación de vía. Incluye escarificación, nivelación y compactación de la superficie.", onvalue = 1, offvalue = 0, background = 'white', justify = 'left', variable = f9c12)
c12f9.place(x = 50, y = 410)

c13f9 = Checkbutton(frm9, text = "Sellado de grietas con material de limo y cal (Grieta máximo 15*60 cm)", onvalue = 1, offvalue = 0, background = 'white', justify = 'left', variable = f9c13)
c13f9.place(x = 50, y = 440)

c14f9 = Checkbutton(frm9, text = "Suministro  aplicación de lodo fertilizado y agromanto, incluye semilla", onvalue = 1, offvalue = 0, background = 'white', justify = 'left', variable = f9c14)
c14f9.place(x = 50, y = 470)

c15f9 = Checkbutton(frm9, text = "Suministro de matero (alcorque) en concreto a la vista de 0,40*0,40*1,00 m de largo", onvalue = 1, offvalue = 0, background = 'white', justify = 'left', variable = f9c15)
c15f9.place(x = 50, y = 500)

c16f9 = Checkbutton(frm9, text = "Suministro, transporte e instalación de geomalla uniaxial coextruida con una resistencia última a la tensión de 144 KN/m y resistencia en las uniones o juntas de 135  KN/m, incluye traslapos y todo lo necesario para su correcta construcción", onvalue = 1, offvalue = 0, background = 'white', justify = 'left', variable = f9c16)
c16f9.place(x = 50, y = 530)

c17f9 = Checkbutton(frm9, text = "Suministro, transporte y colocación de un manto permanente para el control de erosión con una resistencia a la tensión en cualquier dirección longitudinal superior a 8,8 KN/m, resistencia UV del 90% y resistencia al cortante de 385 Pa o superior. Incluye traslapos donde se consideren pertinentes y todo lo necesario para su correcta construcción", onvalue = 1, offvalue = 0, background = 'white', justify = 'left', variable = f9c17)
c17f9.place(x = 50, y = 560)

c18f9 = Checkbutton(frm92, text = "Suministro, transporte y colocación de grama, para conformación de zonas verdes. Incluye conformación, nivelación de la superficie y regado.", onvalue = 1, offvalue = 0, background = 'white', justify = 'left', variable = f9c18)
c18f9.place(x = 50, y = 80)

c19f9 = Checkbutton(frm92, text = "Suministro, transporte e instalación de geomalla uniaxial coextruida con una resistencia última a la tensión de 114 KN/m y resistencia en las uniones o juntas de 105  KN/m, incluye traslapos y todo lo necesario para su correcta construcción", onvalue = 1, offvalue = 0, background = 'white', justify = 'left', variable = f9c19)
c19f9.place(x = 50, y = 110)

c20f9 = Checkbutton(frm92, text = "Suministro, transporte e instalación de geomalla uniaxial coextruida con una resistencia última a la tensión de 175 KN/m y resistencia en las uniones o juntas de 160 KN/m, incluye traslapos y todo lo necesario para su correcta construcción", onvalue = 1, offvalue = 0, background = 'white', justify = 'left', variable = f9c20)
c20f9.place(x = 50, y = 140)

c21f9 = Checkbutton(frm92, text = "Suministro, transporte e instalación de Geotextil no tejido NT 1800 para retener finos, incluye traslapos", onvalue = 1, offvalue = 0, background = 'white', justify = 'left', variable = f9c21)
c21f9.place(x = 50, y = 170)

c22f9 = Checkbutton(frm92, text = "Suministro, transporte e instalación de Geotextil no tejido NT 2000 para retener finos, incluye traslapos", onvalue = 1, offvalue = 0, background = 'white', justify = 'left', variable = f9c22)
c22f9.place(x = 50, y = 200)

c23f9 = Checkbutton(frm92, text = "Suministro, transporte e instalación de Geotextil no tejido NT 2500 para retener finos, incluye traslapos", onvalue = 1, offvalue = 0, background = 'white', justify = 'left', variable = f9c23)
c23f9.place(x = 50, y = 230)

c24f9 = Checkbutton(frm92, text = "Suministro, transporte e instalación de Geotextil tejido con una resistencia a la tensión de 2400 N, resistencia al punzamiento de 1060 N, resistencia al rasgado de 690 N, permeabilidad de 0,064 cm/s y un tasa de flujo de 1500 l/min/m2. Incluye traslapos y todo lo necesario para su correcta construcción", onvalue = 1, offvalue = 0, background = 'white', justify = 'left', variable = f9c24)
c24f9.place(x = 50, y = 260)

"//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////"

c1f10 = Checkbutton(frm10, text = "Arrendamiento o compra de predios", onvalue = 1, offvalue = 0, variable = f10c1, background = 'white', justify = 'left')
c1f10.place(x = 50, y = 80)
c2f10 = Checkbutton(frm10, text = "Elaboración de acta de vecindad", onvalue = 1, offvalue = 0, variable = f10c2, background = 'white', justify = 'left')
c2f10.place(x = 50, y = 110)
c3f10 = Checkbutton(frm10, text = "Elaboración de acta de entorno", onvalue = 1, offvalue = 0, variable = f10c3, background = 'white', justify = 'left')
c3f10.place(x = 50, y = 140)
c4f10 = Checkbutton(frm10, text = "Pago de servidumbres", onvalue = 1, offvalue = 0, variable = f10c4, background = 'white', justify = 'left')
c4f10.place(x = 50, y = 170)
c5f10 = Checkbutton(frm10, text = "Reasentamiento de familias", onvalue = 1, offvalue = 0, variable = f10c5, background = 'white', justify = 'left')
c5f10.place(x = 50, y = 200)
c6f10 = Checkbutton(frm10, text = "Reconstrucción de andén en concreto con acabado vitrificado antideslizante, arenón chino, espesor de 10cm, incluye piedra entresuelo e=0,15m, arenilla compactada e=0,50 m, juntas y acabados", onvalue = 1, offvalue = 0, variable = f10c6, background = 'white', justify = 'left')
c6f10.place(x = 50, y = 230)
c7f10 = Checkbutton(frm10, text = "Reconstrucción de andén en granito", onvalue = 1, offvalue = 0, variable = f10c7, background = 'white', justify = 'left')
c7f10.place(x = 50, y = 260)
c8f10 = Checkbutton(frm10, text = "Reparación de daños en acometidas y/o redes secundarias de acueducto", onvalue = 1, offvalue = 0, variable = f10c8, background = 'white', justify = 'left')
c8f10.place(x = 50, y = 290)
c9f10 = Checkbutton(frm10, text = "Suministro, transporte y colocación de almancenamiento provisional, por duración de las obras en el tanque de almacenamiento, incluye obra hidráulica, obras ", onvalue = 1, offvalue = 0, variable = f10c9, background = 'white', justify = 'left')
c9f10.place(x = 50, y = 320)
c10f10 = Checkbutton(frm10, text = "Atención médica", onvalue = 1, offvalue = 0, variable = f10c10, background = 'white', justify = 'left')
c10f10.place(x = 50, y = 350)

"//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////"

#checkbuttons frm11
c1f11 = Checkbutton(frm11, text="Buzón de sugerencias en acrílico de 0,30 m * 0,30 m * 0,30 m (según manual de comunicaciones)",onvalue = 1, offvalue = 0,variable = f11c1 ,background = 'white',justify = 'left')
c1f11.place(x = 50, y = 80)
c2f11 = Checkbutton(frm11, text="Cartelera informativa de 1,20 m * 0,80 m en madera con fondo de corcho (según manual de comunicaciones)",onvalue = 1, offvalue = 0,variable = f11c2 ,background = 'white',justify = 'left')
c2f11.place(x = 50, y = 110)
c3f11 = Checkbutton(frm11, text="Centro de atención móvil",onvalue = 1, offvalue = 0,variable = f11c3 ,background = 'white',justify = 'left')
c3f11.place(x = 50, y = 140)
c4f11 = Checkbutton(frm11, text="Cuña radial informativa",onvalue = 1, offvalue = 0,variable = f11c4 ,background = 'white',justify = 'left')
c4f11.place(x = 50, y = 170)
c5f11 = Checkbutton(frm11, text="Elaboración de testimonios",onvalue = 1, offvalue = 0,variable = f11c5 ,background = 'white',justify = 'left')
c5f11.place(x = 50, y = 200)
c6f11 = Checkbutton(frm11, text="Gestión informativa en redes sociales (diseñador wed + impresos)",onvalue = 1, offvalue = 0,variable = f11c6 ,background = 'white',justify = 'left')
c6f11.place(x = 50, y = 230)
c7f11 = Checkbutton(frm11, text="Logística reuniones con la comunidad (alquiler video beam, refrigerios para 50 personas)",onvalue = 1, offvalue = 0,variable = f11c7 ,background = 'white',justify = 'left')
c7f11.place(x = 50, y = 260)
c8f11 = Checkbutton(frm11, text="Logística reuniones con la comunidad (alquiler video beam, refrigerios para 100 personas)",onvalue = 1, offvalue = 0,variable = f11c8 ,background = 'white',justify = 'left')
c8f11.place(x = 50, y = 290)
c9f11 = Checkbutton(frm11, text="Pasacalles 7 m * 0,7 m en lona (según manual de comunicaciones)",onvalue = 1, offvalue = 0,variable = f11c9 ,background = 'white',justify = 'left')
c9f11.place(x = 50, y = 320)
c10f11 = Checkbutton(frm11, text="Pendón de 3.00 mt x 2.00 mts, 4x0 con hojaletes, diseños a definir",onvalue = 1, offvalue = 0,variable = f11c10,background = 'white',justify = 'left')
c10f11.place(x = 50, y = 350)
c11f11 = Checkbutton(frm11, text="Plotter adhesivo 70x23 cm, 4x0, full color Ref. Cartelera",onvalue = 1, offvalue = 0,variable = f11c11,background = 'white',justify = 'left')
c11f11.place(x = 50, y = 380)
c12f11 = Checkbutton(frm11, text="Plotter adhesivo 70x23 cm, 4x0, full color Ref. Buzón",onvalue = 1, offvalue = 0,variable = f11c12,background = 'white',justify = 'left')
c12f11.place(x = 50, y = 410)
c13f11 = Checkbutton(frm11, text="Stiker logo Antioquia la mas educada 7 x 7",onvalue = 1, offvalue = 0,variable = f11c13,background = 'white',justify = 'left')
c13f11.place(x = 50, y = 440)
c14f11 = Checkbutton(frm11, text="Valla (6mx4m). Incluye estructura metálica para fijación y soporte",onvalue = 1, offvalue = 0,variable = f11c14,background = 'white',justify = 'left')
c14f11.place(x = 50, y = 470)
c15f11 = Checkbutton(frm11, text="Volantes según oficina de comunicaciones de la Gobernación (2.000 unidades x Municipio)",onvalue = 1, offvalue = 0,variable = f11c15,background = 'white',justify = 'left')
c15f11.place(x = 50, y = 500)
c16f11 = Checkbutton(frm11, text="Volantes según oficina de comunicaciones de la Gobernación (2.000 unidades x Municipio)",onvalue = 1, offvalue = 0,variable = f11c16,background = 'white',justify = 'left')
c16f11.place(x = 50, y = 530)
c17f11 = Checkbutton(frm11, text="Distribución de cartillas o manuales",onvalue = 1, offvalue = 0,variable = f11c17,background = 'white',justify = 'left')
c17f11.place(x = 50, y = 560)
c18f11 = Checkbutton(frm11, text="Prospección arqueológica",onvalue = 1, offvalue = 0,variable = f11c18,background = 'white',justify = 'left')
c18f11.place(x = 50, y = 590)

"//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////"

#checkbuttons frm12

c1f12 = Checkbutton(frm12, text = "Construcción de acopios en madera para cemento, acero, pétreos, productos químicos, residuos sólidos",onvalue = 1, offvalue = 0, variable = f12c1 , background = 'white', justify = 'left')
c1f12.place(x = 50,y = 80)
c2f12 = Checkbutton(frm12, text = 'Construcción de polvorín en concreto de 21 MPa de resistencia, de 1,40m x 1,40m por 2,60m de alto con losa de contrapiso de 20cm, muros y losa de cubierta de espesor 10 cm, con puerta metálica de 2,10m x 0,8m con chapilla de madera en su interior, sistema de ventilación compuesto por dos codos de PVC 4" para ventilación en la losa de cubierta, Incluye acero de refuerzo y todos los demás elementos necesarios para su correcta construcción, según diseño.',onvalue = 1, offvalue = 0, variable = f12c2 , background = 'white', justify = 'left')
c2f12.place(x = 50,y = 110)
c3f12 = Checkbutton(frm12, text = "Instalación de cerramiento provisional en tela verde con una altura de 2,1 m. Incluye suministro, transporte e instalación de la tela, estructura en taco de madera común, concreto de 14 MPa, según diseño de mezclas aprobado por la interventoría para fijación de estructura en madera común, excavación manual en cualquier material, cargue, transporte y botada de material y todos los demás elementos necesarios para su correcta instalación.",onvalue = 1, offvalue = 0, variable = f12c3 , background = 'white', justify = 'left')
c3f12.place(x = 50,y = 140)
c4f12 = Checkbutton(frm12, text = "Instalación de cerramiento en teja ondulada de zinc calibre 35e:0,20mm, con altura de 2,20 metros. Incluye suministro, transporte e instalación de la teja, estructura en madera cada metros, larguero horizontal en la parte superior, concreto de 17,5 Mpa para fijación de estructura en madera común, vientos en madera cada 3m, excavación manual en cualquier materiales, cargue, transporte y botada de material.",onvalue = 1, offvalue = 0, variable = f12c4 , background = 'white', justify = 'left')
c4f12.place(x = 50,y = 170)
c5f12 = Checkbutton(frm12, text = "Malla polisombra, para proteger de la contaminación por polvo (ancho de 3,0m referencia 70%)",onvalue = 1, offvalue = 0, variable = f12c5 , background = 'white', justify = 'left')
c5f12.place(x = 50,y = 200)
c6f12 = Checkbutton(frm12, text = "Malla polisombra, para proteger de la contaminación por polvo (ancho de 2,1m de ancho)",onvalue = 1, offvalue = 0, variable = f12c6 , background = 'white', justify = 'left')
c6f12.place(x = 50,y = 230)
c7f12 = Checkbutton(frm12, text = "Suministro, transporte e instalación de tanque de almacenamiento de combustible para planta eléctrica en poliéster reforzado con fibra de vidrio, volumen de 1m3 (incluye base de tanque PRFV)",onvalue = 1, offvalue = 0, variable = f12c7 , background = 'white', justify = 'left')
c7f12.place(x = 50,y = 260)
c8f12 = Checkbutton(frm12, text = 'Suministro, transporte e instalación de cubierta tipo invernadero, provisional en plástico agrícola. Incluye estructura madera inmunizada, plástico TRATADO UV para invernadero o equivalente con un calibre de 7, colocado a una altura entre 4 y 6 m, cables de súper GX de 3/16" y 1/4", guarda cabos, tensores, grilletes, cinta, alambre No 13, excavación manual postes en madera inmunizada y vientos en cualquier material y los respectivos muertos para cada viento. Incluye el posterior desmonte de los elementos y botada del material, así́ como todos los demás elementos necesarios para su correcta instalación. La instalación se debe realizar con personal certificado con su respectiva dotación y equipos para trabajo en alturas. Esta actividad se realizará con previa autorización de la interventoría en caso de requerirse.',onvalue = 1, offvalue = 0, variable = f12c8 , background = 'white', justify = 'left')
c8f12.place(x = 50,y = 290)
c9f12 = Checkbutton(frm12, text = 'Otros - adecuación de maquinaria, equipos y planta industrial',onvalue = 1, offvalue = 0, variable = f12c9 , background = 'white', justify = 'left')
c9f12.place(x = 50,y = 320)
c10f12 = Checkbutton(frm12, text = "Adquisición de kit de atención de derrames",onvalue = 1, offvalue = 0, variable = f12c10, background = 'white', justify = 'left')
c10f12.place(x = 50,y = 350)

"//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////"

next13 = Button(frm13, text = "Siguiente Página", command = m132)
next13.place(x = 1200, y = 50)

back132 = Button(frm132, text = "Anterior Página", command = m13)
back132.place(x = 1200, y = 50)

c1f13 = Checkbutton(frm13,text = "Baliza o delineador tubular con tres bandas reflectabas blancas, grado diamante (1,27 m) Tubo señalizador con cinta de alta densidad ",onvalue = 1, offvalue = 0, variable = f13c1 ,background = "white", justify = "left")
c1f13.place(x = 100, y =80 )

c2f13 = Checkbutton(frm13,text = "Barricadas (1,50 m alto x 2,40 m ancho, con refractivo grado diamante). (Alquiler)",onvalue = 1, offvalue = 0, variable = f13c2 ,background = "white", justify = "left")
c2f13.place(x = 100, y =110 )

c3f13 = Checkbutton(frm13,text = "Cinta de cerramiento 12 cm de alto, Según especificaciones del Manual de diseño e imagen y previa aprobación de la supervisión.",onvalue = 1, offvalue = 0, variable = f13c3 ,background = "white", justify = "left")
c3f13.place(x = 100, y =140 ) 

c4f13 = Checkbutton(frm13,text = "Cinta Señalización, ancho 0.12 m (según manual de comunicaciones)",onvalue = 1, offvalue = 0, variable = f13c4 ,background = "white", justify = "left")
c4f13.place(x = 100, y =170 )

c5f13 = Checkbutton(frm13,text = "Cinta Señalización Naranja (calibre 4, 12 cm de alto, color naranja - blanco o amarillo- negro), incluye leyenda y logo según diseño de la entidad.",onvalue = 1, offvalue = 0, variable = f13c5 ,background = "white", justify = "left")
c5f13.place(x = 100, y =200 )

c6f13 = Checkbutton(frm13,text = "Cinta de señalización naranja (Calibre 4, rollo por 80 metros debe incluir logo de acuerdo al diseño institucional)",onvalue = 1, offvalue = 0, variable = f13c6 ,background = "white", justify = "left")
c6f13.place(x = 100, y =220)

c7f13 = Checkbutton(frm13,text = "Conos (0,90 m de altura, material plástico color naranja) y dos fajas reflectabas",onvalue = 1, offvalue = 0, variable = f13c7 ,background = "white", justify = "left")
c7f13.place(x = 100, y =250)

c8f13 = Checkbutton(frm13,text = "Estacón en madera común para instalación de malla verde",onvalue = 1, offvalue = 0, variable = f13c8 ,background = "white", justify = "left")
c8f13.place(x = 100, y =280)

c9f13 = Checkbutton(frm13,text = "Franjas Barricadas 1,50 x 2,40 m",onvalue = 1, offvalue = 0, variable = f13c9 ,background = "white", justify = "left")
c9f13.place(x = 100, y =310)

c10f13 = Checkbutton(frm13,text = "Lámpara flasher, iluminación intermitente o fija, LED  de alto brillo",onvalue = 1, offvalue = 0, variable = f13c10,background = "white", justify = "left")
c10f13.place(x = 100, y =340)

c11f13 = Checkbutton(frm13,text = "Lámpara redonda tipo sirena (licuadora)",onvalue = 1, offvalue = 0, variable = f13c11,background = "white", justify = "left")
c11f13.place(x = 100, y =370)

c12f13 = Checkbutton(frm13,text = "Linterna alargada que emita haz luminosos de color rojo",onvalue = 1, offvalue = 0, variable = f13c12,background = "white", justify = "left")
c12f13.place(x = 100, y =400)

c13f13 = Checkbutton(frm13,text = "Lona corporativa para vehículo (volqueta o camión) de 1,50 x 0,80 metros impresión injekt resistente a la intemperie",onvalue = 1, offvalue = 0, variable = f13c13,background = "white", justify = "left")
c13f13.place(x = 100, y =430)

c14f13 = Checkbutton(frm13,text = "Maletín o barrera de contención vial de 2mt x 1mt",onvalue = 1, offvalue = 0, variable = f13c14,background = "white", justify = "left")
c14f13.place(x = 100, y =460)

c15f13 = Checkbutton(frm13,text = "Malla tipo cerramiento color verde (2,100 m ancho), para protección",onvalue = 1, offvalue = 0, variable = f13c15,background = "white", justify = "left")
c15f13.place(x = 100, y =490)

c16f13 = Checkbutton(frm13,text = "Paleta de pare y siga (papel grado diamante 45 cm de diámetro y paral de 1,50 m de largo)",onvalue = 1, offvalue = 0, variable = f13c16,background = "white", justify = "left")
c16f13.place(x = 100, y =520)

c17f13 = Checkbutton(frm13,text = "Paleta de pare y siga con paral tipo 3",onvalue = 1, offvalue = 0, variable = f13c17,background = "white", justify = "left")
c17f13.place(x = 100, y =550)

c18f13 = Checkbutton(frm13,text = "Pendones para volqueta de 0,7m * 1m con información de la obra",onvalue = 1, offvalue = 0, variable = f13c18,background = "white", justify = "left")
c18f13.place(x = 100, y =580)

c19f13 = Checkbutton(frm132,text = "Señales informativas (aproximación a obra, inicio, fin, carril cerrado, sendero peatonal. Tablero rectangular fondo naranja, símbolos y orla negros, lamina galvanizada, calibre 20, altura de 3,50 m). (Alquiler)",onvalue = 1, offvalue = 0, variable = f13c19,background = "white", justify = "left")
c19f13.place(x = 100, y =80 )

c20f13 = Checkbutton(frm132,text = "Señales informativas (75x90) para 5 usos",onvalue = 1, offvalue = 0, variable = f13c20,background = "white", justify = "left")
c20f13.place(x = 100, y =110 )

c21f13 = Checkbutton(frm132,text = "Señales informativas y preventivas de obra y exteriores",onvalue = 1, offvalue = 0, variable = f13c21,background = "white", justify = "left")
c21f13.place(x = 100, y =140 )

c22f13 = Checkbutton(frm132,text = "Señales preventivas (entrada y salida de volquetas, Trabajos en la vía, maquinaria en vía. En forma de rombo, fondo naranja, color negro para símbolos, tamaño 75 x 90). (Alquiler)",onvalue = 1, offvalue = 0, variable = f13c22,background = "white", justify = "left")
c22f13.place(x = 100, y =170 )

c23f13 = Checkbutton(frm132,text = "Señales preventivas  (75x90) para 5 usos",onvalue = 1, offvalue = 0, variable = f13c23,background = "white", justify = "left")
c23f13.place(x = 100, y =200 )

c24f13 = Checkbutton(frm132,text = "Señales preventivas (señales de protección, señales de obra, entre otras). En forma de rombo, fondo naranja, color negro para símbolos, tamaño 75 x 90). (Alquiler)",onvalue = 1, offvalue = 0, variable = f13c24,background = "white", justify = "left")
c24f13.place(x = 100, y =230)

c25f13 = Checkbutton(frm132,text = "Señales reglamentarias según manual de señalización vial de 90x90 y de un paral (desvío, vía cerrada, entre otros).",onvalue = 1, offvalue = 0, variable = f13c25,background = "white", justify = "left")
c25f13.place(x = 100, y =260 )

c26f13 = Checkbutton(frm132,text = "Señales verticales ( Informativas, Preventivas, Reglamentarias)",onvalue = 1, offvalue = 0, variable = f13c26,background = "white", justify = "left")
c26f13.place(x = 100, y =290 )

c27f13 = Checkbutton(frm132,text = "Señalización acopios",onvalue = 1, offvalue = 0, variable = f13c27,background = "white", justify = "left")
c27f13.place(x = 100, y =320)

c28f13 = Checkbutton(frm132,text = "Señalización de residuos sólidos",onvalue = 1, offvalue = 0, variable = f13c28,background = "white", justify = "left")
c28f13.place(x = 100, y =350)

c29f13 = Checkbutton(frm132,text = "Señalización seguridad industrial",onvalue = 1, offvalue = 0, variable = f13c29,background = "white", justify = "left")
c29f13.place(x = 100, y =380)

c30f13 = Checkbutton(frm132,text = "Servicio de pare y siga en derrumbes y/o vía con un solo carril en servicio por eventos diferentes al retiro y cargue de derrumbes",onvalue = 1, offvalue = 0, variable = f13c30,background = "white", justify = "left")
c30f13.place(x = 100, y =410)

c31f13 = Checkbutton(frm132,text = "Servicio de pare y siga en derrumbes y/o vía con un solo carril en servicio por eventos diferentes al retiro y cargue de derrumbes",onvalue = 1, offvalue = 0, variable = f13c31,background = "white", justify = "left")
c31f13.place(x = 100, y =440)

c32f13 = Checkbutton(frm132,text = "Teleras (9 x 135)",onvalue = 1, offvalue = 0, variable = f13c32,background = "white", justify = "left")
c32f13.place(x = 100, y =470)

c33f13 = Checkbutton(frm132,text = "Tijera de obra dimensiones 1m * 1,2 m, según modelo de la entidad*",onvalue = 1, offvalue = 0, variable = f13c33,background = "white", justify = "left")
c33f13.place(x = 100, y =500)

"//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////"

#14

next142 = Button(frm14, text="Siguiente Página", command=m142)
next142.place(x=1200, y = 50)
back14 = Button(frm142, text="Anterior Página", command=m14)
back14.place(x=1200, y= 50)

c1f14 = Checkbutton(frm14, text = "Abrigos plásticos (pantalón y chaqueta).", offvalue = 0, onvalue = 1, variable = f14c1, background = "white", justify = "left")
c1f14.place(x= 100, y=80 )

c2f14 = Checkbutton(frm14, text = "Adhesivo con logo para cascos (según manual de comunicaciones)", offvalue = 0, onvalue = 1, variable = f14c2, background = "white", justify = "left")
c2f14.place(x= 100, y=110 )

c3f14 = Checkbutton(frm14, text = "Arnés pélvico con eslinga doble y absorvedor de energía", offvalue = 0, onvalue = 1, variable = f14c3, background = "white", justify = "left")
c3f14.place(x= 100, y=140 )

c4f14 = Checkbutton(frm14, text = "Aviso troquelado, 70x70 full color, en poliestireno 4x0 REF:2 (Esta obra es tuya)", offvalue = 0, onvalue = 1, variable = f14c4, background = "white", justify = "left")
c4f14.place(x= 100, y=170 )

c5f14 = Checkbutton(frm14, text = "Botas caucho con puntera", offvalue = 0, onvalue = 1, variable = f14c5, background = "white", justify = "left")
c5f14.place(x= 100, y=200 )

c6f14 = Checkbutton(frm14, text = "Botiquín básico de primeros auxilios red. 115 en lona (cruz roja)", offvalue = 0, onvalue = 1, variable = f14c6, background = "white", justify = "left")
c6f14.place(x= 100, y=230 )

c7f14 = Checkbutton(frm14, text = "Camilla rígida en madera con inmovilizador 180 metros x 0,45 mts", offvalue = 0, onvalue = 1, variable = f14c7, background = "white", justify = "left")
c7f14.place(x= 100, y=260 )

c8f14 = Checkbutton(frm14, text = "Camisa dril manga larga con dos logos estampados (según manual de comunicaciones)", offvalue = 0, onvalue = 1, variable = f14c8, background = "white", justify = "left")
c8f14.place(x= 100, y=290 )

c9f14 = Checkbutton(frm14, text = "Camiseta negra con logo de la Gobernación de Antioquia Adelante Pequeño y atrás grande", offvalue = 0, onvalue = 1, variable = f14c9, background = "white", justify = "left")
c9f14.place(x= 100, y=320 )

c10f14 = Checkbutton(frm14, text = "Chalecos reflectivos sencillos con logo de la entidad", offvalue = 0, onvalue = 1, variable = f14c10, background = "white", justify = "left")
c10f14.place(x= 100, y =350 )

c11f14 = Checkbutton(frm14, text = "Chalecos reflectivos para bandereros", offvalue = 0, onvalue = 1, variable = f14c11, background = "white", justify = "left")
c11f14.place(x= 100, y =380)

c12f14 = Checkbutton(frm14, text = "Chalecos para ingenieros y tecnólogos, con tres logos bordados (según manual de comunicaciones)", offvalue = 0, onvalue = 1, variable = f14c12, background = "white", justify = "left")
c12f14.place(x= 100, y =410 )

c13f14 = Checkbutton(frm14, text = "Carné Trabajadores", offvalue = 0, onvalue = 1, variable = f14c13, background = "white", justify = "left")
c13f14.place(x= 100, y =440)

c14f14 = Checkbutton(frm14, text = "Carnet de identificación personal con logo de la empresa constructora, carnet plásticos, full color, calibre de 30 micras, tamaño estándar de 86*54 mm+ brazalete portacarnet de seguridad", offvalue = 0, onvalue = 1, variable = f14c14, background = "white", justify = "left")
c14f14.place(x= 100, y =470 )

c15f14 = Checkbutton(frm14, text = "Capas plásticas", offvalue = 0, onvalue = 1, variable = f14c15, background = "white", justify = "left")
c15f14.place(x= 100, y =500 )

c16f14 = Checkbutton(frm14, text = "Casco de seguridad blanco tipo ingeniero", offvalue = 0, onvalue = 1, variable = f14c16, background = "white", justify = "left")
c16f14.place(x= 100, y =530 )

c17f14 = Checkbutton(frm14, text = "Casco dieléctrico amarillo con barbuquejo", offvalue = 0, onvalue = 1, variable = f14c17, background = "white", justify = "left")
c17f14.place(x= 100, y =560 )

c18f14 = Checkbutton(frm14, text = "Casco naranja con franja reflectiva para bandereros", offvalue = 0, onvalue = 1, variable = f14c18, background = "white", justify = "left")
c18f14.place(x= 100, y =590 )

c19f14 = Checkbutton(frm142, text = "Extintor ABC 10 LB (mas dos recargas)", offvalue = 0, onvalue = 1, variable = f14c19, background = "white", justify = "left")
c19f14.place(x= 100, y =80 )

c20f14 = Checkbutton(frm142, text = "Extintor de 20 LB de polvo químico ABC multipropósito (2 recargas, soporte y señalización)", offvalue = 0, onvalue = 1, variable = f14c20, background = "white", justify = "left")
c20f14.place(x= 100, y =110 )

c21f14 = Checkbutton(frm142, text = "Gafas protectoras", offvalue = 0, onvalue = 1, variable = f14c21, background = "white", justify = "left")
c21f14.place(x= 100, y =140 )

c22f14 = Checkbutton(frm142, text = "Guantes de caucho", offvalue = 0, onvalue = 1, variable = f14c22, background = "white", justify = "left")
c22f14.place(x= 100, y =170 )

c23f14 = Checkbutton(frm142, text = "Guantes de carnaza", offvalue = 0, onvalue = 1, variable = f14c23, background = "white", justify = "left")
c23f14.place(x= 100, y =200 )

c24f14 = Checkbutton(frm142, text = "Guantes plásticos", offvalue = 0, onvalue = 1, variable = f14c24, background = "white", justify = "left")
c24f14.place(x= 100, y =230 )

c25f14 = Checkbutton(frm142, text = "Inmovilizador de cuello", offvalue = 0, onvalue = 1, variable = f14c25, background = "white", justify = "left")
c25f14.place(x= 100, y =260)

c26f14 = Checkbutton(frm142, text = "Línea de vida", offvalue = 0, onvalue = 1, variable = f14c26, background = "white", justify = "left")
c26f14.place(x= 100, y =290)

c27f14 = Checkbutton(frm142, text = "Manguera para agua lineal", offvalue = 0, onvalue = 1, variable = f14c27, background = "white", justify = "left")
c27f14.place(x= 100, y =320 )

c28f14 = Checkbutton(frm142, text = "Manguera para agua rollo", offvalue = 0, onvalue = 1, variable = f14c28, background = "white", justify = "left")
c28f14.place(x= 100, y =350 )

c29f14 = Checkbutton(frm142, text = "Overol", offvalue = 0, onvalue = 1, variable = f14c29, background = "white", justify = "left")
c29f14.place(x= 100, y =380 )

c30f14 = Checkbutton(frm142, text = "Pantalón dril con un logo estampado (según manual de comunicaciones)", offvalue = 0, onvalue = 1, variable = f14c30, background = "white", justify = "left")
c30f14.place(x= 100, y =410 )

c31f14 = Checkbutton(frm142, text = "Protectores auditivos", offvalue = 0, onvalue = 1, variable = f14c31, background = "white", justify = "left")
c31f14.place(x= 100, y =440)

c32f14 = Checkbutton(frm142, text = "Radios de comunicación", offvalue = 0, onvalue = 1, variable = f14c32, background = "white", justify = "left")
c32f14.place(x= 100, y =470 )

c33f14 = Checkbutton(frm142, text = "Señales de campamento - avisos en poliestireno de 30x50 cm (uso de EPP, extintor, camilla, botiquín, salida de evacuación, sustancias peligrosos, etc).", offvalue = 0, onvalue = 1, variable = f14c33, background = "white", justify = "left")
c33f14.place(x= 100, y =500 )

c34f14 = Checkbutton(frm142, text = "Señalización campamento", offvalue = 0, onvalue = 1, variable = f14c34, background = "white", justify = "left")
c34f14.place(x= 100, y =530 )

c35f14 = Checkbutton(frm142, text = "Tapabocas para polvo en poliéster", offvalue = 0, onvalue = 1, variable = f14c35, background = "white", justify = "left")
c35f14.place(x= 100, y =560 )


c36f14 = Checkbutton(frm142, text = "Uniformes (pantalón y camisa personal de operación) de acuerdo al manual de obra pública", offvalue = 0, onvalue = 1, variable = f14c36, background = "white", justify = "left")
c36f14.place(x= 100, y =590 )

#15

c1f15 = Checkbutton(frm15, text = "Visitas y permisos ambientales por la entidad competente", offvalue = 0, onvalue = 1, variable = f15c1, background = "white", justify = "left")
c1f15.place(x= 100,y= 80)

c2f15 = Checkbutton(frm15, text = "Estudio de línea base", offvalue = 0, onvalue = 1, variable = f15c2, background = "white", justify = "left")
c2f15.place(x= 100,y= 80+(30*1))

c3f15 = Checkbutton(frm15, text = "Inventarios de fauna", offvalue = 0, onvalue = 1, variable = f15c3, background = "white", justify = "left")
c3f15.place(x= 100,y= 80+(30*2))

c4f15 = Checkbutton(frm15, text = "Inventarios de flora", offvalue = 0, onvalue = 1, variable = f15c4, background = "white", justify = "left")
c4f15.place(x= 100,y= 80+(30*3))

c5f15 = Checkbutton(frm15, text = "Estudios hidrológicos e hidráulicos", offvalue = 0, onvalue = 1, variable = f15c5, background = "white", justify = "left")
c5f15.place(x= 100,y= 80+(30*4))

c6f15 = Checkbutton(frm15, text = "Modelaciones", offvalue = 0, onvalue = 1, variable = f15c6, background = "white", justify = "left")
c6f15.place(x= 100,y= 80+(30*5))

c7f15 = Checkbutton(frm15, text = "Estudios hidrogeológicos", offvalue = 0, onvalue = 1, variable = f15c7, background = "white", justify = "left")
c7f15.place(x= 100,y= 80+(30*6))

c8f15 = Checkbutton(frm15, text = "Muestreos isocinéticos", offvalue = 0, onvalue = 1, variable = f15c8, background = "white", justify = "left")
c8f15.place(x= 100,y= 80+(30*7))

c9f15 = Checkbutton(frm15, text = "Mediciones de ruido ambiental", offvalue = 0, onvalue = 1, variable = f15c9, background = "white", justify = "left")
c9f15.place(x= 100,y= 80+(30*8))

c10f15 = Checkbutton(frm15, text = "Caracterizaciones de aguas", offvalue = 0, onvalue = 1, variable = f15c10, background = "white", justify = "left")
c10f15.place(x= 100, y=80+(30*9) )

c11f15 = Checkbutton(frm15, text = "DAA, EIA: estudios arqueológicos (programa de arqueología preventiva).", offvalue = 0, onvalue = 1, variable = f15c11, background = "white", justify = "left")
c11f15.place(x= 100, y=80+(30*10))


#LISTA DE CHECKBUTTONS

botoneslt = [c1f1 ,c2f1 , c3f1, c4f1, c5f1, c6f1, c7f1, c8f1, c9f1, c10f1, c11f1, c12f1, c13f1, c14f1, c15f1, c16f1,
			c1f2, c2f2, c3f2, 
			c1f3, c2f3, c3f3, c4f3, c5f3, c6f3, c7f3, c8f3, c9f3, c10f3, c11f3, c12f3, 
			c1f4, c2f4, c3f4, c4f4, c5f4, c6f4, c7f4, c8f4, c9f4, c10f4, c11f4, c12f4, c13f4, c14f4, 
			c1f5, c2f5, c3f5, c4f5, c5f5, c6f5, c7f5, c8f5, 
			c1f6, c2f6, c3f6, 
			c1f7,c2f7,c3f7,c4f7, 
			c1f8, c2f8, c3f8, c4f8, c5f8, c6f8, c7f8, c8f8, c9f8, c10f8, c11f8, c12f8,c13f8, c14f8, c15f8, c16f8, c17f8, c18f8, c19f8, c20f8, c21f8, c22f8, c23f8, c24f8, c25f8, c26f8, c27f8, c28f8, c29f8, c30f8, c31f8, c32f8, c33f8, c34f8, c35f8, c36f8, 
			c37f8, c38f8, c39f8, c40f8, c41f8, c42f8, c43f8,
			c1f9, c2f9, c3f9, c4f9, c5f9, c6f9, c7f9, c8f9, c9f9, c10f9, c11f9, c12f9, c13f9, c14f9, c15f9, c16f9, c17f9, c18f9, c19f9, c20f9, c21f9, c22f9, c23f9,	c24f9,
			c1f10, c2f10, c3f10, c4f10, c5f10, c6f10, c7f10, c8f10, c9f10, c10f10, 
			c1f11, c2f11, c3f11, c4f11, c5f11, c6f11, c7f11, c8f11, c9f11, c10f11, c11f11, c12f11, c13f11, c14f11, c15f11, c16f11, c17f11, c18f11,
			c1f12, c2f12, c3f12, c4f12, c5f12, c6f12, c7f12, c8f12, c9f12, c10f12,
			c1f13, c2f13, c3f13, c4f13, c5f13, c6f13, c7f13, c8f13, c9f13, c10f13, c11f13, c12f13, c13f13, c14f13, c15f13, c16f13, c17f13, c18f13, c19f13, c20f13, c21f13, c22f13, c23f13, c24f13, c25f13,
			c26f13, c27f13, c28f13, c29f13, c30f13, c31f13, c32f13, c33f13, 
			c1f14, c2f14, c3f14, c4f14, c5f14, c6f14, c7f14, c8f14, c9f14, c10f14, c11f14, c12f14, c13f14, c14f14, c15f14, c16f14, c17f14, c18f14, c19f14, c20f14, c21f14, c22f14, c23f14, c24f14, c25f14, c26f14, c27f14, c28f14, c29f14, c30f14, c31f14, c32f14, c33f14, c34f14, c35f14, c36f14,
			c1f15, c2f15, c3f15, c4f15, c5f15, c6f15, c7f15, c8f15, c9f15, c10f15, c11f15]


pusuario = open('pusuario.txt','r') #---------------------------------------------- ESTA ES LA QUE TIENE SÓLO UN NÚMERO
lpusuario = eval(pusuario.readline()) #---------------------------------------------- ESTA ES LA QUE TIENE SÓLO UN NÚMERO

lt1 = []
pusuario.seek(0, 0)
x = int(pusuario.readline())
for i in range(245):
	lt1.append(RImp.matrizimpactos[i][x])
for i in range(245):
	if(lt1[i]==1):
		botoneslt[i].config(background = "light blue")


actusuario = open('actusuario.txt', 'r')
lactusuario = eval(actusuario.readline())

lt2 = []
for i in range(len(lactusuario)):
	if lactusuario[i]==1:
		for j in range(len(RImp.matrizimpactos)):
			lt2.append(RImp.matrizimpactos[j][i])
		for k in range(245):
			if lt2[k] == 1:
				botoneslt[k].config(background="light blue")
	lt2 = []

impusuario = open('impusuario.txt', 'r')
limpusuario = eval(impusuario.readline())

lt3= []
for i in range(len(limpusuario)):
	if limpusuario[i]==1:
		for j in range(len(RImp.matrizimpactos)):
			lt3.append(RImp.matrizimpactos[j][i])
		for k in range(245):
			if lt3[k] == 1:
				botoneslt[k].config(background="light blue")
	lt3 = []





frm1.grid()

app.mainloop()