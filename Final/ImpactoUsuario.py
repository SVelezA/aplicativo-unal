import os
import sys
from tkinter import *
import RActImp

app = Tk()
app.geometry("1000x400+0+0")
app.config(background="white")
app.title("Selección de Impactos")

save1 = open('actusuario.txt', 'r')
impusuario = open('impusuario.txt', 'w+')

"//////////////////////////////////////////////////////////////////////////////////////////////////"
#Frames para cada tipo de impacto

frmAg = Frame(bg="white",width=1000,height=500)
frmAi = Frame(bg="white",width=1000,height=500)
frmSue = Frame(bg="white",width=1000,height=500)
frmPro = Frame(bg="white",width=1000,height=500)
frmEuc = Frame(bg="white",width=1000,height=500)
frmPyR = Frame(bg="white",width=1000,height=500)
frmPai = Frame(bg="white",width=1000,height=500)
frmEc = Frame(bg="white",width=1000,height=500)
frmSc = Frame(bg="white",width=1000,height=500)
frmPol = Frame(bg="white",width=1000,height=500)

frmAg.grid()


"//////////////////////////////////////////////////////////////////////////////////////////////////////"
#Funciones para mostrar cada frame

def Agua():
	frmAg.grid()
	frmAi.grid_remove()
	frmSue.grid_remove()
	frmPro.grid_remove()
	frmEuc.grid_remove()
	frmPyR.grid_remove()
	frmPai.grid_remove()
	frmEc.grid_remove()
	frmSc.grid_remove()
	frmPol.grid_remove()

def Aire():
	frmAg.grid_remove()
	frmAi.grid()
	frmSue.grid_remove()
	frmPro.grid_remove()
	frmEuc.grid_remove()
	frmPyR.grid_remove()
	frmPai.grid_remove()
	frmEc.grid_remove()
	frmSc.grid_remove()
	frmPol.grid_remove()

def Suelo():
	frmAg.grid_remove()
	frmAi.grid_remove()
	frmSue.grid()
	frmPro.grid_remove()
	frmEuc.grid_remove()
	frmPyR.grid_remove()
	frmPai.grid_remove()
	frmEc.grid_remove()
	frmSc.grid_remove()
	frmPol.grid_remove()

def Procariota():
	frmAg.grid_remove()
	frmAi.grid_remove()
	frmSue.grid_remove()
	frmPro.grid()
	frmEuc.grid_remove()
	frmPyR.grid_remove()
	frmPai.grid_remove()
	frmEc.grid_remove()
	frmSc.grid_remove()
	frmPol.grid_remove()

def Eucariota():
	frmAg.grid_remove()
	frmAi.grid_remove()
	frmSue.grid_remove()
	frmPro.grid_remove()
	frmEuc.grid()
	frmPyR.grid_remove()
	frmPai.grid_remove()
	frmEc.grid_remove()
	frmSc.grid_remove()
	frmPol.grid_remove()

def Procesos():
	frmAg.grid_remove()
	frmAi.grid_remove()
	frmSue.grid_remove()
	frmPro.grid_remove()
	frmEuc.grid_remove()
	frmPyR.grid()
	frmPai.grid_remove()
	frmEc.grid_remove()
	frmSc.grid_remove()
	frmPol.grid_remove()

def Paisaje():
	frmAg.grid_remove()
	frmAi.grid_remove()
	frmSue.grid_remove()
	frmPro.grid_remove()
	frmEuc.grid_remove()
	frmPyR.grid_remove()
	frmPai.grid()
	frmEc.grid_remove()
	frmSc.grid_remove()
	frmPol.grid_remove()

def Económico():
	frmAg.grid_remove()
	frmAi.grid_remove()
	frmSue.grid_remove()
	frmPro.grid_remove()
	frmEuc.grid_remove()
	frmPyR.grid_remove()
	frmPai.grid_remove()
	frmEc.grid()
	frmSc.grid_remove()
	frmPol.grid_remove()

def Sociocultural():
	frmAg.grid_remove()
	frmAi.grid_remove()
	frmSue.grid_remove()
	frmPro.grid_remove()
	frmEuc.grid_remove()
	frmPyR.grid_remove()
	frmPai.grid_remove()
	frmEc.grid_remove()
	frmSc.grid()
	frmPol.grid_remove()

