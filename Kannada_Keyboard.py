#Two Bugs
# 1 : Adjust the scroll view
# 2 : Cannot edit from middle

import tkinter
from tkinter import *
import time

root = Tk()
root.title("Kannada_Keyboard_By_RAKi")
root.geometry('1366x760')
root.config(bg = '#ff0000')#00ccff
Yellow_Frame = Frame(root,bg = "yellow")
Yellow_Frame.place(x=0,y=0,width = 1366,height = 380)
Label(root,text = "RAKi",bg = "yellow",fg = "yellow").place(x = 73,y = 73)


global Text_Field
Str = ""
Text_Field = Text(root)
Text_Field.place(x=130,y =50,width = 1100,height = 280)
Text_Field.config(font = ('',20))

scrollbar = Scrollbar(root,command = Text_Field.yview)
scrollbar.place(x = 1230, y = 50,height = 280)
Text_Field.config(yscrollcommand = scrollbar.set,wrap = WORD)
#------------------------------------------------------------------------------
#Functions

def Press(Str1):
    global Str
    Str = Text_Field.get("1.0","end-1c")
    Str +=Str1
    Text_Field.delete(1.0,END)
    Text_Field.insert(END,Str)
    root.update()

def BackSpace_Pressed():
    global Str
    Str = Text_Field.get("1.0","end-1c")
    Str = Str[:-1]
    Text_Field.delete(1.0,END)
    Text_Field.insert(END,Str)
    root.update()


#------------------------------------------------------------------------------
#Widgets
A = Button(root,text = "\u0c85",font = ('',20),bg = 'white',command = lambda :Press("\u0c85"))
A.place(x=100,y=350,width = 50,height = 50)

Aa = Button(root,text = "\u0c86",font = ('',20),bg = 'white',command = lambda :Press("\u0c86"))
Aa.place(x=180,y=350,width = 50,height = 50)

E = Button(root,text = "\u0c87",font = ('',20),bg = 'white',command = lambda :Press("\u0c87"))
E.place(x=260,y=350,width = 50,height = 50)

Ee = Button(root,text = "\u0c88",font = ('',20),bg = 'white',command = lambda :Press("\u0c88"))
Ee.place(x=340,y=350,width = 50,height = 50)

U = Button(root,text = "\u0c89",font = ('',20),bg = 'white',command = lambda :Press("\u0c89"))
U.place(x=420,y=350,width = 50,height = 50)

Uu = Button(root,text = "\u0c8a",font = ('',20),bg = 'white',command = lambda :Press("\u0c8a"))
Uu.place(x=500,y=350,width = 50,height = 50)

RU = Button(root,text = "\u0c8b",font = ('',20),bg = 'white',command = lambda :Press("\u0c8b"))
RU.place(x=580,y=350,width = 50,height = 50)

AE = Button(root,text = "\u0c8e",font = ('',20),bg = 'white',command = lambda :Press("\u0c8e"))
AE.place(x=660,y=350,width = 50,height = 50)

AEe = Button(root,text = "\u0c8f",font = ('',20),bg = 'white',command = lambda :Press("\u0c8f"))
AEe.place(x=740,y=350,width = 50,height = 50)

I = Button(root,text = "\u0c90",font = ('',20),bg = 'white',command = lambda :Press("\u0c90"))
I.place(x=820,y=350,width = 50,height = 50)

O = Button(root,text = "\u0c92",font = ('',20),bg = 'white',command = lambda :Press("\u0c92"))
O.place(x=900,y=350,width = 50,height = 50)

Oo = Button(root,text = "\u0c93",font = ('',20),bg = 'white',command = lambda :Press("\u0c93"))
Oo.place(x=980,y=350,width = 50,height = 50)

OU = Button(root,text = "\u0c94",font = ('',20),bg = 'white',command = lambda :Press("\u0c94"))
OU.place(x=1060,y=350,width = 50,height = 50)
###########################

KA = Button(root,text = "\u0c95",font = ('',20),bg = 'white',command = lambda :Press("\u0c95"))
KA.place(x=100,y=410,width = 50,height = 50)

KHA = Button(root,text = "\u0c96",font = ('',20),bg = 'white',command = lambda :Press("\u0c96"))
KHA.place(x=180,y=410,width = 50,height = 50)


GA = Button(root,text = "\u0c97",font = ('',20),bg = 'white',command = lambda :Press("\u0c97"))
GA.place(x=260,y=410,width = 50,height = 50)


