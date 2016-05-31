import numpy as np
import os
from tkinter import *
import sys

app = Tk()
app.geometry("1000x400+0+0")
app.config(background="white")
app.title("Form5")

"/////////////////////////////////////////////////////////////////////////////////////"

#Frames para cada programa de manejo
frm1 = Frame(bg="white",width=1000,height=500)
frm2 = Frame(bg="white",width=1000,height=500)
frm3 = Frame(bg="white",width=1000,height=500)
frm4 = Frame(bg="white",width=1000,height=500)
frm5 = Frame(bg="white",width=1000,height=500)
frm6 = Frame(bg="white",width=1000,height=500)
frm7 = Frame(bg="white",width=1000,height=500)
frm8= Frame(bg="white",width=1000,height=500)
frm9= Frame(bg="white",width=1000,height=500)
frm10 = Frame(bg="white",width=1000,height=500)
frm11= Frame(bg="white",width=1000,height=500)
frm12 = Frame(bg="white",width=1000,height=500)
frm13 = Frame(bg="white",width=1000,height=500)
frm14= Frame(bg="white",width=1000,height=500)


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
f3c13 = IntVar()
f3c14 = IntVar()
f3c15 = IntVar()
f3c16 = IntVar()

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

app.mainloop()



