def Político():
	frmAg.grid_remove()
	frmAi.grid_remove()
	frmSue.grid_remove()
	frmPro.grid_remove()
	frmEuc.grid_remove()
	frmPyR.grid_remove()
	frmPai.grid_remove()
	frmEc.grid_remove()
	frmSc.grid_remove()
	frmPol.grid()

def guardar():
	impusuario.seek(0,0)
	sel = []
	for i in range(40):
		check = variablesl[i].get()
		sel.append(check)
	print(sel)
	print(str(sel))
	impusuario.write(str(sel))
	impusuario.close()
	app.destroy()
	import MedidaUsuario


def marcartodas():
	for i in range(40):
		botones[i].select()

def dmarcartodas():
	for i in range(40):
		botones[i].deselect()

"//////////////////////////////////////////////////////////////////////////////////////////////////////"
#Variables de los checkbuttons

#Agua
ag1 = IntVar()
ag2 = IntVar()
ag3 = IntVar()
ag4 = IntVar()

#Aire
ai1 = IntVar()
ai2 = IntVar()
ai3 = IntVar()
ai4 = IntVar()

#Suelo
sue1 = IntVar()
sue2 = IntVar()
sue3 = IntVar()
sue4 = IntVar()

#Procariota
pro1 = IntVar()
pro2 = IntVar()
pro3 = IntVar()
pro4 = IntVar()

#Eucariota
euc1 = IntVar()
euc2 = IntVar()
euc3 = IntVar()
euc4 = IntVar()

#Procesos y relaciones
pyr1 = IntVar()
pyr2 = IntVar()
pyr3 = IntVar()
pyr4 = IntVar()

#Paisaje
pai1 = IntVar()
pai2 = IntVar()
pai3 = IntVar()
pai4 = IntVar()

#Economico
ec1 = IntVar()
ec2 = IntVar()
ec3 = IntVar()
ec4 = IntVar()

#Socioeconomico
sc1 = IntVar()
sc2 = IntVar()
sc3 = IntVar()
sc4 = IntVar()

#Politico
pol1 = IntVar()
pol2 = IntVar()
pol3 = IntVar()
pol4 = IntVar()


"//////////////////////////////////////////////////////////////////////////////////////////////////////"
#Encabezado y boton

text1 = Label(app,text="Por favor seleccione los posibles impactos ambientales que tendrá el proyecto. Recuerde que los  componentes ambientales son  \n Agua, Aire, Suelo, Procariota, Eucariota, Procesos y Relaciones, Paisaje, Económico, Sociocultural y Político. \n Luego de la selección, haga clic en el botón 'Seleccionar medidas'",background="white")
text1.place(x=120,y=20)

"//////////////////////////////////////////////////////////////////////////////////////////////////////"

#Radiobuttons para cada tipo de impacto
rdbtnAg = Radiobutton(app,text="Agua",width=5,value=0,command=Agua,background="white")
rdbtnAg.place(x=100-50,y=70)
rdbtnAg.select()

rdbtnAi = Radiobutton(app,text="Aire",width=5,value=1,command=Aire,background="white")
rdbtnAi.place(x=160-50,y=70)
rdbtnAi.deselect()

rdbtnSue = Radiobutton(app,text="Suelo",width=3,value=2,command=Suelo,background="white")
rdbtnSue.place(x=230-50,y=70)
rdbtnSue.deselect()

rdbtnPro = Radiobutton(app,text="Procariota",width=7,value=3,command=Procariota,background="white")
rdbtnPro.place(x=290-50,y=70)
rdbtnPro.deselect()

rdbtnEuc = Radiobutton(app,text="Eucariota",width=6,value=4,command=Eucariota,background="white")
rdbtnEuc.place(x=380-50,y=70)
rdbtnEuc.deselect()

rdbtnPyR = Radiobutton(app,text="Procesos y Relaciones",width=15,value=5,command=Procesos,background="white")
rdbtnPyR.place(x=465-50,y=70)
rdbtnPyR.deselect()

rdbtnPai = Radiobutton(app,text="Paisaje",width=5,value=6,command=Paisaje,background="white")
rdbtnPai.place(x=610-50,y=70)
rdbtnPai.deselect()

rdbtnEc = Radiobutton(app,text="Económico",width=7,value=7,command=Económico,background="white")
rdbtnEc.place(x=685-50,y=70)
rdbtnEc.deselect()