GHA = Button(root,text = "\u0c98",font = ('',20),bg = 'white',command = lambda :Press("\u0c98"))
GHA.place(x=340,y=410,width = 50,height = 50)


GNA = Button(root,text = "\u0c99",font = ('',20),bg = 'white',command = lambda :Press("\u0c99"))
GNA.place(x=420,y=410,width = 50,height = 50)


############################

CA = Button(root,text = "\u0c9a",font = ('',20),bg = 'white',command = lambda :Press("\u0c9a"))
CA.place(x=100,y=470,width = 50,height = 50)

CHA = Button(root,text = "\u0c9b",font = ('',20),bg = 'white',command = lambda :Press("\u0c9b"))
CHA.place(x=180,y=470,width = 50,height = 50)


JA = Button(root,text = "\u0c9c",font = ('',20),bg = 'white',command = lambda :Press("\u0c9c"))
JA.place(x=260,y=470,width = 50,height = 50)


JHA = Button(root,text = "\u0c9d",font = ('',20),bg = 'white',command = lambda :Press("\u0c9d"))
JHA.place(x=340,y=470,width = 50,height = 50)


INA = Button(root,text = "\u0c9e",font = ('',20),bg = 'white',command = lambda :Press("\u0c9e"))
INA.place(x=420,y=470,width = 50,height = 50)

############################

TTA = Button(root,text = "\u0c9f",font = ('',20),bg = 'white',command = lambda :Press("\u0c9f"))
TTA.place(x=100,y=530,width = 50,height = 50)

TTAA = Button(root,text = "\u0ca0",font = ('',20),bg = 'white',command = lambda :Press("\u0ca0"))
TTAA.place(x=180,y=530,width = 50,height = 50)


DDA = Button(root,text = "\u0ca1",font = ('',20),bg = 'white',command = lambda :Press("\u0ca1"))
DDA.place(x=260,y=530,width = 50,height = 50)


DDAA = Button(root,text = "\u0ca2",font = ('',20),bg = 'white',command = lambda :Press("\u0ca2"))
DDAA.place(x=340,y=530,width = 50,height = 50)


NNA = Button(root,text = "\u0ca3",font = ('',20),bg = 'white',command = lambda :Press("\u0ca3"))
NNA.place(x=420,y=530,width = 50,height = 50)

############################

TA = Button(root,text = "\u0ca4",font = ('',20),bg = 'white',command = lambda :Press("\u0ca4"))
TA.place(x=100,y=590,width = 50,height = 50)

THA = Button(root,text = "\u0ca5",font = ('',20),bg = 'white',command =lambda :Press("\u0ca5"))
THA.place(x=180,y=590,width = 50,height = 50)


DA = Button(root,text = "\u0ca6",font = ('',20),bg = 'white',command =lambda :Press("\u0ca6"))
DA.place(x=260,y=590,width = 50,height = 50)


DHA = Button(root,text = "\u0ca7",font = ('',20),bg = 'white',command = lambda :Press("\u0ca7"))
DHA.place(x=340,y=590,width = 50,height = 50)


NA = Button(root,text = "\u0ca8",font = ('',20),bg = 'white',command = lambda :Press("\u0ca8"))
NA.place(x=420,y=590,width = 50,height = 50)
############################

PA = Button(root,text = "\u0caa",font = ('',20),bg = 'white',command = lambda :Press("\u0caa"))
PA.place(x=100,y=650,width = 50,height = 50)

PHA = Button(root,text = "\u0cab",font = ('',20),bg = 'white',command =lambda :Press("\u0cab"))
PHA.place(x=180,y=650,width = 50,height = 50)


BA = Button(root,text = "\u0cac",font = ('',20),bg = 'white',command = lambda :Press("\u0cac"))
BA.place(x=260,y=650,width = 50,height = 50)


BHA = Button(root,text = "\u0cad",font = ('',20),bg = 'white',command = lambda :Press("\u0cad"))
BHA.place(x=340,y=650,width = 50,height = 50)


MA = Button(root,text = "\u0cae",font = ('',20),bg = 'white',command = lambda :Press("\u0cae"))
MA.place(x=420,y=650,width = 50,height = 50)
##################################################

YA = Button(root,text = "\u0caf",font = ('',20),bg = 'white',command = lambda :Press("\u0caf"))
YA.place(x=100,y=700,width = 50,height = 50)

RA = Button(root,text = "\u0cb0",font = ('',20),bg = 'white',command =lambda :Press("\u0cb0"))
RA.place(x=180,y=700,width = 50,height = 50)


