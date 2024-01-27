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
output_label = Label(root, text="Result", font=font)
output_text = Entry(root, width=20, font=font)
output_label.grid(row=2, column=0, sticky=W)
output_text.grid(row=2, column=1)

#button widget
convertBtn = Button(root, text="Convert", font=font, width=10, bg=color)
resetBtn = Button(root, text="Clear", font=font, width=7, bg=color)
convertBtn.grid(row=3, column=1, sticky=W, padx=5, pady=5)
resetBtn.grid(row=3, column=1, sticky=E, padx=5, pady=5)

root.mainloop()