rdbtnSo = Radiobutton(app,text="Sociocultural",width=10,value=8,command=Sociocultural,background="white")
rdbtnSo.place(x=775-50,y=70)
rdbtnSo.deselect()

rdbtnPol = Radiobutton(app,text="Político",width=5,value=9,command=Político,background="white")
rdbtnPol.place(x=880-50,y=70)
rdbtnPol.deselect()


"/////////////////////////////////////////////////////////////////////////////////////////////////////////////"
#Checkbuttons impacto agua

chbtn1Ag = Checkbutton(frmAg,text="Alteración de la calidad físico química del agua",onvalue=1,offvalue=0,background="white",variable=ag1)
chbtn1Ag.place(x=50,y=100)
chbtn2Ag = Checkbutton(frmAg,text="Alteración de la dinámica fluvial: curso y dirección",onvalue=1,offvalue=0,background="white",variable=ag2)
chbtn2Ag.place(x=50,y=130)
chbtn3Ag = Checkbutton(frmAg,text="Disminución de caudal disponible",onvalue=1,offvalue=0,background="white",variable=ag3)
chbtn3Ag.place(x=50,y=160)
chbtn4Ag = Checkbutton(frmAg,text="Afectación al sistema de drenaje desviación, obstaculización, pérdida de conectividad",onvalue=1,offvalue=0,background="white",variable=ag4)
chbtn4Ag.place(x=50,y=190)

"/////////////////////////////////////////////////////////////////////////////////////////////////////////////"
#Checkbuttons impacto aire

chbtn1Ai = Checkbutton(frmAi,text="Aumento de los niveles de ruido ambiental",onvalue=1,offvalue=0,background="white",variable=ai1)
chbtn1Ai.place(x=50,y=100)
chbtn2Ai = Checkbutton(frmAi,text="Aumento en la dispersión de olores ofensivos",onvalue=1,offvalue=0,background="white",variable=ai2)
chbtn2Ai.place(x=50,y=130)
chbtn3Ai = Checkbutton(frmAi,text="Deterioro de la calidad de aire: aumento en la concentración de gases y material particulado",onvalue=1,offvalue=0,background="white",variable=ai3)
chbtn3Ai.place(x=50,y=160)
chbtn4Ai = Checkbutton(frmAi,text="Aumento en la presencia de nieblas, aerosoles o similares, ondas electromagnéticas",onvalue=1,offvalue=0,background="white",variable=ai4)
chbtn4Ai.place(x=50,y=190)

"/////////////////////////////////////////////////////////////////////////////////////////////////////////////"
#Checkbuttons impacto Suelo

chbtn1Sue = Checkbutton(frmSue,text="Alteración de las características físico químicas del suelo",onvalue=1,offvalue=0,background="white",variable=sue1)
chbtn1Sue.place(x=50,y=100)
chbtn2Sue = Checkbutton(frmSue,text="Aumento en la presencia de fenómenos de inestabilidad, remoción en masa",onvalue=1,offvalue=0,background="white",variable=sue2)
chbtn2Sue.place(x=50,y=130)
chbtn3Sue = Checkbutton(frmSue,text="Aumento en la presencia de procesos erosivos, socavación y pérdida de suelo",onvalue=1,offvalue=0,background="white",variable=sue3)
chbtn3Sue.place(x=50,y=160)
chbtn4Sue = Checkbutton(frmSue,text="Compactación del suelo",onvalue=1,offvalue=0,background="white",variable=sue4)
chbtn4Sue.place(x=50,y=190)

"/////////////////////////////////////////////////////////////////////////////////////////////////////////////"
#Checkbuttons impacto Procariota

chbtn1Pro = Checkbutton(frmPro,text="Aumento en la concentración de microorganismos patógenos en agua y suelo",onvalue=1,offvalue=0,background="white",variable=pro1)
chbtn1Pro.place(x=50,y=100)
chbtn2Pro = Checkbutton(frmPro,text="Deterioro de la calidad microbiológica en agua y suelo",onvalue=1,offvalue=0,background="white",variable=pro2)
chbtn2Pro.place(x=50,y=130)
chbtn3Pro = Checkbutton(frmPro,text="Pérdida de abundancia y/o diversidad de especies procariotas (microflora y microfauna)",onvalue=1,offvalue=0,background="white",variable=pro3)
chbtn3Pro.place(x=50,y=160)
chbtn4Pro = Checkbutton(frmPro,text="Proliferación de masas microbianas en ambientes construidos",onvalue=1,offvalue=0,background="white",variable=pro4)
chbtn4Pro.place(x=50,y=190)

