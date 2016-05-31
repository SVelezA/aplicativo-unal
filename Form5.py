import numpy as np
import os
from tkinter import *
import sys

app = Tk()
app.geometry("1400x650+00+0")
app.config(background="white")
app.title("Form5")

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
frm9= Frame(bg="white",width=1400,height=650)
frm10 = Frame(bg="white",width=1400,height=650)
frm11= Frame(bg="white",width=1400,height=650)
frm12 = Frame(bg="white",width=1400,height=650)
frm13 = Frame(bg="white",width=1400,height=650)
frm14= Frame(bg="white",width=1400,height=650)


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

def m8():
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




"//////////////////////////////////////////////////////////////////////////////////////////////////////"
#Variables de los checkbuttons

#Frm1
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

#Frm2
f2c1 = IntVar()
f2c2 = IntVar()
f2c3 = IntVar()

#Frm3
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

#frm4
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

#frm5
f5c1 = IntVar()
f5c2 = IntVar()
f5c3 = IntVar()
f5c4 = IntVar()
f5c5 = IntVar()
f5c6 = IntVar()
f5c7 = IntVar()
f5c8 = IntVar()

#frm6
f6c1 = IntVar()
f6c2 = IntVar()
f6c3 = IntVar()

#frm7
f7c1 = IntVar()
f7c2 = IntVar()
f7c3 = IntVar()
f7c4 = IntVar()

#frm8
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
f8c44 = IntVar()
f8c45 = IntVar()

#frm9
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

#frm10
f10c1 = IntVar()
f10c2 = IntVar()
f10c3 = IntVar()
f10c4 = IntVar()
f10c5 = IntVar()
f10c6 = IntVar()
f10c7 = IntVar()
f10c8 = IntVar()
f10c9 = IntVar()

#frm11
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

#frm12
f12c1 = IntVar()
f12c2 = IntVar()
f12c3 = IntVar()
f12c4 = IntVar()
f12c5 = IntVar()
f12c6 = IntVar()
f12c7 = IntVar()
f12c8 = IntVar()

#frm13
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
f13c34 = IntVar()

#frm14

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
f14c37= IntVar()
f14c38= IntVar()
f14c39= IntVar()
f14c40= IntVar()
f14c41= IntVar()
f14c42= IntVar()
f14c43= IntVar()
f14c44= IntVar()
f14c45= IntVar()


"//////////////////////////////////////////////////////////////////////////////////////////////////////"

#RADIOBUTTONS PARA DISPLAY DE FRAMES

menubar = Menubutton(app, text = "Opciones", relief = RAISED)
menubar.place(x = 0, y = 0)

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

c15f1 = Checkbutton(frm1, text = "Suministro, transporte y construcción de Gaviones, incluye transporte material.", onvalue = 1, offvalue = 0, variable = f1c16, background = 'white', justify = 'left')
c15f1.place(x = 50, y = 590)

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

c12f3 = Checkbutton(frm3, text = "Otros - manejo de fuentes emisoras y receptoras de ruido y olores ofensivos", onvalue = 1, offvalue = 0, variable = f3c10, background = 'white', justify = 'left')
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

c1f6 = Checkbutton(frm6, text = "Retiro de limunarias fluorescentes. Incluye cargue, transporte, botada en botaderos autorizados por el municipio y recuperación de los materiales "
	+"aprovechables y su transporte hasta el sitio que lo indique la interventoría.", onvalue = 1, offvalue = 0, variable = f6c2, background = 'white', justify = 'left')
c1f6.place(x = 50, y = 110)

c1f6 = Checkbutton(frm6, text = "Pago por transporte, tratamiento y disposición final a empresa gestora de RESPEL", onvalue = 1, offvalue = 0, variable = f6c3, background = 'white', justify = 'left')
c1f6.place(x = 50, y = 140)

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

c1f8 = Checkbutton(frm8, text = "Plantación de arbustos ornamentales de 1 m de altura, cobertura en coleo, incluye excavación, tierra abonada.", onvalue = 1, offvalue = 0, variable = f8c1, background = 'white', justify = 'left')
c1f8.place(x = 54, y = 80)

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

c17f8 = Checkbutton(frm82, text = "", onvalue = 1, offvalue = 0, variable = f7c4, background = 'white', justify = 'left')
c17f8.place(x = 50, y = 80)

c18f8 = Checkbutton(frm82, text = "", onvalue = 1, offvalue = 0, variable = f7c4, background = 'white', justify = 'left')
c18f8.place(x = 50, y = 80)

c19f8 = Checkbutton(frm82, text = "", onvalue = 1, offvalue = 0, variable = f7c4, background = 'white', justify = 'left')
c19f8.place(x = 50, y = 80)

c20f8 = Checkbutton(frm82, text = "", onvalue = 1, offvalue = 0, variable = f7c4, background = 'white', justify = 'left')
c20f8.place(x = 50, y = 80)

