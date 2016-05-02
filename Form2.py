#!/usr/bin/env python
# -*- coding: utf-8 -*-

import  os
import sys
from tkinter import *

master = Tk()
master.geometry("1200x550+0+0")
master.config(bg= "white")
master.title("Aplicativo de Simulacion Costos, Por Santiago Vélez Aristizabal")

nuevo = open('nuevo.txt', 'r+')

valor = ""

#Ciclo que me llena cada línea del listbox con cada línea del Archivo 'text.txt'

def fncLineal():
	archivoLineal.seek(0,0)
	lista.delete(0, END)
	for i in range(25):
		lista.insert(END, archivoLineal.readline())

def fncConcentrado():
	archivoConcentrado.seek(0,0)
	lista.delete(0, END)
	for i in range(25):
		lista.insert(END, archivoConcentrado.readline())

def guardar():
	linea = lista.get(lista.curselection())
	nuevo.seek(0,2)
	nuevo.write(linea)


"///////////////////////////////////////////////////////////////////////////////////////////////"

#RADIOBUTTONS

radiobtnlineal = Radiobutton(master, variable = valor, background = "white", text = "Lineal", command = fncLineal, value = 0)
radiobtnlineal.place(x= 50, y = 40)

radiobtncntrado = Radiobutton(master, variable = valor, background = "white", text = "Concentrado", command = fncConcentrado, value = 1)
radiobtncntrado.place(x = 110, y = 40)

"////////////////////////////////////////////////////////////////////////////////////////////////"


txt1 = Label(master, text = 'Por favor, seleccione el tipo de proyecto a desarrollar, luego de la selección, haga click en el botón "Seleccionar Actividades"', background = "white")
txt1.place(x = 50, y = 15)

big = Frame(bg = 'Black', height = 372, width = 1000)
big.place(x = 50, y= 70)
lista = Listbox(big, activestyle = 'dotbox', bg = 'white', height = '23', width = 600)
lista.place(x = 0, y = 0)
boton = Button(master, height = 2, width = 20, text = "Seleccionar actividades", command = guardar)
boton.place(x = 840, y = 450)

archivoLineal = open('lineal.txt', 'r')
archivoConcentrado = open('concentrado.txt', 'r')

"////////////////////////////////////////////////////////////////////////////////////////////////////"

for i in range(25):
		lista.insert(END, archivoLineal.readline())
radiobtnlineal.select()

master.mainloop()