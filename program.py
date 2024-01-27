from tkinter import *
from tkinter import ttk

root=Tk()
root.title("Program temperature converter")
root.iconbitmap("icon/tempicon.ico")
root.resizable(0, 0)

#settings
font = ("Arial", 15, "bold")
color = "orange"

#input widget
input_label = Label(root, text="Temperature(C)", font=font)
input_txt = Entry(root, width=20, font=font)
input_label.grid(row=0, column=0, sticky=W) # sticky is directional position.
input_txt.grid(row=0, column=1)

#combobox widget
unit_label = Label(root, text="Convert to unit", font=font)
unit_list = ["Fahrenheit", "Kelvin"]
temp_combo = ttk.Combobox(root, value=unit_list, font=font, width=18)
temp_combo.set("Kelvin") # Set default value.

unit_label.grid(row=1, column=0, sticky=W)
temp_combo.grid(row=1, column=1)
#output widget

#button widget

root.mainloop()
