from tkinter import *
import tkinter.messagebox as tmsg
root=Tk()
root.geometry("900x750") 
root.configure(bg="cyan")
root.minsize(900,750)
root.maxsize(900,750)
root.title("GUI Calculator")
root.wm_iconbitmap("1.ico")
def click(event):
    global scvalue
    text=event.widget.cget("text")
    print (text)

    if text =="C":
       scvalue.set("")
       screen.update()
    elif text =="=":
        if scvalue.get().isdigit():
            value=int(scvalue.get())
        else:
            try:
                value=eval(screen.get())
            except Exception as e:
                value=""
                tmsg.showinfo("Warning","ERROR")

        scvalue.set(value)
        screen.update()
    else:
        scvalue.set(scvalue.get()+text)
        screen.update()


scvalue=StringVar()
scvalue.set("")
screen=Entry(root,textvar=scvalue,font="arial 50 bold")
screen.pack(fill=X,ipadx=10,pady=20,padx=20)


frame1=Frame(root,bg="cyan")
button=Button(frame1,text="9",font="arial 40 bold", bg= "grey")
button.pack(side=LEFT,expand= TRUE, fill=BOTH, pady=20, padx=20 )
button.bind("<Button-1>",click)
button=Button(frame1,text="8",font="arial 40 bold", bg= "grey")
button.pack(side=LEFT,expand= TRUE, fill=BOTH, pady=20, padx=20 )
button.bind("<Button-1>",click)
button=Button(frame1,text="7",font="arial 40 bold", bg= "grey")
button.pack(side=LEFT,expand= TRUE, fill=BOTH,pady=20, padx=20 )
button.bind("<Button-1>",click)
button=Button(frame1,text="+",font="arial 40 bold", bg="yellow")
button.pack(side=LEFT,expand= TRUE, fill=BOTH, pady=20, padx=20 )
button.bind("<Button-1>",click)
frame1.pack(fill=BOTH)

frame1=Frame(root,bg="cyan")
button=Button(frame1,text="6",font="arial 40 bold", bg= "grey")
button.pack(side=LEFT,expand= TRUE, fill=BOTH, pady=20, padx=20 )
button.bind("<Button-1>",click)
button=Button(frame1,text="5",font="arial 40 bold", bg= "grey")
button.pack(side=LEFT,expand= TRUE, fill=BOTH, pady=20, padx=20 )
button.bind("<Button-1>",click)
button=Button(frame1,text="4",font="arial 40 bold", bg= "grey")
button.pack(side=LEFT,expand= TRUE, fill=BOTH, pady=20, padx=20 )
button.bind("<Button-1>",click)
button=Button(frame1,text="-",font="arial 40 bold",bg="yellow")
button.pack(side=LEFT,expand= TRUE, fill=BOTH, pady=20, padx=20 )
button.bind("<Button-1>",click)
frame1.pack(fill=BOTH)

frame1=Frame(root,bg="cyan")
button=Button(frame1,text="3",font="arial 40 bold", bg= "grey")
button.pack(side=LEFT,expand= TRUE, fill=BOTH, pady=20, padx=20 )
button.bind("<Button-1>",click)
button=Button(frame1,text="2",font="arial 40 bold", bg= "grey")
button.pack(side=LEFT,expand= TRUE, fill=BOTH, pady=20, padx=20 )
button.bind("<Button-1>",click)
button=Button(frame1,text="1",font="arial 40 bold", bg= "grey")
button.pack(side=LEFT,expand= TRUE, fill=BOTH, pady=20, padx=20 )
button.bind("<Button-1>",click)
button=Button(frame1,text="*",font="arial 40 bold", bg="yellow")
button.pack(side=LEFT,expand= TRUE, fill=BOTH, pady=20, padx=20 )
button.bind("<Button-1>",click)
frame1.pack(fill=BOTH)

frame2=Frame(root,bg="cyan")
button=Button(frame2,text="C",font="arial 40 bold", bg="red")
button.pack(side=LEFT,expand= TRUE, fill=BOTH, pady=20, padx=20 )
button.bind("<Button-1>",click)
button=Button(frame2,text="0",font="arial 40 bold", bg= "grey")
button.pack(side=LEFT,expand= TRUE, fill=BOTH, pady=20, padx=20 )
button.bind("<Button-1>",click)
button=Button(frame2,text="=",font="arial 40 bold", bg= "red")
button.pack(side=LEFT,expand= TRUE, fill=BOTH, pady=20, padx=20 )
button.bind("<Button-1>",click)
button=Button(frame2,text="/",font="arial 40 bold", bg="yellow")
button.pack(side=LEFT,expand= TRUE, fill=BOTH, pady=20, padx=20 )
button.bind("<Button-1>",click)
frame2.pack(fill=BOTH)

root.mainloop()
