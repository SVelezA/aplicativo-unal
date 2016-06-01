#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys
from tkinter import *

master = Tk()
master.geometry("710x450+0+0")
master.config(bg= "white")
master.title("Aplicativo de Simulacion Costos, Por Santiago Vélez Aristizabal")


manodeobra = DoubleVar()
materiales = DoubleVar()
equipos = DoubleVar()
transporte = DoubleVar()
complejidad = ""
promedionotepad = open('complejidad.txt', 'w+')

def abrir():
	os.startfile(r'C:\Users\Santiago\Desktop\Proyecto\1.01\ProyectoUsuario.py')
	master.destroy()

def promedio():
	total = (manodeobra.get()+materiales.get()+equipos.get()+transporte.get())
	total = round(total, 1)
	promediotxt.config(text= total)
	if total > 3.5:
		complejidadtxt.config(text = "Proyecto de complejidad Alta")
	elif total < 3.5 and total > 2.5:
		complejidadtxt.config(text = "Proyecto de complejidad Media")
	elif total < 2.5 and total >= 0:
		complejidadtxt.config(text = "Proyecto de complejidad Baja")
	promedionotepad.write(str(total))

boton1 = Button(master, text="Seleccione el tipo de proyecto", command = abrir)
boton1.place(x=270, y= 350)

"//////////////////////////////////////////////////////////////////////////////////////////////////////////"

#TITULOS DE LA VENTANA Y PIE DE PÁGINA

titulo = Label(master, text= "Aplicativo de simulación de costos", background = "white")
titulo.place(x=230, y= 15)

descripcion1 = Label(master, text = "A continuación, seleccione las condiciones particulares de su proyecto.", background = "white")
descripcion2 = Label(master, text = 'Luego, indique el programa que quiere costear y haga click en "Seleccionar proyecto"', background = "white")
descripcion1.place(x = 165, y = 50)
descripcion2.place(x = 125, y = 68)

pie = Label(master, text = "Elaborado por la Universidad Nacional de Colombia - Sede Medellín", background = "white")
pie.place(x=190, y = 410)

"//////////////////////////////////////////////////////////////////////////////////////////////////////////"

#RADIOBUTTONS PARA "MANO DE OBRA"

manodeobra1 = Radiobutton(master, variable = manodeobra, value = 0.25, command= promedio, background="white")
manodeobra2 = Radiobutton(master, variable = manodeobra, value = 0.5, command= promedio, background="white")
manodeobra3 = Radiobutton(master, variable = manodeobra, value = 0.75, command = promedio, background="white")
manodeobra4 = Radiobutton(master, variable = manodeobra, value = 1, command = promedio, background="white")
manodeobra5 = Radiobutton(master, variable = manodeobra, value = 1.25, command = promedio, background="white")

manodeobra1.place(x=240, y= 125)
manodeobra2.place(x = 325, y = 125)
manodeobra3.place(x= 400, y= 125)
manodeobra4.place(x = 475, y = 125)
manodeobra5.place(x= 550, y= 125)

"/////////////////////////////////////////////////////////////////////////////////////////////////"

#RADIOBUTTONS PARA "MATERIALES"

materiales1 = Radiobutton(master, variable = materiales, value = 0.25, command= promedio, background="white")
materiales2= Radiobutton(master, variable = materiales, value = 0.5, command= promedio, background="white")
materiales3 = Radiobutton(master, variable = materiales, value = 0.75, command = promedio, background="white")
materiales4 = Radiobutton(master, variable = materiales, value = 1, command = promedio, background="white")
materiales5 = Radiobutton(master, variable = materiales, value = 1.25, command = promedio, background="white")

materiales1.place(x=240, y= 170)
materiales2.place(x = 325, y = 170)
materiales3.place(x= 400, y= 170)
materiales4.place(x = 475, y = 170)
materiales5.place(x= 550, y= 170)

"/////////////////////////////////////////////////////////////////////////////////////////////////"

#RADIOBUTTONS PARA "EQUIPOS"

