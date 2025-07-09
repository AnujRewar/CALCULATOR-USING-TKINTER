#making caluculator using tkinter
from tkinter import *
window=Tk()

#size and shape
window.title("Calculator")
window.geometry("500x500")
window.config(bg="white")

e1=Entry(window,width="100",bg="grey")
e1.place(x=0,y=0)

def click(num):
    result=e1.get()
    e1.delete(0 ,END)
    e1.insert(0,str(result)+str(num))

button1=Button(window,text="1",width="8",height="2",command=lambda:click(1))
button1.place(x=30,y=60)

button2=Button(window,text="2",width="8",height="2",command=lambda:click(2))
button2.place(x=90,y=60)

button3=Button(window,text="3",width="8",height="2",command=lambda:click(3))
button3.place(x=150,y=60)

button4=Button(window,text="4",width="8",height="2",command=lambda:click(4))
button4.place(x=30,y=110)

button5=Button(window,text="5",width="8",height="2",command=lambda:click(5))
button5.place(x=90,y=110)

button6=Button(window,text="6",width="8",height="2",command=lambda:click(6))
button6.place(x=150,y=110)

button7=Button(window,text="7",width="8",height="2",command=lambda:click(7))
button7.place(x=30,y=160)

button8=Button(window,text="8",width="8",height="2",command=lambda:click(8))
button8.place(x=90,y=160)

button9=Button(window,text="9",width="8",height="2",command=lambda:click(9))
button9.place(x=150,y=160)

button10=Button(window,text="0",width="8",height="2",command=lambda:click(0))
button10.place(x=30,y=210)

def add():
    n1=e1.get()
    global math 
    math="addition"
    global i
    i=int(n1)
    e1.delete(0,END)
button11=Button(window,text="+",width="8",height="2",command=add)
button11.place(x=90,y=210)


def sub():
    n1=e1.get()
    global math
    math="subtraction"
    global i
    i=int(n1)
    e1.delete(0,END)

button12=Button(window,text="-",width="8",height="2",command=sub)
button12.place(x=150,y=210)


def mul():
    n1=e1.get()
    global math
    math="multiplication"
    global i
    i=int(n1)
    e1.delete(0,END)

button13=Button(window,text="*",width="8",height="2",command=mul)
button13.place(x=30,y=260)


def dev():
    n1=e1.get()
    global math
    math='division'
    global i
    i=int(n1)
    e1.delete(0,END)

button14=Button(window,text="/",width="8",height="2",command=dev)
button14.place(x=90,y=260)


def equal():
   n2=e1.get()
   e1.delete(0,END)
   try:
       
      if math =="addition":
        e1.insert(0,i+int(n2))
      elif math =="subtraction":
        e1.insert(0,i-int(n2))
      elif math =="multiplication":
        e1.insert(0,i*int(n2))
      elif math=="division":
        e1.insert(0,i/int(n2))
      else:
        e1.insert(0,"invalid")
   except ZeroDivisionError:
      e1.insert(0,"Error") 
     
button15=Button(window,text="=",width="8",height="2",command=equal)
button15.place(x=150,y=260)


def clear():
    e1.delete(0,END)

button16=Button(window,text="clear",width="8",height="2",command=clear)
button16.place(x=30,y=310)

mainloop()