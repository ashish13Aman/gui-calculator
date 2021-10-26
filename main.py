import pyttsx3
from tkinter import *
import tkinter.messagebox as tmsg
from PIL import ImageTk,Image


s_root=Tk()
s_root.title("calculator")
s_root.geometry("300x200")
my_img=ImageTk.PhotoImage(Image.open("splash.jpg"))
my_label=Label(image=my_img)
my_label.pack()

def main_window():
    s_root.destroy()
    root = Tk()
    root.geometry("900x800")
    root.minsize(900, 800)
    root.maxsize(900, 800)
    root.title("GUI speech Calculator")
    root.wm_iconbitmap("1.ico")

    engine = pyttsx3.init()
    engine.setProperty("rate", 190)
    engine.say("initialising G u i speech calculator ")
    engine.runAndWait()
    engine.stop()
    global scvalue


    def click(event):
       
        text = event.widget.cget("text")
        print(text)

        if text == "C":
            scvalue.set("")
            screen.update()
        elif text == "=":
            if scvalue.get().isdigit():
                value = int(scvalue.get())
            else:
                try:
                    value = eval(screen.get())

                except Exception as e:
                    value = ""
                    tmsg.showinfo("Warning", "ERROR")

            scvalue.set(value)
            screen.update()
            engine.setProperty("rate", 200)

            engine.say(value)
            engine.runAndWait()
            engine.stop()

        else:
            scvalue.set(scvalue.get() + text)
            screen.update()


    frame_parent = Frame(root, bg="#20B2AA", width=900, height=900, relief=SUNKEN, borderwidth=10)
    frame_parent.pack(fill=BOTH)

    scvalue = StringVar()
    scvalue.set("")
    screen = Entry(frame_parent, textvar=scvalue, bg="#FAF9F6", font="arial 50 bold", relief=SUNKEN, borderwidth=10)
    screen.pack(fill=X, ipadx=10, pady=20, padx=20)

    frame1 = Frame(frame_parent, bg="#00CED1")
    button = Button(frame1, text="9", font="arial 40 bold", bg="grey", relief=RAISED, borderwidth=8)
    button.pack(side=LEFT, expand=TRUE, fill=BOTH, pady=20, padx=20)
    button.bind("<Button-1>", click)
    button = Button(frame1, text="8", font="arial 40 bold", bg="grey", relief=RAISED, borderwidth=8)
    button.pack(side=LEFT, expand=TRUE, fill=BOTH, pady=20, padx=20)
    button.bind("<Button-1>", click)
    button = Button(frame1, text="7", font="arial 40 bold", bg="grey", relief=RAISED, borderwidth=8)
    button.pack(side=LEFT, expand=TRUE, fill=BOTH, pady=20, padx=20)
    button.bind("<Button-1>", click)
    button = Button(frame1, text="+", font="arial 40 bold", bg="yellow", relief=GROOVE, borderwidth=8)
    button.pack(side=LEFT, expand=TRUE, fill=BOTH, pady=20, padx=20)
    button.bind("<Button-1>", click)
    frame1.pack(fill=BOTH)

    frame1 = Frame(frame_parent, bg="#00CED1")
    button = Button(frame1, text="6", font="arial 40 bold", bg="grey", relief=RAISED, borderwidth=8)
    button.pack(side=LEFT, expand=TRUE, fill=BOTH, pady=20, padx=20)
    button.bind("<Button-1>", click)
    button = Button(frame1, text="5", font="arial 40 bold", bg="grey", relief=RAISED, borderwidth=8)
    button.pack(side=LEFT, expand=TRUE, fill=BOTH, pady=20, padx=20)
    button.bind("<Button-1>", click)
    button = Button(frame1, text="4", font="arial 40 bold", bg="grey", relief=RAISED, borderwidth=8)
    button.pack(side=LEFT, expand=TRUE, fill=BOTH, pady=20, padx=20)
    button.bind("<Button-1>", click)
    button = Button(frame1, text="-", font="arial 40 bold", bg="yellow", relief=GROOVE, borderwidth=8)
    button.pack(side=LEFT, expand=TRUE, fill=BOTH, pady=20, padx=20)
    button.bind("<Button-1>", click)
    frame1.pack(fill=BOTH)

    frame1 = Frame(frame_parent, bg="#00CED1")
    button = Button(frame1, text="3", font="arial 40 bold", bg="grey", relief=RAISED, borderwidth=8)
    button.pack(side=LEFT, expand=TRUE, fill=BOTH, pady=20, padx=20)
    button.bind("<Button-1>", click)
    button = Button(frame1, text="2", font="arial 40 bold", bg="grey", relief=RAISED, borderwidth=8)
    button.pack(side=LEFT, expand=TRUE, fill=BOTH, pady=20, padx=20)
    button.bind("<Button-1>", click)
    button = Button(frame1, text="1", font="arial 40 bold", bg="grey", relief=RAISED, borderwidth=8)
    button.pack(side=LEFT, expand=TRUE, fill=BOTH, pady=20, padx=20)
    button.bind("<Button-1>", click)
    button = Button(frame1, text="*", font="arial 40 bold", bg="yellow", relief=GROOVE, borderwidth=8)
    button.pack(side=LEFT, expand=TRUE, fill=BOTH, pady=20, padx=20)
    button.bind("<Button-1>", click)
    frame1.pack(fill=BOTH)

    frame2 = Frame(frame_parent, bg="#00CED1")
    button = Button(frame2, text="C", font="arial 40 bold", bg="red", relief=GROOVE, borderwidth=8)
    button.pack(side=LEFT, expand=TRUE, fill=BOTH, pady=20, padx=20)
    button.bind("<Button-1>", click)
    button = Button(frame2, text="0", font="arial 40 bold", bg="grey", relief=RAISED, borderwidth=8)
    button.pack(side=LEFT, expand=TRUE, fill=BOTH, pady=20, padx=20)
    button.bind("<Button-1>", click)
    button = Button(frame2, text="=", font="arial 40 bold", bg="red", relief=GROOVE, borderwidth=8)
    button.pack(side=LEFT, expand=TRUE, fill=BOTH, pady=20, padx=20)
    button.bind("<Button-1>", click)
    button = Button(frame2, text="/", font="arial 40 bold", bg="yellow", relief=GROOVE, borderwidth=8)
    button.pack(side=LEFT, expand=TRUE, fill=BOTH, pady=20, padx=20)
    button.bind("<Button-1>", click)
    frame2.pack(fill=BOTH)

s_root.after(1000,main_window)

mainloop()
