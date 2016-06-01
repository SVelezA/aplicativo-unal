#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
from tkinter import *
import sys
import RActProy
import numpy as np

master = Tk()
master.geometry("1000x500+0+0")
master.config(bg= "white")
master.title("Aplicativo de Simulacion Costos, Por Santiago Vélez Aristizabal")

save1 = open('actusuario.txt', 'w+')

"//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////"

#CREAMOS UN FRAME PARA CADA FASE, INCLUYENDO LAS FASES MEZCLADAS

frmplncn= Frame(bg = "white", width = 1000, height = 500)

frmcnstrccn = Frame(bg = "white", width = 1000, height = 500)

frmoprcn = Frame(bg = 'white', width = 1000, height = 500)

frmabndn = Frame(bg = 'white', width = 1000, height = 500)

frmoprncyabdn = Frame(bg = 'white', width = 1000, height = 500)

frmtodos = Frame(bg = 'white', width = 1000, height = 500)

frmplncn.grid()

"//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////"

txt1 = Label(master, text=  "Por favor, seleccione las actividades de ingeniería que se llevarán a cabo en el proyecto, de acuerdo con la fase del ciclo de vida, así: P (Planeación), C (Construcción),\n O (Operación) y A (Abandono). Luego de la selección, haga click en el botón 'Seleccionar Impactos'", background = 'white')
txt1.place(x = 80, y = 25)

txt1 = Label(frmplncn, text=  "Por favor, seleccione las actividades de ingeniería que se llevarán a cabo en el proyecto, de acuerdo con la fase del ciclo de vida, así: P (Planeación), C (Construcción),\n O (Operación) y A (Abandono). Luego de la selección, haga click en el botón 'Seleccionar Impactos'", background = 'white')
txt1.place(x = 80, y = 25)

txt1 = Label(frmcnstrccn, text=  "Por favor, seleccione las actividades de ingeniería que se llevarán a cabo en el proyecto, de acuerdo con la fase del ciclo de vida, así: P (Planeación), C (Construcción),\n O (Operación) y A (Abandono). Luego de la selección, haga click en el botón 'Seleccionar Impactos'", background = 'white')
txt1.place(x = 80, y = 25)

txt1 = Label(frmoprcn, text=  "Por favor, seleccione las actividades de ingeniería que se llevarán a cabo en el proyecto, de acuerdo con la fase del ciclo de vida, así: P (Planeación), C (Construcción),\n O (Operación) y A (Abandono). Luego de la selección, haga click en el botón 'Seleccionar Impactos'", background = 'white')
txt1.place(x = 80, y = 25)

txt1 = Label(frmabndn, text=  "Por favor, seleccione las actividades de ingeniería que se llevarán a cabo en el proyecto, de acuerdo con la fase del ciclo de vida, así: P (Planeación), C (Construcción),\n O (Operación) y A (Abandono). Luego de la selección, haga click en el botón 'Seleccionar Impactos'", background = 'white')
txt1.place(x = 80, y = 25)

txt1 = Label(frmoprncyabdn, text=  "Por favor, seleccione las actividades de ingeniería que se llevarán a cabo en el proyecto, de acuerdo con la fase del ciclo de vida, así: P (Planeación), C (Construcción),\n O (Operación) y A (Abandono). Luego de la selección, haga click en el botón 'Seleccionar Impactos'", background = 'white')
txt1.place(x = 80, y = 25)

txt1 = Label(frmtodos, text=  "Por favor, seleccione las actividades de ingeniería que se llevarán a cabo en el proyecto, de acuerdo con la fase del ciclo de vida, así: P (Planeación), C (Construcción),\n O (Operación) y A (Abandono). Luego de la selección, haga click en el botón 'Seleccionar Impactos'", background = 'white')
txt1.place(x = 80, y = 25)



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

def guardar():
	save1.seek(0.0)
	sel = []
	for i in range(36):
		check = listachecks[i].get()
		sel.append(check)
	print(sel)
	print(str(sel))
	save1.write(str(sel))
	save1.close()
	master.destroy()
	import ImpactoUsuario

def marcartodas():
	for i in range(36):
		botones[i].select()

def dmarcartodas():
	for i in range(36):
		botones[i].deselect()

"//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////"

#variableS PARA LOS RADIOBUTTONS

