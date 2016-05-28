
import  os
import sys
from tkinter import *
#import RActProy
#import Form3
#from Form3 import *

master = Tk()
master.geometry("1200x550+0+0")
master.config(bg= "white")
master.title("Aplicativo de Simulacion Costos, Por Santiago Vélez Aristizabal")

guardado = open('g.txt', 'w+')

valor = ""

"///////////////////////////////////////////////////////////////////////////////////////////////////////////////////"

#Valor de mi variable según curselection
a1 = "Mantenimiento manual de vías: rocería, limpieza de obras de drenaje, limpieza y reparación de señales.".split(' ')

a2 = "Mantenimiento mecánico de vías: remoción de derrumbes, perfilado y compactación de superficie, reconstrucción de cunetas.".split(' ')

a3 = "Mantenimiento rutinario de vías: Incluye las actividades de mantenimiento manual / mecánico, reparación de baches en afirmado y reparcheos en pavimento".split(' ')

a4 = "Mantenimiento periódico: Incluye las actividades de mantenimiento rutinario; Mantenimiento de obras de drenaje y de paso; Reposición de pavimento, recuperación de estructura de pavimento; Recuperación/reconstrucción de estructura/espesores de afirmado; Construcción de obras de protección / muros de contención; Reconstrucción de obras de drenaje; Recuperación de señalización horizontal y vertical; Mantenimiento de puentes.".split(' ')

a5 = "Rehabilitación de rasante de vías: Construcción obras de drenaje; Recuperación/reconstrucción de estructura/espesores de afirmado; Reposición de pavimento, recuperación de estructura de pavimento; Construcción obras de estabilización de taludes / contención ".split(' ')

a6 = "Rehabilitación de puntos críticos viales: Construcción obras de estabilización de taludes / contención; Construcción de calzadas/viaductos otras obras de paso; Construcción obras de estabilización de taludes / contención ".split(' ')

a7 = "Mejoramiento vial: Estabilización físico-química de afirmados; Construcción afirmados; Tratamiento superficial doble riego; Pavimentación pavimento rígido; Pavimentación pavimento flexible; Rectificación alineamiento vertical/horizontal; Ampliación calzada / construcción nuevos carriles; Construcción de obras de drenaje y sub-drenaje (filtros); Reposición/instalación señalización horizontal; Reposición/instalación señalización vertical; Reposición/instalación iluminación; Construcción de redes de iluminación".split(' ')

a8 = "Mantenimiento rutinario de puentes".split(' ')

a9 = "Rehabilitación estructural de puentes".split(' ')

a10 = "Reposición de elementos del puente".split(' ')

a11= "Construcción de obras de protección de puentes".split(' ')

a12= "Mantenimiento obras de protección".split(' ')

a13= "Construcción de puentes".split(' ')

a14= "Pavimentación de vías urbanas: Construcción de pavimento rígido; Construcción de pavimento flexible; Construcción otros tipo de pavimento; Bacheo; Reparcheos, reconstrucción".split(' ')

a15= "Mantenimiento electromecánico de cables aéreos".split(' ')

a16= "Mantenimiento rutinario y mantenimiento sistemas electromecánicos de túneles".split(' ')

a17= "Construcción de túneles".split(' ')

a18= "Mantenimiento mecánico de vías terciarias".split(' ')

a19= "Construcción de rieles".split(' ')

a20= "Construcción de pavimento placa-huella".split(' ')

a21= "Construcción de obras de iluminación, obras complementarias".split(' ')

a22= "Construcción de redes de acueducto, alcantarillado".split(' ')

a23= "Construcción de redes de transmisión eléctrica".split(' ')

a24= "Mantenimiento de parques municipales / corregimentales".split(' ')

a25= "Reposición de redes".split(' ')

a26= "Mantenimiento preventivo y correctivo de plazas de mercado y u otras infraestructura municipales.".split(' ')

a27= "Ampliación de plazas de mercado y u otras infraestructura municipales.".split(' ')

