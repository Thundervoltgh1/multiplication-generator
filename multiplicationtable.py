from tkinter import*
from tkinter.ttk import*
new=Tk()
new.title("MULTIPILCATION TABLE GENERATOR")
title=Label(new,text="Multiplication table")
title.grid(row=0,column=3,columnspan=3,pady=25)
h=Label(new,text="number and range")
h.grid(row=2,column=0,padx=10)
l=IntVar
u=Combobox(new,textvariable=l,width=5)
u["values"]=tuple(range(101))
u.grid(row=2,column=1)
n=IntVar
g=Radiobutton(new,text="10",variable=n,value=10)
g1=Radiobutton(new,text="20",variable=n,value=20)
g2=Radiobutton(new,text="30",variable=n,value=30)
g.grid(row=2,column=3)
g1.grid(row=3,column=3)
g2.grid(row=4,column=3)
button=Button(new,text="Generate",command="")
button.grid(row=5,column=2)
c=Label(new,anchor="center")
c.grid(row=6,column=1,pady=25)
new.mainloop()