actividades = IntVar()

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

listachecks = [p1,p2,p3,c1,c2,c3,c4,c5,c6,c7,c8,c9,c10,c11,o1,o1,o3,o4,o5,o6,o7,o8,o9,a1,a2,a3,a4,oa1,oa2,t1,t2,t3,t4,t5,t6,t7]

"//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////"

#CREAMOS RADIOBUTTONS PARA DISPLAY DE FRAMES

rdbtnplncn = Radiobutton(master, text = "Planeación", width = 10, background = 'white',  command = planeacion, value = "Plncn", variable = actividades)
rdbtnplncn.place(x = 100, y = 80)
rdbtnplncn.select()

rdbtncnstrccn = Radiobutton(master, text = "Construcción", width = 10, background = 'white', command = construccion, value = "Cnstrccn", variable = actividades)
rdbtncnstrccn.place(x = 200, y = 80)
rdbtncnstrccn.deselect()

rdbtnoprcn = Radiobutton(master, text = "Operación", width = 10, background = 'white',command = operacion, value = "Oprcn", variable = actividades)
rdbtnoprcn.place(x = 300, y = 80)
rdbtnoprcn.deselect()

rdbtnabndn = Radiobutton(master, text = "Abandono", width = 10, background = 'white', command = abandono, value = "Abndn", variable = actividades)
rdbtnabndn.place(x = 400, y = 80)
rdbtnabndn.deselect()

rdbtnoprcnyabdn = Radiobutton(master, text = "Operación y Abandono", width = 20, background = 'white',command = operacionabandono, value = "opabdndn", variable = actividades)
rdbtnoprcnyabdn.place(x = 500, y = 80)
rdbtnoprcnyabdn.deselect()

rdbtntodos = Radiobutton(master, text = "Todos", width = 10, background = 'white', command = todos, value = "Todos", variable = actividades)
rdbtntodos.place(x = 655, y = 80)
rdbtntodos.deselect()

"//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////"

#ELEMENTOS DEL FRAME DE PLANEACIÓN

chbtn1plncn = Checkbutton(frmplncn, text = "Gestión de trámites legales", background = 'white', onvalue = 1, offvalue =0,variable = p1)
chbtn1plncn.place(x = 100, y = 120)

chbtn2plncn = Checkbutton(frmplncn, text = "Realización de línea base y estudios técnicos", background = 'white', onvalue = 1, offvalue =0,variable = p2)
chbtn2plncn.place(x = 100, y = 150)

chbtn3plncn = Checkbutton(frmplncn, text = "Realización de diseños", background = 'white', onvalue = 1, offvalue =0,variable = p3)
chbtn3plncn.place(x = 100, y = 180)

"//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////"

#ELEMENTOS DEL FRAME DE CONSTRUCCIÓN

chbtn1cnstrccn = Checkbutton(frmcnstrccn, text = "Localización y replanteo", background = 'white', onvalue = 1, offvalue =0,variable = c1)
chbtn1cnstrccn.place(x = 100, y = 120)

chbtn2cnstrccn = Checkbutton(frmcnstrccn, text = "Adecuación de accesos o vías", background = 'white', onvalue = 1, offvalue =0,variable = c2)
chbtn2cnstrccn.place(x = 100, y = 150)

chbtn3cnstrccn = Checkbutton(frmcnstrccn, text = "Instalación de obras provisionales y/o definitivas", background = 'white', onvalue = 1, offvalue =0,variable = c3)
chbtn3cnstrccn.place(x = 100, y = 180)

chbtn4cnstrccn = Checkbutton(frmcnstrccn, text = "Explotación de préstamos", background = 'white', onvalue = 1, offvalue =0,variable = c4)
chbtn4cnstrccn.place(x = 100, y = 210)

chbtn5cnstrccn = Checkbutton(frmcnstrccn, text = "Ejecución de tratamientos silviculturales y manejo de coberturas", background = 'white', onvalue = 1, offvalue =0,variable = c5)
chbtn5cnstrccn.place(x = 100, y = 240)

chbtn6cnstrccn = Checkbutton(frmcnstrccn, text = "Construcción de obras de protección y drenaje", background = 'white', onvalue = 1, offvalue =0, variable = c6)
chbtn6cnstrccn.place(x = 100, y = 270)