LA = Button(root,text = "\u0cb2",font = ('',20),bg = 'white',command = lambda :Press("\u0cb2"))
LA.place(x=260,y=700,width = 50,height = 50)


VA = Button(root,text = "\u0cb5",font = ('',20),bg = 'white',command = lambda :Press("\u0cb5"))
VA.place(x=340,y=700,width = 50,height = 50)


SHE = Button(root,text = "\u0cb6",font = ('',20),bg = 'white',command = lambda :Press("\u0cb6"))
SHE.place(x=420,y=700,width = 50,height = 50)

SHA = Button(root,text = "\u0cb7",font = ('',20),bg = 'white',command = lambda :Press("\u0cb7"))
SHA.place(x=500,y=700,width = 50,height = 50)

SA = Button(root,text = "\u0cb8",font = ('',20),bg = 'white',command = lambda :Press("\u0cb8"))
SA.place(x=580,y=700,width = 50,height = 50)

HA = Button(root,text = "\u0cb9",font = ('',20),bg = 'white',command = lambda :Press("\u0cb9"))
HA.place(x=660,y=700,width = 50,height = 50)

LLA = Button(root,text = "\u0cb3",font = ('',20),bg = 'white',command = lambda :Press("\u0cb3"))
LLA.place(x=740,y=700,width = 50,height = 50)


#------------------------------------------------------------------------------

###########################

S1 = Button(root,text = "\u0c80",font = ('',20),bg = 'white',command = lambda :Press("\u0c80"))
S1.place(x=100+480,y=410,width = 50,height = 50)

S2 = Button(root,text = "\u0c81",font = ('',20),bg = 'white',command = lambda :Press("\u0c81"))
S2.place(x=180+480,y=410,width = 50,height = 50)


S3 = Button(root,text = "\u0c82",font = ('',20),bg = 'white',command = lambda :Press("\u0c82"))
S3.place(x=260+480,y=410,width = 50,height = 50)


S4 = Button(root,text = "\u0c83",font = ('',20),bg = 'white',command = lambda :Press("\u0c83"))
S4.place(x=340+480,y=410,width = 50,height = 50)


S5 = Button(root,text = "\u0cbc",font = ('',20),bg = 'white',command = lambda :Press("\u0cbc"))
S5.place(x=420+480,y=410,width = 50,height = 50)




S6 = Button(root,text = "\u0cbd",font = ('',20),bg = 'white',command = lambda :Press("\u0cbd"))
S6.place(x=100+480,y=470,width = 50,height = 50)

S7 = Button(root,text = "\u0cbe",font = ('',20),bg = 'white',command = lambda :Press("\u0cbe"))
S7.place(x=180+480,y=470,width = 50,height = 50)


S8 = Button(root,text = "\u0cbf",font = ('',20),bg = 'white',command = lambda :Press("\u0cbf"))
S8.place(x=260+480,y=470,width = 50,height = 50)


S9 = Button(root,text = "\u0cc0",font = ('',20),bg = 'white',command = lambda :Press("\u0cc0"))
S9.place(x=340+480,y=470,width = 50,height = 50)


S10 = Button(root,text = "\u0cc1",font = ('',20),bg = 'white',command = lambda :Press("\u0cc1"))
S10.place(x=420+480,y=470,width = 50,height = 50)



S11 = Button(root,text = "\u0cc2",font = ('',20),bg = 'white',command = lambda :Press("\u0cc2"))
S11.place(x=100+480,y=530,width = 50,height = 50)

S12 = Button(root,text = "\u0cc3",font = ('',20),bg = 'white',command = lambda :Press("\u0cc3"))
S12.place(x=180+480,y=530,width = 50,height = 50)


S13 = Button(root,text = "\u0cc4",font = ('',20),bg = 'white',command = lambda :Press("\u0cc4"))
S13.place(x=260+480,y=530,width = 50,height = 50)


S14 = Button(root,text = "\u0cc6",font = ('',20),bg = 'white',command = lambda :Press("\u0cc6"))
S14.place(x=340+480,y=530,width = 50,height = 50)


S15 = Button(root,text = "\u0cc7",font = ('',20),bg = 'white',command = lambda :Press("\u0cc7"))
S15.place(x=420+480,y=530,width = 50,height = 50)



S16 = Button(root,text = "\u0cc8",font = ('',20),bg = 'white',command = lambda :Press("\u0cc8"))
S16.place(x=100+480,y=590,width = 50,height = 50)

S17 = Button(root,text = "\u0cca",font = ('',20),bg = 'white',command =lambda :Press("\u0cca"))
S17.place(x=180+480,y=590,width = 50,height = 50)


