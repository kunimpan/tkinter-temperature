from tkinter import *

root=Tk()
root.title("Program temperature converter")
root.iconbitmap("icon/tempicon.ico")
root.resizable(0, 0)

#settings
font = ("Arial", 15, "bold")
color = "orange"

#input widget
input_label = Label(root, text="temperature(C)", font=font)
input_txt = Entry(root, width=20, font=font)
input_label.grid(row=0, column=0, sticky=S) # sticky is directional position
input_txt.grid(row=0, column=1)

#combobox widget

#output widget

#button widget

root.mainloop()