chbtn7cnstrccn = Checkbutton(frmcnstrccn, text = "Realización de trabajos preliminares", background = 'white', onvalue = 1, offvalue =0,variable = c7)
chbtn7cnstrccn.place(x = 100, y = 300)

chbtn8cnstrccn = Checkbutton(frmcnstrccn, text = "Ejecución de cimentaciones, fundaciones, relleno y compactación", background = 'white', onvalue = 1, offvalue =0,variable = c8)
chbtn8cnstrccn.place(x = 100, y = 330)

chbtn9cnstrccn = Checkbutton(frmcnstrccn, text = "Levantamiento o instalación de estructuras.", background = 'white', onvalue = 1, offvalue =0,variable = c9)
chbtn9cnstrccn.place(x = 100, y = 360)

chbtn10cnstrccn = Checkbutton(frmcnstrccn, text = "Levantamiento o instalación de muros", background = 'white', onvalue = 1, offvalue =0,variable = c10)
chbtn10cnstrccn.place(x = 100, y = 390)

chbtn11cnstrccn = Checkbutton(frmcnstrccn, text = "Realización de acabados y obras exteriores", background = 'white', onvalue = 1, offvalue =0,variable = c11)
chbtn11cnstrccn.place(x = 100, y = 420)

"//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////"

#ELEMENTOS DEL FRAME DE OPERACIÓN

chbtn1oprcn = Checkbutton(frmoprcn, text = "Realización de pruebas", background = 'white', onvalue = 1, offvalue =0,variable = o1)
chbtn1oprcn.place(x = 100, y = 120)

chbtn2oprcn = Checkbutton(frmoprcn, text = "Operación obra de infraestructura", background = 'white', onvalue = 1, offvalue =0,variable = o2)
chbtn2oprcn.place(x = 100, y = 150)

chbtn3oprcn = Checkbutton(frmoprcn, text = "Reposición de elementos o tramos", background = 'white', onvalue = 1, offvalue =0,variable = o3)
chbtn3oprcn.place(x = 100, y = 180)

chbtn4oprcn = Checkbutton(frmoprcn, text = "Reparación de elementos o tramos", background = 'white', onvalue = 1, offvalue =0,variable = o4)
chbtn4oprcn.place(x = 100, y = 210)

chbtn5oprcn = Checkbutton(frmoprcn, text = "Limpieza de las instalaciones y elementos", background = 'white', onvalue = 1, offvalue =0,variable = o5)
chbtn5oprcn.place(x = 100, y = 240)

chbtn6oprcn = Checkbutton(frmoprcn, text = "Mejoramiento o ampliaciones", background = 'white', onvalue = 1, offvalue =0,variable = o6)
chbtn6oprcn.place(x = 100, y = 270)

chbtn7oprcn = Checkbutton(frmoprcn, text = "Limpieza final de la obra e instalaciones temporales", background = 'white', onvalue = 1, offvalue =0,variable = o7)
chbtn7oprcn.place(x = 100, y = 300)

chbtn8oprcn = Checkbutton(frmoprcn, text = "Control de emisiones y vertimientos", background = 'white', onvalue = 1, offvalue =0,variable = o8)
chbtn8oprcn.place(x = 100, y = 330)

chbtn9oprcn = Checkbutton(frmoprcn, text = "Cobertura o reconformación final del sitio", background = 'white', onvalue = 1, offvalue =0,variable = o9)
chbtn9oprcn.place(x = 100, y = 360)


"//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////"

#ELEMENTOS FRAME ABANDONO

chbtn1abndn = Checkbutton(frmabndn, text = "Desmantelamiento/demolición", background = 'white', onvalue = 1, offvalue =0,variable = a1)
chbtn1abndn.place(x = 100, y = 120)

chbtn2abndn = Checkbutton(frmabndn, text = "Reactivación de un servicio o sistema natural", background = 'white', onvalue = 1, offvalue =0,variable = a2)
chbtn2abndn.place(x = 100, y = 150)

chbtn3abndn = Checkbutton(frmabndn, text = "Obras de urbanismo", background = 'white', onvalue = 1, offvalue =0,variable = a3)
chbtn3abndn.place(x = 100, y = 180)

