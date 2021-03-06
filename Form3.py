#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
from tkinter import *
import sys

master = Tk()
master.geometry("1200x600+0+0")
master.config(bg= "white")
master.title("Aplicativo de Simulacion Costos, Por Santiago Vélez Aristizabal")

"//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////"

#CREAMOS UN FRAME PARA CADA FASE, INCLUYENDO LAS FASES MEZCLADAS

frmplncn= Frame(bg = "white", width = 1200, height = 600)

frmcnstrccn = Frame(bg = "white", width = 1200, height = 600)

frmoprcn = Frame(bg = 'white', width = 1200, height = 600)

frmabndn = Frame(bg = 'white', width = 1200, height = 600)

frmoprncyabdn = Frame(bg = 'white', width = 1200, height = 600)

frmtodos = Frame(bg = 'white', width = 1200, height = 600)


"//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////"

#FUNCIONES PARA LOS RADIOBUTTONS FIJOS
def mostrar():
	print(p1.get())


def planeacion():

	frmcnstrccn.grid_remove()
	frmoprcn.grid_remove()
	frmabndn.grid_remove()
	frmoprncyabdn.grid_remove()
	frmtodos.grid_remove()
	frmplncn.grid()

def construccion():

	frmoprcn.grid_remove()
	frmabndn.grid_remove()
	frmoprncyabdn.grid_remove()
	frmtodos.grid_remove()
	frmplncn.grid_remove()
	frmcnstrccn.grid()

def operacion():

	frmcnstrccn.grid_remove()
	frmplncn.grid_remove()	
	frmabndn.grid_remove()
	frmoprncyabdn.grid_remove()
	frmtodos.grid_remove()
	frmplncn.grid_remove()
	frmoprcn.grid()

def abandono():

	frmcnstrccn.grid_remove()
	frmplncn.grid_remove()
	frmoprcn.grid_remove()
	frmoprncyabdn.grid_remove()
	frmtodos.grid_remove()
	frmplncn.grid_remove()
	frmabndn.grid()

def operacionabandono():

	frmcnstrccn.grid_remove()
	frmplncn.grid_remove()
	frmoprcn.grid_remove()
	frmabndn.grid_remove()
	frmtodos.grid_remove()
	frmplncn.grid_remove()
	frmoprncyabdn.grid()

def todos():

	frmcnstrccn.grid_remove()
	frmplncn.grid_remove()
	frmoprcn.grid_remove()
	frmabndn.grid_remove()
	frmoprncyabdn.grid_remove()
	frmplncn.grid_remove()
	frmtodos.grid()

"//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////"

#variableS PARA LOS RADIOBUTTONS

#PLANEACIÓN

p1 = IntVar()
p2 = IntVar()
p3 = IntVar()


#CONSTRUCCIÓN

c1 = IntVar()
c2 = IntVar()
c3 = IntVar()
c4 = IntVar()
c5 = IntVar()
c6 = IntVar()
c7 = IntVar()
c8 = IntVar()
c9 = IntVar()
c10 = IntVar()
c11 = IntVar()

#OPERACIÓN

o1 = IntVar()
o2 = IntVar()
o3 = IntVar()
o4 = IntVar()
o5 = IntVar()
o6 = IntVar()
o7 = IntVar()
o8 = IntVar()
o9 = IntVar()
#ABANDONO

a1 = IntVar()
a2 = IntVar()
a3 = IntVar()
a4 = IntVar()

#OPERACIÓN Y ABANDONO

oa1 = IntVar()
oa2 = IntVar()

#TODOS

t1 = IntVar()
t2 = IntVar()
t3 = IntVar()
t4 = IntVar()
t5 = IntVar()
t6 = IntVar()
t7 = IntVar()

"//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////"

#CREAMOS RADIOBUTTONS PARA DISPLAY DE FRAMES

rdbtnplncn = Radiobutton(master, text = "Planeación", width = 10, background = 'white',  command = planeacion, value = 0)
rdbtnplncn.place(x = 100, y = 60)
rdbtnplncn.deselect()

rdbtncnstrccn = Radiobutton(master, text = "Construcción", width = 10, background = 'white', command = construccion, value = 1)
rdbtncnstrccn.place(x = 200, y = 60)
rdbtncnstrccn.deselect()

rdbtnoprcn = Radiobutton(master, text = "Operación", width = 10, background = 'white',command = operacion, value = 2)
rdbtnoprcn.place(x = 300, y = 60)
rdbtnoprcn.deselect()

rdbtnabndn = Radiobutton(master, text = "Abandono", width = 10, background = 'white', command = abandono, value = 3)
rdbtnabndn.place(x = 400, y = 60)
rdbtnabndn.deselect()

