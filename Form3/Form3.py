#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
from tkinter import *
import sys

master = Tk()
master.geometry("1200x550+0+0")
master.config(bg= "white")
master.title("Aplicativo de Simulacion Costos, Por Santiago Vélez Aristizabal")

"//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////"

#DEFIIMOS NUESTRAS FUNCIONES

def fncPlaneacion():
	archivoPlaneacion.seek(0,0)
	lista.delete(0, END)
	for i in range(25):
		lista.insert(END, archivoPlaneacion.readline())

def fncConstruccion():
	archivoConstruccion.seek(0,0)
	lista.delete(0, END)
	for i in range(25):
		lista.insert(END, archivoConstruccion.readline())

def fncOperacion():
	archivoOperacion.seek(0,0)
	lista.delete(0, END)
	for i in range(25):
		lista.insert(END, archivoOperacion.readline())

def fncAbandono():
	archivoAbandono.seek(0,0)
	lista.delete(0, END)
	for i in range(25):
		lista.insert(END, archivoAbandono.readline())

def todos():
	archivoTodos.seek(0,0)
	lista.delete(0, END)
	for i in range(25):
		lista.insert(END, archivoTodos.readline())

def guardar():
	linea = lista.get(lista.curselection())
	nuevo.seek(0,2)
	nuevo.write(linea)
