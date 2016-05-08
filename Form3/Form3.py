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

#VARIABLES PARA LOS RADIOBUTTONS

#PLANEACIÓN

p1 = IntVar()
p2 = IntVar()
p3 = IntVar()


#CONSTRUCCIÓN

c1 = 1
c2 = 2
c3 = 3
c4 = 4
c5 = 5
c6 = 6
c7 = 7
c8 = 8
c9 = 9
c10 = 10
c11 = 11

#OPERACIÓN

o1 = 1
o2 = 2
o3 = 3
o4 = 4
o5 = 5
o6 = 6
o7 = 7
o8 = 8
o9 = 9

#ABANDONO

a1 = 1
a2 = 2
a3 = 3
a4 = 4

#OPERACIÓN Y ABANDONO

oa1 = 1
oa2 = 2

#TODOS

t1 = 1
t2 = 2
t3 = 3
t4 = 4
t5 = 5
t6 = 6
t7 = 7

"//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////"

#CREAMOS RADIOBUTTONS PARA DISPLAY DE FRAMES

rdbtnplncn = Radiobutton(master, text = "Planeación", width = 10, background = 'white', command = planeacion, value = 0)
rdbtnplncn.place(x = 100, y = 60)
rdbtnplncn.deselect()

rdbtncnstrccn = Radiobutton(master, text = "Construcción", width = 10, background = 'white', command = construccion, value = 1)
rdbtncnstrccn.place(x = 200, y = 60)
rdbtncnstrccn.deselect()

rdbtnoprcn = Radiobutton(master, text = "Operación", width = 10, background = 'white', command = operacion, value = 2)
rdbtnoprcn.place(x = 300, y = 60)
rdbtnoprcn.deselect()

rdbtnabndn = Radiobutton(master, text = "Abandono", width = 10, background = 'white', command = abandono, value = 3)
rdbtnabndn.place(x = 400, y = 60)
rdbtnabndn.deselect()

rdbtnoprcnyabdn = Radiobutton(master, text = "Operación y Abandono", width = 20, background = 'white', command = operacionabandono, value = 4)
rdbtnoprcnyabdn.place(x = 500, y = 60)
rdbtnoprcnyabdn.deselect()

rdbtntodos = Radiobutton(master, text = "Todos", width = 10, background = 'white', command = todos, value = 5)
rdbtntodos.place(x = 655, y = 60)
rdbtntodos.deselect()

"//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////"

#ELEMENTOS DEL FRAME DE PLANEACIÓN

rdbtn1plncn = Radiobutton(frmplncn, text = "Gestión de trámites legales", background = 'white', variable = p1, value = "Gestion")
rdbtn1plncn.place(x = 100, y = 120)

rdbtn2plncn = Radiobutton(frmplncn, text = "Realización de línea base y estudios técnicos", background = 'white', variable = p2, value = "LByET")
rdbtn2plncn.place(x = 100, y = 140)

rdbtn3plncn = Radiobutton(frmplncn, text = "Realización de diseños", background = 'white', variable = p3, value = "Diseños")
rdbtn3plncn.place(x = 100, y = 160)

"//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////"

#ELEMENTOS DEL FRAME DE CONSTRUCCIÓN

rdbtn1cnstrccn = Radiobutton(frmcnstrccn, text = "Localización y replanteo", background = 'white', variable = c1)
rdbtn1cnstrccn.place(x = 100, y = 120)

rdbtn2cnstrccn = Radiobutton(frmcnstrccn, text = "Adecuación de accesos o vías", background = 'white', variable = c2)
rdbtn2cnstrccn.place(x = 100, y = 140)

rdbtn3cnstrccn = Radiobutton(frmcnstrccn, text = "Instalación de obras provisionales y/o definitivas", background = 'white', variable = c3)
rdbtn3cnstrccn.place(x = 100, y = 160)

rdbtn4cnstrccn = Radiobutton(frmcnstrccn, text = "Explotación de préstamos", background = 'white', variable = c4)
rdbtn4cnstrccn.place(x = 100, y = 180)

rdbtn5cnstrccn = Radiobutton(frmcnstrccn, text = "Ejecución de tratamientos silviculturales y manejo de coberturas", background = 'white', variable = c5)
rdbtn5cnstrccn.place(x = 100, y = 200)

rdbtn6cnstrccn = Radiobutton(frmcnstrccn, text = "Construcción de obras de protección y drenaje", background = 'white', variable = c6)
rdbtn6cnstrccn.place(x = 100, y = 220)

rdbtn7cnstrccn = Radiobutton(frmcnstrccn, text = "Realización de trabajos preliminares", background = 'white', variable = c7)
rdbtn7cnstrccn.place(x = 100, y = 240)

rdbtn8cnstrccn = Radiobutton(frmcnstrccn, text = "Ejecución de cimentaciones, fundaciones, relleno y compactación", background = 'white', variable = c8)
rdbtn8cnstrccn.place(x = 100, y = 260)

rdbtn9cnstrccn = Radiobutton(frmcnstrccn, text = "Levantamiento o instalación de estructuras.", background = 'white', variable = c9)
rdbtn9cnstrccn.place(x = 100, y = 280)

