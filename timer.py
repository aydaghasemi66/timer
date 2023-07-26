from tkinter import *
from tkinter import messagebox
win=Tk()
win.geometry('500x250')
win.resizable(0,0)
win.config(bg="#FFE4C4")


#functions======================================
time = 0
timee=StringVar()
def countdown():
    global time
    if time>0:
        time-=1
        b1.config(state=DISABLED)
        b2.config(state=DISABLED) 
        l2.config(text=time)
        if time==0:
            messagebox.showinfo("شمارش معکوس","زمان به پایان رسید")
            b1.config(state=NORMAL)
            b2.config(state=NORMAL)
            e1.delete(0,END)
            l2.config(text=" ")
        l2.after(1000,countdown)
   
def reset():
    global time
    time=0  
    e1.delete(0,END)
    l2.config(text=" ")
    b1.config(state=NORMAL)
    b2.config(state=NORMAL)

    
           
def set():
    global time
    time += int(e1.get())
    return time
    
    
#buttons===============================================
b1=Button(win,text="شروع", bg='#C3B091' ,font='Tahoma 20',command=countdown)
b1.place(x=50,y=170)

b2=Button(win,text="تنظیم زمان", bg='#C3B091' ,font='Tahoma 20',command=set)
b2.place(x=150,y=170)

b3=Button(win,text="تنظیم مجدد", bg='#C3B091' ,font='Tahoma 20',command=reset)
b3.place(x=300,y=170)
#labels=================================================
lbl1=Label(win,text="زمان را بر حسب ثانیه وارد کنید",font='tahoma 14',bg="#FFE4C4")
lbl1.place(x=10,y=110)
l2=Label(win,text=" ",font="Tahoma 45")
l2.place(x=200,y=20)


#Entry==================================================
e1=Entry(win,textvariable=timee,relief=SOLID)
e1.place(x=290,y=115)



win.mainloop()