chbtn4abndn = Checkbutton(frmabndn, text = "Uso final del sitio", background = 'white', onvalue = 1, offvalue =0,variable = a4)
chbtn4abndn.place(x = 100, y = 210)


"//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////"

#ELEMENTOS FRAME ABANDONO Y OPERACIÓN

chbtn1abdndyoprcn = Checkbutton(frmoprncyabdn, text = "Arborización y/o revegetalización", background = 'white', onvalue = 1, offvalue =0,variable = oa1)
chbtn1abdndyoprcn.place(x = 100, y = 120)

chbtn2abndnyoprcn = Checkbutton(frmoprncyabdn, text = "Dragados", background = 'white', onvalue = 1, offvalue =0,variable = oa2)
chbtn2abndnyoprcn.place(x = 100, y = 150)


"//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////"

#ELEMENTOS FRAME TODOS

chbtn1todos = Checkbutton(frmtodos, text = "Movilización de equipos, maquinaria y materiales.", background = 'white', onvalue = 1, offvalue =0,variable = t1)
chbtn1todos.place(x = 100, y= 120)

chbtn2todos = Checkbutton(frmtodos, text = "Gestión de residuos sólidos y peligrosos generados.", background = 'white', onvalue = 1, offvalue =0,variable = t2)
chbtn2todos.place(x = 100, y= 150)

chbtn3todos = Checkbutton(frmtodos, text = "Gestión de residuos líquidos y aguas lluvias generadas.", background = 'white', onvalue = 1, offvalue =0,variable = t3)
chbtn3todos.place(x = 100, y= 180)

chbtn4todos = Checkbutton(frmtodos, text = "Atención de PQR`s en obra, y veedurías", background = 'white', onvalue = 1, offvalue =0,variable = t4)
chbtn4todos.place(x = 100, y= 210)

chbtn5todos = Checkbutton(frmtodos, text = "Atención de contingencias", background = 'white', onvalue = 1, offvalue =0,variable = t5)
chbtn5todos.place(x = 100, y= 240)

chbtn6todos = Checkbutton(frmtodos, text = "Labores administrativas (organización laboral)", background = 'white', onvalue = 1, offvalue =0,variable = t6)
chbtn6todos.place(x = 100, y= 270)

chbtn7todos = Checkbutton(frmtodos, text = "Monitoreo y control (Plan de Seguimiento y Monitoreo)", background = 'white', onvalue = 1, offvalue =0,variable = t7)
chbtn7todos.place(x = 100, y= 300)

"//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////"

btnslccnr = Button(master, text = "Seleccionar Impactos", command = guardar, width = 20)
btnslccnr.place(x = 800, y = 400)

mrcrtodas = Button(master, text = "Desmarcar Todas", command =dmarcartodas, width = 20)
mrcrtodas.place(x = 800, y = 350)

dmrcrtodas = Button(master, text = "Marcar Todas", command = marcartodas, width = 20)
dmrcrtodas.place(x = 800, y = 300)




"//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////"
#DEFIIMOS NUESTRAS FUNCIONES

botones= [chbtn1plncn,chbtn2plncn,chbtn3plncn,
		chbtn1cnstrccn,chbtn2cnstrccn,chbtn3cnstrccn,chbtn4cnstrccn,chbtn5cnstrccn,chbtn6cnstrccn,chbtn7cnstrccn,chbtn8cnstrccn,chbtn9cnstrccn,chbtn10cnstrccn,chbtn11cnstrccn,
        chbtn1oprcn,chbtn2oprcn,chbtn3oprcn,chbtn4oprcn,chbtn5oprcn,chbtn6oprcn,chbtn7oprcn,chbtn8oprcn,chbtn9oprcn,
        chbtn1abndn,chbtn2abndn,chbtn3abndn,chbtn4abndn,
        chbtn1abdndyoprcn,chbtn2abndnyoprcn,
        chbtn1todos,chbtn2todos,chbtn3todos,chbtn4todos,chbtn5todos,chbtn6todos,chbtn7todos]


ind = open('pusuario.txt','r')

lt = []
ind.seek(0,0)
x = int(ind.readline())
RActProy.listaproyectos[x]=1
for i in range(36):
	lt.append(RActProy.matrizsugerencias[i][x])
print(lt)
for i in range(36):
	if(lt[i]==1):
		print(i)
		botones[i].config(background="light blue")


master.mainloop()