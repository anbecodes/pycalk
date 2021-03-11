from tkinter import *

graphic = Tk()
graphic.title("Calculator")

display = Entry(graphic)
display.grid(row=1, columnspan=6, sticky=W+E)

# number buttons
Button(graphic, text=1,).grid(row=2, column=0)
Button(graphic, text=2,).grid(row=2, column=1)
Button(graphic, text=3,).grid(row=2, column=2)
Button(graphic, text=4,).grid(row=3, column=0)
Button(graphic, text=5,).grid(row=3, column=1)
Button(graphic, text=6,).grid(row=3, column=2)
Button(graphic, text=7,).grid(row=4, column=0)
Button(graphic, text=8,).grid(row=4, column=1)
Button(graphic, text=9,).grid(row=4, column=2)
Button(graphic, text=0,).grid(row=5, column=0)

graphic.mainloop()