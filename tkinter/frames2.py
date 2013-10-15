from Tkinter import *


root = Tk()
root.title('Frames')

of = [None]*5
for bdw in range(5):
    of[bdw] = Frame(root, borderwidth=0)
    Label(of[bdw], text='borderwidth = %d ' % bdw).pack(side=LEFT)
    ifx = 0
    iff = []
    for relief in [RAISED, SUNKEN, FLAT, RIDGE, GROOVE, SOLID]:
        iff.append(Frame(of[bdw], borderwidth=bdw, relief=relief))
        Label(iff[ifx], text=relief, width=10).pack(side=LEFT)
        iff[ifx].pack(side=LEFT, padx=7-bdw, pady=5+bdw)
        ifx = ifx+1
    of[bdw].pack()

root.mainloop()