"/////////////////////////////////////////////////////////////////////////////////////////////////////////////"
#Checkbuttons impacto Eucariota

chbtn1Euc = Checkbutton(frmEuc,text="Atracción o expulsión de especies eucariotas (macroflora y macrofauna)",onvalue=1,offvalue=0,background="white",variable=euc1)
chbtn1Euc.place(x=50,y=100)
chbtn2Euc = Checkbutton(frmEuc,text="Intervención de especies en veda o amenaza",onvalue=1,offvalue=0,background="white",variable=euc2)
chbtn2Euc.place(x=50,y=130)
chbtn3Euc = Checkbutton(frmEuc,text="Pérdida de abundancia y/o diversidad de especies eucariotas terrestres o acuáticas",onvalue=1,offvalue=0,background="white",variable=euc3)
chbtn3Euc.place(x=50,y=160)
chbtn4Euc = Checkbutton(frmEuc,text="Pérdida de corredores biológicos, hábitat y matriz de vegetación, fragmentación",onvalue=1,offvalue=0,background="white",variable=euc4)
chbtn4Euc.place(x=50,y=190)

"/////////////////////////////////////////////////////////////////////////////////////////////////////////////"
#Checkbuttons impacto Procesos y relaciones

chbtn1PyR = Checkbutton(frmPyR,text="Alteración en los ciclos y rutas migratorias de seres vivos",onvalue=1,offvalue=0,background="white",variable=pyr1)
chbtn1PyR.place(x=50,y=100)
chbtn2PyR = Checkbutton(frmPyR,text="Alteración de los ciclos biogeoquímicos",onvalue=1,offvalue=0,background="white",variable=pyr2)
chbtn2PyR.place(x=50,y=130)
chbtn3PyR = Checkbutton(frmPyR,text="Obstrucción en las relaciones intraespecíficas",onvalue=1,offvalue=0,background="white",variable=pyr3)
chbtn3PyR.place(x=50,y=160)
chbtn4PyR = Checkbutton(frmPyR,text="Obstrucción en las relaciones interespecíficas",onvalue=1,offvalue=0,background="white",variable=pyr4)
chbtn4PyR.place(x=50,y=190)

"/////////////////////////////////////////////////////////////////////////////////////////////////////////////"
#Checkbuttons impacto Paisaje

chbtn1Pai = Checkbutton(frmPai,text="Alteración de la cuenca visual/visibilidad del paisaje",onvalue=1,offvalue=0,background="white",variable=pai1)
chbtn1Pai.place(x=50,y=100)
chbtn2Pai = Checkbutton(frmPai,text="Alteración de la geomorfología",onvalue=1,offvalue=0,background="white",variable=pai2)
chbtn2Pai.place(x=50,y=130)
chbtn3Pai = Checkbutton(frmPai,text="Afectación del paisaje construido",onvalue=1,offvalue=0,background="white",variable=pai3)
chbtn3Pai.place(x=50,y=160)
chbtn4Pai = Checkbutton(frmPai,text="Pérdida de la calidad subjetiva del paisaje",onvalue=1,offvalue=0,background="white",variable=pai4)
chbtn4Pai.place(x=50,y=190)

"/////////////////////////////////////////////////////////////////////////////////////////////////////////////"
#Checkbuttons impacto Economico

chbtn1Ec = Checkbutton(frmEc,text="Aumento en la tasa de empleo",onvalue=1,offvalue=0,background="white",variable=ec1)
chbtn1Ec.place(x=50,y=100)
chbtn2Ec = Checkbutton(frmEc,text="Aumento o disminución en el uso de un recurso natural",onvalue=1,offvalue=0,background="white",variable=ec2)
chbtn2Ec.place(x=50,y=130)
chbtn3Ec = Checkbutton(frmEc,text="Afectación de las actividades económicas",onvalue=1,offvalue=0,background="white",variable=ec3)
chbtn3Ec.place(x=50,y=160)
chbtn4Ec = Checkbutton(frmEc,text="Afectación en la tenencia de la tierra",onvalue=1,offvalue=0,background="white",variable=ec4)
chbtn4Ec.place(x=50,y=190)

"/////////////////////////////////////////////////////////////////////////////////////////////////////////////"
#Checkbuttons impacto Sociocultural

