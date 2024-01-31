
from  tkinter import *
root = Tk()


root.title("calculater")
root .geometry("800x800+400+400")
root.resizable(True,False)
# root.minsize("200", "200")
# root.maxsize("200", "200")

def kg():

    var1=1000*int(ent1.get())
    lbl1_2.config(text=var1)

def meter():

    var2=100*int(ent2.get())
    lbl2_2.config(text=var2)




lbl1 = Label(root, text="KG",bg="gray")
lbl1.grid(row=0,column=0,padx=5,pady=5)

ent1 = Entry(root)
ent1.grid(row=0,column=1)

lbl1_1 = Label(root, text="to grm",bg="gray")
lbl1_1.grid(row=0,column=2,padx=5,pady=5)

lbl1 = Label(root)
lbl1.grid(row=0,column=3,padx=5,pady=5)

lbl1_2 = Label(root)
lbl1_2.grid(row=0,column=4,padx=5,pady=5)

btn1 = Button(root,text="kg => grm ",bg="red",command=kg)
btn1.grid(row=2,column=5)




lbl2 = Label(root, text="meter",bg="gray")
lbl2.grid(row=1,column=0,padx=5,pady=5)

ent2 = Entry(root)
ent2.grid(row=1,column=1)

lbl2_1 = Label(root, text="to cm",bg="gray")
lbl2_1.grid(row=1,column=2,padx=5,pady=5)

btn2 = Button(root,text="meter => cm ",bg="red",command=meter)
btn2.grid(row=2,column=6)

lbl2_2 = Label(root)
lbl2_2.grid(row=1,column=4,padx=5,pady=5)


############################################################step two

lblexit=Label(root,text="enter your first number",bg="yellow")
lblexit.grid(row=4,column=0,padx=5)

entexit = Entry(root)
entexit.grid(row=4,column=1)



lblexit2=Label(root,text="enter your second number",bg="yellow")
lblexit2.grid(row=5,column=0,padx=5)

entexit2 = Entry(root)
entexit2.grid(row=5,column=1)


lblexit55=Label(root,fg="red")
lblexit55.grid(row=8,column=3,padx=5)

#########################################

def zarb():

    var3=int(entexit.get())
    var4=int(entexit2.get())
    var22=0
    var22 =var3*var4

    lblexit55.config(text=var22)

def taghsim():

    var3=int(entexit.get())
    var4=int(entexit2.get())
    var22=0
    var22 =var3/var4

    lblexit55.config(text=var22)

def jam():

    var3=int(entexit.get())
    var4=int(entexit2.get())
    var22=0
    var22 =var3+var4

    lblexit55.config(text=var22)

def menha():

    var3=int(entexit.get())
    var4=int(entexit2.get())
    var22=0
    var22 =var3-var4

    lblexit55.config(text=var22)

btn_zarb=Button(root,text="*",bg="yellow",fg="blue",command=zarb)
btn_zarb.grid(row=7,column=0,padx=5,pady=5,rowspan=1,columnspan=1,sticky=W+S+N+E)

btn_taghsim=Button(root,text="/",bg="yellow",fg="blue",command=taghsim)
btn_taghsim.grid(row=7,column=1,padx=5,pady=5,rowspan=1,columnspan=1,sticky=W+S+N+E)

btn_jam=Button(root,text="+",bg="yellow",fg="blue",command=jam)
btn_jam.grid(row=7,column=2,padx=5,pady=5,rowspan=1,columnspan=1,sticky=W+S+N+E)

btn_menha=Button(root,text="-",bg="yellow",fg="blue",command=menha)
btn_menha.grid(row=7,column=3,padx=5,pady=5,rowspan=1,columnspan=1,sticky=W+S+N+E)






root.mainloop()