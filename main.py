from tkinter import*
root=Tk()
root.geometry("600x750")
root.minsize(600,750)
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
            value=eval(screen.get())
            scvalue.set(value)
            screen.update()
    else:
        scvalue.set(scvalue.get()+text)
        screen.update()


scvalue=StringVar()
scvalue.set("")
screen=Entry(root,textvar=scvalue,font="arial 40 bold")
screen.pack(fill=X,ipadx=10,pady=10,padx=10)


frame1=Frame(root,bg="grey")
button=Button(frame1,text="7",font="arial 40 bold")
button.pack(side=LEFT,pady=10,padx=10)
button.bind("<Button-1>",click)
button=Button(frame1,text="8",font="arial 40 bold")
button.pack(side=LEFT,pady=10,padx=10)
button.bind("<Button-1>",click)
button=Button(frame1,text="9",font="arial 40 bold")
button.pack(side=LEFT,pady=10,padx=10)
button.bind("<Button-1>",click)
frame1.pack()

frame1=Frame(root,bg="grey")
button=Button(frame1,text="4",font="arial 40 bold")
button.pack(side=LEFT,pady=10,padx=10)
button.bind("<Button-1>",click)
button=Button(frame1,text="5",font="arial 40 bold")
button.pack(side=LEFT,pady=10,padx=10)
button.bind("<Button-1>",click)
button=Button(frame1,text="6",font="arial 40 bold")
button.pack(side=LEFT,pady=10,padx=10)
button.bind("<Button-1>",click)
frame1.pack()

frame1=Frame(root,bg="grey")
button=Button(frame1,text="1",font="arial 40 bold")
button.pack(side=LEFT,pady=10,padx=10)
button.bind("<Button-1>",click)
button=Button(frame1,text="2",font="arial 40 bold")
button.pack(side=LEFT,pady=10,padx=10)
button.bind("<Button-1>",click)
button=Button(frame1,text="3",font="arial 40 bold")
button.pack(side=LEFT,pady=10,padx=10)
button.bind("<Button-1>",click)
frame1.pack()

frame1_5=Frame(root,bg="grey")
button=Button(frame1_5,text="0",font="arial 40 bold")
button.pack(side=BOTTOM,pady=10,padx=10)
button.bind("<Button-1>",click)
frame1_5.pack()

##operators
frame2=Frame(root,bg="grey")
button=Button(frame2,text="/",font="arial 40 bold")
button.pack(side=LEFT,pady=10,padx=10)
button.bind("<Button-1>",click)
button=Button(frame2,text="*",font="arial 40 bold")
button.pack(side=LEFT,pady=10,padx=10)
button.bind("<Button-1>",click)
button=Button(frame2,text="-",font="arial 40 bold")
button.pack(side=LEFT,pady=10,padx=10)
button.bind("<Button-1>",click)
button=Button(frame2,text="+",font="arial 40 bold")
button.pack(side=LEFT,pady=10,padx=10)
button.bind("<Button-1>",click)
button=Button(frame2,text="C",font="arial 40 bold")
button.pack(side=LEFT,pady=10,padx=10)
button.bind("<Button-1>",click)
button=Button(frame2,text="=",font="arial 40 bold")
button.pack(side=LEFT,pady=10,padx=10)
button.bind("<Button-1>",click)
frame2.pack()

root.mainloop()