c21f8 = Checkbutton(frm82, text = "", onvalue = 1, offvalue = 0, variable = f7c4, background = 'white', justify = 'left')
c21f8.place(x = 50, y = 80)

c22f8 = Checkbutton(frm82, text = "", onvalue = 1, offvalue = 0, variable = f7c4, background = 'white', justify = 'left')
c22f8.place(x = 50, y = 80)

c23f8 = Checkbutton(frm82, text = "", onvalue = 1, offvalue = 0, variable = f7c4, background = 'white', justify = 'left')
c23f8.place(x = 50, y = 80)

c24f8 = Checkbutton(frm82, text = "", onvalue = 1, offvalue = 0, variable = f7c4, background = 'white', justify = 'left')
c24f8.place(x = 50, y = 80)

c25f8 = Checkbutton(frm82, text = "", onvalue = 1, offvalue = 0, variable = f7c4, background = 'white', justify = 'left')
c25f8.place(x = 50, y = 80)

c26f8 = Checkbutton(frm82, text = "", onvalue = 1, offvalue = 0, variable = f7c4, background = 'white', justify = 'left')
c26f8.place(x = 50, y = 80)

c27f8 = Checkbutton(frm82, text = "", onvalue = 1, offvalue = 0, variable = f7c4, background = 'white', justify = 'left')
c27f8.place(x = 50, y = 80)

c28f8 = Checkbutton(frm82, text = "", onvalue = 1, offvalue = 0, variable = f7c4, background = 'white', justify = 'left')
c28f8.place(x = 50, y = 80)

c29f8 = Checkbutton(frm82, text = "", onvalue = 1, offvalue = 0, variable = f7c4, background = 'white', justify = 'left')
c29f8.place(x = 50, y = 80)

c30f8 = Checkbutton(frm82, text = "", onvalue = 1, offvalue = 0, variable = f7c4, background = 'white', justify = 'left')
c30f8.place(x = 50, y = 80)

c31f8 = Checkbutton(frm82, text = "", onvalue = 1, offvalue = 0, variable = f7c4, background = 'white', justify = 'left')
c31f8.place(x = 50, y = 80)

c32f8 = Checkbutton(frm82, text = "", onvalue = 1, offvalue = 0, variable = f7c4, background = 'white', justify = 'left')
c32f8.place(x = 50, y = 80)

c33f8 = Checkbutton(frm82, text = "", onvalue = 1, offvalue = 0, variable = f7c4, background = 'white', justify = 'left')
c33f8.place(x = 50, y = 80)

c34f8 = Checkbutton(frm82, text = "", onvalue = 1, offvalue = 0, variable = f7c4, background = 'white', justify = 'left')
c34f8.place(x = 50, y = 80)

c35f8 = Checkbutton(frm82, text = "", onvalue = 1, offvalue = 0, variable = f7c4, background = 'white', justify = 'left')
c35f8.place(x = 50, y = 80)

c36f8 = Checkbutton(frm82, text = "", onvalue = 1, offvalue = 0, variable = f7c4, background = 'white', justify = 'left')
c36f8.place(x = 50, y = 80)

c37f8 = Checkbutton(frm82, text = "", onvalue = 1, offvalue = 0, variable = f7c4, background = 'white', justify = 'left')
c37f8.place(x = 50, y = 80)

c38f8 = Checkbutton(frm82, text = "", onvalue = 1, offvalue = 0, variable = f7c4, background = 'white', justify = 'left')
c38f8.place(x = 50, y = 80)

c39f8 = Checkbutton(frm82, text = "", onvalue = 1, offvalue = 0, variable = f7c4, background = 'white', justify = 'left')
c39f8.place(x = 50, y = 80)

c40f8 = Checkbutton(frm82, text = "", onvalue = 1, offvalue = 0, variable = f7c4, background = 'white', justify = 'left')
c40f8.place(x = 50, y = 80)

c41f8 = Checkbutton(frm82, text = "", onvalue = 1, offvalue = 0, variable = f7c4, background = 'white', justify = 'left')
c41f8.place(x = 50, y = 80)

c42f8 = Checkbutton(frm82, text = "", onvalue = 1, offvalue = 0, variable = f7c4, background = 'white', justify = 'left')
c42f8.place(x = 50, y = 80)

c43f8 = Checkbutton(frm82, text = "", onvalue = 1, offvalue = 0, variable = f7c4, background = 'white', justify = 'left')
c43f8.place(x = 50, y = 80)

c44f8 = Checkbutton(frm82, text = "", onvalue = 1, offvalue = 0, variable = f7c4, background = 'white', justify = 'left')
c44f8.place(x = 50, y = 80)

c45f8 = Checkbutton(frm82, text = "", onvalue = 1, offvalue = 0, variable = f7c4, background = 'white', justify = 'left')
c45f8.place(x = 50, y = 80)
"//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////"

frm8.grid()

app.mainloop()