equipos1 = Radiobutton(master, variable = equipos, value = 0.25, command= promedio, background="white")
equipos2 = Radiobutton(master, variable = equipos, value = 0.5, command= promedio, background="white")
equipos3 = Radiobutton(master, variable = equipos, value = 0.75, command = promedio, background="white")
equipos4 = Radiobutton(master, variable = equipos, value = 1, command = promedio, background="white")
equipos5 = Radiobutton(master, variable = equipos, value = 1.25, command = promedio, background="white")

equipos1.place(x=240, y= 215)
equipos2.place(x = 325, y = 215)
equipos3.place(x= 400, y= 215)
equipos4.place(x = 475, y = 215)
equipos5.place(x= 550, y= 215)

"/////////////////////////////////////////////////////////////////////////////////////////////////"

#RADIOBUTTONS PARA "TRANSPORTE"

transporte1 = Radiobutton(master, variable = transporte, value = 0.25, command= promedio, background="white")
transporte2 = Radiobutton(master, variable = transporte, value = 0.5, command= promedio, background="white")
transporte3 = Radiobutton(master, variable = transporte, value = 0.75, command = promedio, background="white")
transporte4 = Radiobutton(master, variable = transporte, value = 1, command = promedio, background="white")
transporte5 = Radiobutton(master, variable = transporte, value = 1.25, command = promedio, background="white")

transporte1.place(x= 240, y= 260)
transporte2.place(x = 325, y = 260)
transporte3.place(x= 400, y= 260)
transporte4.place(x = 475, y = 260)
transporte5.place(x= 550, y= 260)

"/////////////////////////////////////////////////////////////////////////////////////////////////"

#Texto para mostrar el promedio de complejidad del proyecto

promediotxt = Label(master, text = "0.0", background="white")
promediotxt.place(x = 310, y = 305, width = 40, height= 20)

lbl1 = Label(master, text = "Complejidad del Proyecto", background= "white")
lbl1.place(x=90, y= 305, width = 220, height = 20)

complejidadtxt = Label(master, text = "Proyecto de complejidad: " + complejidad, background = "white")
complejidadtxt.place(x=370, y = 303)

"///////////////////////////////////////////////////////////////////////////////////////////////////"

#TITULOS

vrbltxt = Label(master, text = "Variable", background = "white")
vrbltxt.place(x = 110, y = 90)

basetxt = Label(master, text = "Base", background = "white")
basetxt.place(x = 230, y = 90)

bmediotxt = Label(master, text = "Base-Medio", background = "white")
bmediotxt.place (x = 290, y = 90)

mediotxt = Label(master, text = "Medio", background = "white")
mediotxt.place(x = 385, y = 90)

medioaltotxt = Label(master, text = "Medio-Alto", background = "white")
medioaltotxt.place(x = 450, y = 90)

altotxt = Label(master, text = "Alto", background = "white")
altotxt.place(x = 545, y = 90)


"////////////////////////////////////////////////////////////////////////////////////////////////////"

#DESCRIPCION DE LAS VARIABLES A EVALUAR

mnobratxt = Label(master, text = "Mano de Obra \nno calificada", background="white")
mnobratxt.place(x=100, y = 125, height = 30)

mtrlstxt = Label(master, text = "Materiales", background="white")
mtrlstxt.place(x=110, y = 170)

equipostxt = Label(master, text= "Equipos", background = "white")
equipostxt.place(x= 115, y = 215)

trnsprtxt = Label(master, text = "Transporte", background = "white")
trnsprtxt.place(x=110, y = 260)

"////////////////////////////////////////////////////////////////////////////////////////////////"

#Creamos nuevas fuentes para nuestra conveniencia y se las aplicamos a nuestros label

labelfont = ("Calibri", 12, 'bold')
titlefont = ("Calibri", 13, 'bold')

promediotxt.config(font= labelfont)
lbl1.config(font= labelfont)
vrbltxt.config(font = titlefont)
basetxt.config(font = titlefont)
bmediotxt.config(font = titlefont)
mediotxt.config(font = titlefont)
medioaltotxt.config(font = titlefont)
altotxt.config(font = titlefont)
complejidadtxt.config(font = labelfont)
titulo.config(font = titlefont)


miarchivo = open("Base.txt", "w+")

master.mainloop()