S18 = Button(root,text = "\u0ccb",font = ('',20),bg = 'white',command =lambda :Press("\u0ccb"))
S18.place(x=260+480,y=590,width = 50,height = 50)


S19 = Button(root,text = "\u0ccc",font = ('',20),bg = 'white',command = lambda :Press("\u0ccc"))
S19.place(x=340+480,y=590,width = 50,height = 50)


S20 = Button(root,text = "\u0ccd",font = ('',20),bg = 'white',command = lambda :Press("\u0ccd"))
S20.place(x=420+480,y=590,width = 50,height = 50)

#---------------
S21 = Button(root,text = "\u0cd5",font = ('',20),bg = 'white',command = lambda :Press("\u0cd5"))
S21.place(x=980,y=410,width = 50,height = 50)

S22 = Button(root,text = "\u0cd6",font = ('',20),bg = 'white',command =lambda :Press("\u0cd6"))
S22.place(x=980,y=470,width = 50,height = 50)


S23 = Button(root,text = "\u0ce2",font = ('',20),bg = 'white',command =lambda :Press("\u0ce2"))
S23.place(x=980,y=530,width = 50,height = 50)


S24 = Button(root,text = "\u0ce3",font = ('',20),bg = 'white',command = lambda :Press("\u0ce3"))
S24.place(x=980,y=590,width = 50,height = 50)


S25 = Button(root,text = "\u0c8c",font = ('',20),bg = 'white',command = lambda :Press("\u0c8c"))
S25.place(x=1060,y=410,width = 50,height = 50)
#--
S26 = Button(root,text = "\u0cde",font = ('',20),bg = 'white',command =lambda :Press("\u0cde"))
S26.place(x=1060,y=470,width = 50,height = 50)


S27 = Button(root,text = "\u0ce0",font = ('',20),bg = 'white',command = lambda :Press("\u0ce0"))
S27.place(x=1060,y=530,width = 50,height = 50)


S28 = Button(root,text = "\u0c81",font = ('',20),bg = 'white',command = lambda :Press("\u0c81"))
S28.place(x=1060,y=590,width = 50,height = 50)


Enter = Button(root,text = "<-|",font = ('',20),bg = 'white',command = lambda :Press("\n"))
Enter.place(x=1140,y=450,width = 70,height = 70)

BackSpace= Button(root,text = "<--",font = ('',20),bg = 'white',command = BackSpace_Pressed)
BackSpace.place(x=1140,y=350,width = 50,height = 50)

#------------------------------------------------------------------------------
#Numbers

N0 = Button(root,text = "\u0ce6",font = ('',20),bg = 'white',command = lambda :Press("\u0ce6"))
N0.place(x=100+480,y=650,width = 50,height = 50)

N1 = Button(root,text = "\u0ce7",font = ('',20),bg = 'white',command = lambda :Press("\u0ce7"))
N1.place(x=180+480,y=650,width = 50,height = 50)


N2 = Button(root,text = "\u0ce8",font = ('',20),bg = 'white',command = lambda :Press("\u0ce8"))
N2.place(x=260+480,y=650,width = 50,height = 50)


N3 = Button(root,text = "\u0ce9",font = ('',20),bg = 'white',command = lambda :Press("\u0ce9"))
N3.place(x=340+480,y=650,width = 50,height = 50)


N4 = Button(root,text = "\u0cea",font = ('',20),bg = 'white',command = lambda :Press("\u0cea"))
N4.place(x=420+480,y=650,width = 50,height = 50)


N5 = Button(root,text = "\u0ceb",font = ('',20),bg = 'white',command = lambda :Press("\u0ceb"))
N5.place(x=500+480,y=650,width = 50,height = 50)

N6 = Button(root,text = "\u0cec",font = ('',20),bg = 'white',command = lambda :Press("\u0cec"))
N6.place(x=580+480,y=650,width = 50,height = 50)


N7 = Button(root,text = "\u0ced",font = ('',20),bg = 'white',command = lambda :Press("\u0ced"))
N7.place(x=660+480,y=650,width = 50,height = 50)


N8 = Button(root,text = "\u0cee",font = ('',20),bg = 'white',command = lambda :Press("\u0cee"))
N8.place(x=740+480,y=650,width = 50,height = 50)


N9 = Button(root,text = "\u0cef",font = ('',20),bg = 'white',command = lambda :Press("\u0cef"))
N9.place(x=820+480,y=650,width = 50,height = 50)

#-------------------------------------------------------------------------------
root.mainloop()