rdbtn10cnstrccn = Radiobutton(frmcnstrccn, text = "Levantamiento o instalación de muros", background = 'white', variable = c10)
rdbtn10cnstrccn.place(x = 100, y = 300)

rdbtn11cnstrccn = Radiobutton(frmcnstrccn, text = "Realización de acabados y obras exteriores", background = 'white', variable = c11)
rdbtn11cnstrccn.place(x = 100, y = 320)

"//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////"

#ELEMENTOS DEL FRAME DE OPERACIÓN

rdbtn1oprcn = Radiobutton(frmoprcn, text = "Realización de pruebas", background = 'white', variable = o1)
rdbtn1oprcn.place(x = 100, y = 120)

rdbtn2oprcn = Radiobutton(frmoprcn, text = "Operación obra de infraestructura", background = 'white', variable = o2)
rdbtn2oprcn.place(x = 100, y = 140)

rdbtn3oprcn = Radiobutton(frmoprcn, text = "Reposición de elementos o tramos", background = 'white', variable = o3)
rdbtn3oprcn.place(x = 100, y = 160)

rdbtn4oprcn = Radiobutton(frmoprcn, text = "Reparación de elementos o tramos", background = 'white', variable = o4)
rdbtn4oprcn.place(x = 100, y = 180)

rdbtn5oprcn = Radiobutton(frmoprcn, text = "Limpieza de las instalaciones y elementos", background = 'white', variable = o5)
rdbtn5oprcn.place(x = 100, y = 200)

rdbtn6oprcn = Radiobutton(frmoprcn, text = "Mejoramiento o ampliaciones", background = 'white', variable = o6)
rdbtn6oprcn.place(x = 100, y = 220)

rdbtn7oprcn = Radiobutton(frmoprcn, text = "Limpieza final de la obra e instalaciones temporales", background = 'white', variable = o7)
rdbtn7oprcn.place(x = 100, y = 240)

rdbtn8oprcn = Radiobutton(frmoprcn, text = "Control de emisiones y vertimientos", background = 'white', variable = o8)
rdbtn8oprcn.place(x = 100, y = 260)

rdbtn9oprcn = Radiobutton(frmoprcn, text = "Cobertura o reconformación final del sitio", background = 'white', variable = o9)
rdbtn9oprcn.place(x = 100, y = 280)


"//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////"

#ELEMENTOS FRAME ABANDONO

rdbtn1abndn = Radiobutton(frmabndn, text = "Desmantelamiento/demolición", background = 'white', variable = a1)
rdbtn1abndn.place(x = 100, y = 120)

rdbtn2abndn = Radiobutton(frmabndn, text = "Reactivación de un servicio o sistema natural", background = 'white', variable = a2)
rdbtn2abndn.place(x = 100, y = 140)

rdbtn3abndn = Radiobutton(frmabndn, text = "Obras de urbanismo", background = 'white', variable = a3)
rdbtn3abndn.place(x = 100, y = 160)

rdbtn4abndn = Radiobutton(frmabndn, text = "Uso final del sitio", background = 'white', variable = a4)
rdbtn4abndn.place(x = 100, y = 180)


"//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////"

#ELEMENTOS FRAME ABANDONO Y OPERACIÓN

rdbtn1abdndyoprcn = Radiobutton(frmoprncyabdn, text = "Arborización y/o revegetalización", background = 'white', variable = oa1)
rdbtn1abdndyoprcn.place(x = 100, y = 120)

rdbtn2abndnyoprcn = Radiobutton(frmoprncyabdn, text = "Dragados", background = 'white', variable = oa2)
rdbtn2abndnyoprcn.place(x = 100, y = 140)


"//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////"

#ELEMENTOS FRAME TODOS

rdbtn1todos = Radiobutton(frmtodos, text = "Movilización de equipos, maquinaria y materiales.", background = 'white', variable = t1)
rdbtn1todos.place(x = 100, y= 120)

rdbtn2todos = Radiobutton(frmtodos, text = "Gestión de residuos sólidos y peligrosos generados.", background = 'white', variable = t2)
rdbtn2todos.place(x = 100, y= 140)

rdbtn3todos = Radiobutton(frmtodos, text = "Gestión de residuos líquidos y aguas lluvias generadas.", background = 'white', variable = t3)
rdbtn3todos.place(x = 100, y= 160)

rdbtn4todos = Radiobutton(frmtodos, text = "Atención de PQR`s en obra, y veedurías", background = 'white', variable = t4)
rdbtn4todos.place(x = 100, y= 180)

rdbtn5todos = Radiobutton(frmtodos, text = "Atención de contingencias", background = 'white', variable = t5)
rdbtn5todos.place(x = 100, y= 200)

rdbtn6todos = Radiobutton(frmtodos, text = "Labores administrativas (organización laboral)", background = 'white', variable = t6)
rdbtn6todos.place(x = 100, y= 220)

rdbtn7todos = Radiobutton(frmtodos, text = "Monitoreo y control (Plan de Seguimiento y Monitoreo)", background = 'white', variable = t7)
rdbtn7todos.place(x = 100, y= 240)


"//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////"


#DEFIIMOS NUESTRAS FUNCIONES


master.mainloop()


	