rdbtnoprcnyabdn = Radiobutton(master, text = "Operación y Abandono", width = 20, background = 'white',command = operacionabandono, value = 4)
rdbtnoprcnyabdn.place(x = 500, y = 60)
rdbtnoprcnyabdn.deselect()

rdbtntodos = Radiobutton(master, text = "Todos", width = 10, background = 'white', command = todos, value = 5)
rdbtntodos.place(x = 655, y = 60)
rdbtntodos.deselect()

"//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////"

#ELEMENTOS DEL FRAME DE PLANEACIÓN

chbtn1plncn = Checkbutton(frmplncn, text = "Gestión de trámites legales", background = 'white', onvalue = 1, offvalue =0,variable = p1)
chbtn1plncn.place(x = 100, y = 120)

chbtn2plncn = Checkbutton(frmplncn, text = "Realización de línea base y estudios técnicos", background = 'white', onvalue = 1, offvalue =0,variable = p2)
chbtn2plncn.place(x = 100, y = 140)

chbtn3plncn = Checkbutton(frmplncn, text = "Realización de diseños", background = 'white', onvalue = 1, offvalue =0,variable = p3)
chbtn3plncn.place(x = 100, y = 160)

"//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////"

#ELEMENTOS DEL FRAME DE CONSTRUCCIÓN

chbtn1cnstrccn = Checkbutton(frmcnstrccn, text = "Localización y replanteo", background = 'white', onvalue = 1, offvalue =0,variable = c1)
chbtn1cnstrccn.place(x = 100, y = 120)

chbtn2cnstrccn = Checkbutton(frmcnstrccn, text = "Adecuación de accesos o vías", background = 'white', onvalue = 1, offvalue =0,variable = c2)
chbtn2cnstrccn.place(x = 100, y = 140)

chbtn3cnstrccn = Checkbutton(frmcnstrccn, text = "Instalación de obras provisionales y/o definitivas", background = 'white', onvalue = 1, offvalue =0,variable = c3)
chbtn3cnstrccn.place(x = 100, y = 160)

chbtn4cnstrccn = Checkbutton(frmcnstrccn, text = "Explotación de préstamos", background = 'white', onvalue = 1, offvalue =0,variable = c4)
chbtn4cnstrccn.place(x = 100, y = 180)

chbtn5cnstrccn = Checkbutton(frmcnstrccn, text = "Ejecución de tratamientos silviculturales y manejo de coberturas", background = 'white', onvalue = 1, offvalue =0,variable = c5)
chbtn5cnstrccn.place(x = 100, y = 200)

chbtn6cnstrccn = Checkbutton(frmcnstrccn, text = "Construcción de obras de protección y drenaje", background = 'white', onvalue = 1, offvalue =0, variable = c6)
chbtn6cnstrccn.place(x = 100, y = 220)

chbtn7cnstrccn = Checkbutton(frmcnstrccn, text = "Realización de trabajos preliminares", background = 'white', onvalue = 1, offvalue =0,variable = c7)
chbtn7cnstrccn.place(x = 100, y = 240)

chbtn8cnstrccn = Checkbutton(frmcnstrccn, text = "Ejecución de cimentaciones, fundaciones, relleno y compactación", background = 'white', onvalue = 1, offvalue =0,variable = c8)
chbtn8cnstrccn.place(x = 100, y = 260)

chbtn9cnstrccn = Checkbutton(frmcnstrccn, text = "Levantamiento o instalación de estructuras.", background = 'white', onvalue = 1, offvalue =0,variable = c9)
chbtn9cnstrccn.place(x = 100, y = 280)

chbtn10cnstrccn = Checkbutton(frmcnstrccn, text = "Levantamiento o instalación de muros", background = 'white', onvalue = 1, offvalue =0,variable = c10)
chbtn10cnstrccn.place(x = 100, y = 300)

chbtn11cnstrccn = Checkbutton(frmcnstrccn, text = "Realización de acabados y obras exteriores", background = 'white', onvalue = 1, offvalue =0,variable = c11)
chbtn11cnstrccn.place(x = 100, y = 320)

"//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////"

#ELEMENTOS DEL FRAME DE OPERACIÓN

chbtn1oprcn = Checkbutton(frmoprcn, text = "Realización de pruebas", background = 'white', onvalue = 1, offvalue =0,variable = o1)
chbtn1oprcn.place(x = 100, y = 120)

chbtn2oprcn = Checkbutton(frmoprcn, text = "Operación obra de infraestructura", background = 'white', onvalue = 1, offvalue =0,variable = o2)
chbtn2oprcn.place(x = 100, y = 140)

chbtn3oprcn = Checkbutton(frmoprcn, text = "Reposición de elementos o tramos", background = 'white', onvalue = 1, offvalue =0,variable = o3)
chbtn3oprcn.place(x = 100, y = 160)

