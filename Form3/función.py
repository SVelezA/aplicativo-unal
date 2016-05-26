import sys
from tkinter import *
import os
import numpy as np
import RActProy

master = Tk()
master.geometry("600x600+0+0")
master.config(bg= "white")
master.title("test del algoritmo")

v = IntVar()

def enviar():
		var = v.get()
		var = int(var)
		if var > 4:
			print("El número excede el índice de columnas de la matriz")
		else:		
			for i in range(5):
				if i == v:
					listaproy[i] = v


def actualizar():
	text33.config(background = 'gray')
	text22.config(background= 'gray')
	text11.config(background= 'gray')
	text44.config(background= 'gray')
	text55.config(background = 'gray')
	j = v.get()
	if j > 4:
		print("El número excede el índice de columnas de la matriz")
	else:
		if matrizej[0,j]==1:
			text11.config(background= "light blue")
		if matrizej[1,j]==1:
			text22.config(background= 'light blue')
		if matrizej[2,j]==1:
			text33.config(background = 'light blue')
		if matrizej[3,j]==1:
			text44.config(background= 'light blue')
		if matrizej[4,j]==1:
			text55.config(background = 'light blue')



						#0a  1a  2a  3a  4a

listaproy = 				 [0,  0,  0,  0,  0]

matrizej = np.array([[0,  1,  0,  0,  1], #0
										 [0,  0,  1,  0,  0], #1
										 [0,  1,  0,  1,  0], #2
										 [0,  0,  1,  0,  0], #3
										 [0,  1,  1,  1,  1]] #4
										 ) 

										 #1  2  3  4  5	

veces =     				 [0, 0, 0, 0, 0]

entry = Entry(master, textvariable = v).place(x = 50, y= 10)

actualizar = Button(master, text = "Actualizar", command = actualizar)
actualizar.place(x = 280, y = 10)

send = Button(master, text = "Send", command = enviar)
send.place(x = 150, y = 10)

text11 = Label(master, text = " ", width = 30)
text11.place(x = 200, y = 200)

text22= Label(master, text = " ", width = 30 )
text22.place(x = 200, y = 230)

text33 = Label(master, text = " ", width = 30 )
text33.place(x = 200, y = 260)

text44 = Label(master, text = " ", width = 30 )
text44.place(x = 200, y = 290)

text55 = Label(master, text = " ", width = 30 )
text55.place(x = 200, y = 320)

master.mainloop()