chbtn1Sc = Checkbutton(frmSc,text="Afectación del patrimonio histórico, arqueológico, natural y/o territorios colectivos",onvalue=1,offvalue=0,background="white",variable=sc1)
chbtn1Sc.place(x=50,y=100)
chbtn2Sc = Checkbutton(frmSc,text="Aumento/disminución en la oferta de servicios públicos, espacio público y vivienda, equipamietos",onvalue=1,offvalue=0,background="white",variable=sc2)
chbtn2Sc.place(x=50,y=130)
chbtn3Sc = Checkbutton(frmSc,text="Aumento/disminución de la densidad de población",onvalue=1,offvalue=0,background="white",variable=sc3)
chbtn3Sc.place(x=50,y=160)
chbtn4Sc = Checkbutton(frmSc,text="Reducción de las necesidades básicas insatisfechas",onvalue=1,offvalue=0,background="white",variable=sc4)
chbtn4Sc.place(x=50,y=190)

"/////////////////////////////////////////////////////////////////////////////////////////////////////////////"
#Checkbuttons impacto politico

chbtn1Pol = Checkbutton(frmPol,text="Favorecimiento de la participación comunitaria",onvalue=1,offvalue=0,background="white",variable=pol1)
chbtn1Pol.place(x=50,y=100)
chbtn2Pol = Checkbutton(frmPol,text="Mayor inversión, presencia del estado y las autoridades",onvalue=1,offvalue=0,background="white",variable=pol2)
chbtn2Pol.place(x=50,y=130)
chbtn3Pol = Checkbutton(frmPol,text="Potenciación de conflictos, manifestaciones, molestias y expectativas en la comunidad",onvalue=1,offvalue=0,background="white",variable=pol3)
chbtn3Pol.place(x=50,y=160)
chbtn4Pol = Checkbutton(frmPol,text="Incremento en los factores de riesgo natural y antrópico",onvalue=1,offvalue=0,background="white",variable=pol4)
chbtn4Pol.place(x=50,y=190)

"/////////////////////////////////////////////////////////////////////////////////////////////////////////////"

boton1 = Button(app,text="Seleccionar medidas", width = 20, command = guardar)
boton1.place(x=800,y=250)

mrcrtodas = Button(app, text = "Desmarcar Todas", command =dmarcartodas, width = 20)
mrcrtodas.place(x = 800, y = 350)

dmrcrtodas = Button(app, text = "Marcar Todas", command = marcartodas, width = 20)
dmrcrtodas.place(x = 800, y = 300)


"/////////////////////////////////////////////////////////////////////////////////////////////////////////////"

botones = [chbtn1Ag,chbtn2Ag,chbtn3Ag,chbtn4Ag,
		   chbtn1Ai,chbtn2Ai,chbtn3Ai,chbtn4Ai,
		   chbtn1Sue,chbtn2Sue,chbtn3Sue,chbtn4Sue,
		   chbtn1Pro,chbtn2Pro,chbtn3Pro,chbtn4Pro,
		   chbtn1Euc,chbtn2Euc,chbtn3Euc,chbtn4Euc,
		   chbtn1PyR,chbtn2PyR,chbtn3PyR,chbtn4PyR,
		   chbtn1Pai,chbtn2Pai,chbtn3Pai,chbtn4Pai,
		   chbtn1Ec,chbtn2Ec,chbtn3Ec,chbtn4Ec,
		   chbtn1Sc,chbtn2Sc,chbtn3Sc,chbtn4Sc,
		   chbtn1Pol,chbtn2Pol,chbtn3Pol,chbtn4Pol]

variablesl = [ag1, ag1, ag3, ag4, ai1, ai2, ai3, ai4, sue1, sue2, sue3, sue4, pro1, pro2, pro3, pro4, euc1, euc2, euc3, euc4, pyr1, pyr2, pyr3, pyr4, pai1, pai2, pai3, pai4, 
			ec1, ec2, ec3, ec4, sc1, sc2, sc3, sc4, pol1, pol2, pol3, pol4]

save1.seek(0,0)
x = eval(save1.readline())
suge = []
for i in range(len(x)):
	if x[i]==1:
		for j in range(len(RActImp.MatrizIA)):
			suge.append(RActImp.MatrizIA[j][i])
		for k in range(40):
			if suge[k] == 1:
				botones[k].config(background="light blue")
	suge = []


#parte para las sugerencias


app.mainloop()