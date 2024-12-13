from tkinter import*
root = Tk()
root.geometry("400x300")
root.title("main")

def topwin():
    t= Toplevel()
    t.geometry("180x100")
    t.title("toplevel")

    l2 = Label(t, text = "This is toplevel1 window")
    l2.pack()
    t.mainloop()

l = Label(root, text = "This Is root Window")
btn = Button(root, text = "click Here to open Another Window", command = topwin) 
l.pack()
btn.pack()   

