from tkinter import *

def mils_to_km():
    miles_ = float(input.get())
    km_ = round(miles_ * 1.609)
    km_result.config(text=f"{km_}")

window = Tk()
window.title("Mile to Km Converter")
window.config(padx=20,pady=20)

input = Entry(width=10)
input.grid(column=1,row=0)

miles = Label(text="Miles")
miles.grid(column=2,row= 0)


is_equal_to = Label(text="is equal to")
is_equal_to.grid(column=0,row=1)


km = Label(text="Km")
km.grid(column=2, row= 1)

button = Button(text="Calculate", command=mils_to_km)
button.grid(column=1,row=2)


km_result = Label(text="0")
km_result.grid(column=1,row=1)










window.mainloop()