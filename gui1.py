import tkinter
import turtle
import sys
import os

def main():
    root = tkinter.Tk()
    cv = tkinter.Canvas(root, width= 500, height = 600)
    cv.pack(side = tkinter.LEFT)
    root.title("Draw!")

    t = turtle.RawTurtle(cv)

    screen = t.getscreen()

    screen.setworldcoordinates(0,0,600,600)

    frame = tkinter.Frame(root)
    frame.pack(side = tkinter.RIGHT, fill = tkinter.BOTH)

    screen.tracer(0)

    
    def quitHandler():
        print("goodbye")
        #sys.exit("hh")
        os._exit(1)

    quitButton = tkinter.Button(frame, text="Quit", command = quitHandler)
    quitButton.pack()

    textLab = tkinter.Label(frame, text="Text Here")
    textLab.pack()
    
    textVar = tkinter.StringVar()
    textVar.set("Hello World")
    textEntry = tkinter.Entry(frame, textvariable = textVar)
    textEntry.pack()

    def writeHandler():
        t.write(textVar.get())

    writeButton = tkinter.Button(frame, text="Write Text", command = writeHandler)
    writeButton.pack()    
        
    def clickHandler(x,y):
        t.goto(x,y)
        screen.update()

    screen.onclick(clickHandler)        
        
    def dragHandler(x,y):
        t.goto(x,y)
        screen.update()

    t.ondrag(dragHandler)
    



    tkinter.mainloop()

if __name__ == "__main__":
    main()