chbtn4oprcn = Checkbutton(frmoprcn, text = "Reparación de elementos o tramos", background = 'white', onvalue = 1, offvalue =0,variable = o4)
chbtn4oprcn.place(x = 100, y = 180)

chbtn5oprcn = Checkbutton(frmoprcn, text = "Limpieza de las instalaciones y elementos", background = 'white', onvalue = 1, offvalue =0,variable = o5)
chbtn5oprcn.place(x = 100, y = 200)

chbtn6oprcn = Checkbutton(frmoprcn, text = "Mejoramiento o ampliaciones", background = 'white', onvalue = 1, offvalue =0,variable = o6)
chbtn6oprcn.place(x = 100, y = 220)

chbtn7oprcn = Checkbutton(frmoprcn, text = "Limpieza final de la obra e instalaciones temporales", background = 'white', onvalue = 1, offvalue =0,variable = o7)
chbtn7oprcn.place(x = 100, y = 240)

chbtn8oprcn = Checkbutton(frmoprcn, text = "Control de emisiones y vertimientos", background = 'white', onvalue = 1, offvalue =0,variable = o8)
chbtn8oprcn.place(x = 100, y = 260)

chbtn9oprcn = Checkbutton(frmoprcn, text = "Cobertura o reconformación final del sitio", background = 'white', onvalue = 1, offvalue =0,variable = o9)
chbtn9oprcn.place(x = 100, y = 280)


"//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////"

#ELEMENTOS FRAME ABANDONO

chbtn1abndn = Checkbutton(frmabndn, text = "Desmantelamiento/demolición", background = 'white', onvalue = 1, offvalue =0,variable = a1)
chbtn1abndn.place(x = 100, y = 120)

chbtn2abndn = Checkbutton(frmabndn, text = "Reactivación de un servicio o sistema natural", background = 'white', onvalue = 1, offvalue =0,variable = a2)
chbtn2abndn.place(x = 100, y = 140)

chbtn3abndn = Checkbutton(frmabndn, text = "Obras de urbanismo", background = 'white', onvalue = 1, offvalue =0,variable = a3)
chbtn3abndn.place(x = 100, y = 160)

chbtn4abndn = Checkbutton(frmabndn, text = "Uso final del sitio", background = 'white', onvalue = 1, offvalue =0,variable = a4)
chbtn4abndn.place(x = 100, y = 180)


"//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////"

#ELEMENTOS FRAME ABANDONO Y OPERACIÓN

chbtn1abdndyoprcn = Checkbutton(frmoprncyabdn, text = "Arborización y/o revegetalización", background = 'white', onvalue = 1, offvalue =0,variable = oa1)
chbtn1abdndyoprcn.place(x = 100, y = 120)

chbtn2abndnyoprcn = Checkbutton(frmoprncyabdn, text = "Dragados", background = 'white', onvalue = 1, offvalue =0,variable = oa2)
chbtn2abndnyoprcn.place(x = 100, y = 140)


"//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////"

#ELEMENTOS FRAME TODOS

chbtn1todos = Checkbutton(frmtodos, text = "Movilización de equipos, maquinaria y materiales.", background = 'white', onvalue = 1, offvalue =0,variable = t1)
chbtn1todos.place(x = 100, y= 120)

chbtn2todos = Checkbutton(frmtodos, text = "Gestión de residuos sólidos y peligrosos generados.", background = 'white', onvalue = 1, offvalue =0,variable = t2)
chbtn2todos.place(x = 100, y= 140)

chbtn3todos = Checkbutton(frmtodos, text = "Gestión de residuos líquidos y aguas lluvias generadas.", background = 'white', onvalue = 1, offvalue =0,variable = t3)
chbtn3todos.place(x = 100, y= 160)

chbtn4todos = Checkbutton(frmtodos, text = "Atención de PQR`s en obra, y veedurías", background = 'white', onvalue = 1, offvalue =0,variable = t4)
chbtn4todos.place(x = 100, y= 180)

chbtn5todos = Checkbutton(frmtodos, text = "Atención de contingencias", background = 'white', onvalue = 1, offvalue =0,variable = t5)
chbtn5todos.place(x = 100, y= 200)

chbtn6todos = Checkbutton(frmtodos, text = "Labores administrativas (organización laboral)", background = 'white', onvalue = 1, offvalue =0,variable = t6)
chbtn6todos.place(x = 100, y= 220)

chbtn7todos = Checkbutton(frmtodos, text = "Monitoreo y control (Plan de Seguimiento y Monitoreo)", background = 'white', onvalue = 1, offvalue =0,variable = t7)
chbtn7todos.place(x = 100, y= 240)


"//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////"
test = Button(master,text = "Prueba",height= 5,width= 5, command = mostrar)
test.place(x=900,y=400)
#DEFIIMOS NUESTRAS FUNCIONES


master.mainloop()


	
