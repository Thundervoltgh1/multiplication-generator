from tkinter import*
from tkinter.ttk import*
new=Tk()
new.title("MULTIPILCATION TABLE GENERATOR")
title=Label(new,text="Multiplication table")
title.grid(row=0,column=3,columnspan=3,pady=25)
h=Label(new,text="number and range")
h.grid(row=2,column=0,padx=10)
z=IntVar()
u=Combobox(new,textvariable=z,width=5)
u["values"]=tuple(range(101))
u.grid(row=2,column=1)
endVal=IntVar()
g=Radiobutton(new,text="10",variable=endVal,value=10)
g1=Radiobutton(new,text="20",variable=endVal,value=20)
g2=Radiobutton(new,text="30",variable=endVal,value=30)
g.grid(row=2,column=3)
g1.grid(row=3,column=3)
g2.grid(row=4,column=3)
def generate():
    Tables=""
    for i in range(endVal.get()+1):
        Tables+=str(z.get())+"x"+str(i)+"="+str(z.get()*i)+"\n"
    c.configure(text=Tables)

button=Button(new,text="Generate",command=generate)
button.grid(row=5,column=2)
c=Label(new,anchor="center")
c.grid(row=6,column=1,pady=25)

new.mainloop()