a28= "Estudios y diseños: Estudios y diseños de alternativas técnico-ambientales; Estudios y diseños de pavimento prefactibilidad; Estudios y diseños de pavimento factibilidad; Estudios y diseños de valorización prefactibilidad; Estudios y diseños de valorización factibilidad; Estudios y diseños puentes; Estudios y diseños de rehabilitación afirmado; otros estudios".split(' ')

a29= "Construcción de infraestructura de acueducto y alcantarillado: Construcción de todos los elementos que configuran los sistemas de potabilización (tanques, desarenadores, floculadores, etc); Construcción de plantas de tratamiento de aguas residuales; Construcción sistemas de bombeo; Construcción de sistemas no convencionales".split(' ')

a30= "Construcción de rellenos sanitarios: Construcción de rellenos sanitarios a cielo abierto; Implementación planes de abandono; Construcción de plantas de tratamiento de residuos hospitalarios".split(' ')

a31 = "Optimización infraestructura de acueducto y alcantarillado: Optimización de elementos que configuran los sistemas de potabilización (tanques, desarenadores, floculadores, etc); optimización de plantas de tratamiento de aguas residuales; Optimización de sistemas de bombeo; optimización de sistemas no convencionales".split(' ')

a32= "Construcción de vivienda nueva, parques educativos, equipamientos para la prestación de servicios de salud, culturales/patrimoniales".split(' ')

a33= "Mejoramiento de vivienda".split(' ')

a34= "Reconstrucción (reposición) / reubicación de sedes educativas, culturales/patrimoniales".split(' ')

a35= "Mantenimiento preventivo y correctivo de equipamientos educativos, equipamientos para la prestación de servicios de salud, culturales/patrimoniales".split(' ')

a36= "Ampliación de equipamientos educativos, equipamientos para la prestación de servicios de salud, culturales/patrimoniales".split(' ')

a37= "Obras de iluminación, aire acondicionado, reposición de redes de servicios domiciliarios".split(' ')

"/////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////"

#EVALUAMOS EL VALOR DEL CURSELECT 
tod = [a1,a2,a3,a4,a5,a6,a7,a8,a9,a10,a11,a12,a13,a14,a15,a16,a17,a18,a19,a20,a21,a22,a23,a24,a25,a26,a27,a28,a29,a30,a31,a32,a33,a34,a35,a36,a37]
def guardar():
	linea = lista.get(lista.curselection())
	#guardado.seek(0,2)
	g = linea.split()
	x = tod.index(g)
	guardado.write(str(x))
	guardado.close()
	print(x)
	master.destroy()
	import Form3


"//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////"

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



"///////////////////////////////////////////////////////////////////////////////////////////////"

#RADIOBUTTONS

radiobtnlineal = Radiobutton(master, variable = valor, background = "white", text = "Lineal", command = fncLineal, value = 0)
radiobtnlineal.place(x= 50, y = 40)

radiobtncntrado = Radiobutton(master, variable = valor, background = "white", text = "Concentrado", command = fncConcentrado, value = 1)
radiobtncntrado.place(x = 110, y = 40)

"////////////////////////////////////////////////////////////////////////////////////////////////"


txt1 = Label(master, text = 'Por favor, seleccione el tipo de proyecto a desarrollar, luego de la selección, haga click en el botón "Seleccionar Actividades"', background = "white")
txt1.place(x = 50, y = 15)

big = Frame(bg = 'Black', height = 372, width = 1120)
big.place(x = 40, y= 70)
lista = Listbox(big, activestyle = 'dotbox', bg = 'white', height = '23', width = 600)
lista.place(x = 0, y = 0)
boton = Button(master, height = 2, width = 20, text = "Seleccionar actividades", command = guardar)
boton.place(x = 840, y = 460)

archivoLineal = open('lineal.txt', 'r')
archivoConcentrado = open('concentrado.txt', 'r')

"////////////////////////////////////////////////////////////////////////////////////////////////////"

for i in range(25):
		lista.insert(END, archivoLineal.readline())
radiobtnlineal.select()

master.mainloop()