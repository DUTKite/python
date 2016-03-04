import Tkinter as tk
window=tk.Tk()
def sliderupdata(something):
    red=redslider.get()
    green=greenslider.get()
    blue=blueslider.get()

    colour="#%02x%02x%02x" % (red,green,blue)
    canvas.config(bg=colour)
    colourget.delete(0,tk.END)
    colourget.insert(0,colour)

redslider=tk.Scale(window,from_=0,to=255,command=sliderupdata)
greenslider=tk.Scale(window,from_=0,to=255,command=sliderupdata)
blueslider=tk.Scale(window,from_=0,to=255,command=sliderupdata)
canvas=tk.Canvas(window,width=200,height=200)
redlabel=tk.Label(window,text="R")
greenlabel=tk.Label(window,text="G")
bluelabel=tk.Label(window,text="B")
colourlabel=tk.Label(window,text="RGB:")
colourget=tk.Entry(window)

titlelabel=tk.Label(window,text="Colour Creater")
titlelabel.grid(row=1,column=1,columnspan=3)

redlabel.grid(row=2,column=1)
greenlabel.grid(row=2,column=2)
bluelabel.grid(row=2,column=3)

redslider.grid(row=3,column=1)
greenslider.grid(row=3,column=2)
blueslider.grid(row=3,column=3)
canvas.grid(row=4,column=1,columnspan=3)
colourlabel.grid(row=5,column=1)
colourget.grid(row=5,column=2,columnspan=2)

window.mainloop()






        
              
