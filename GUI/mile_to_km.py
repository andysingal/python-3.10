from tkinter import *
def miles_to_km():
    miles = float(miles_input.get())
    km = miles * 1.609
    kilometer_result_label.config(text=f"{km}")

window = Tk()
window.title("Miles to KM converter")
window.config(padx=20,pady=20)

miles_input = Entry(width=10)
miles_input.grid(column=1,row=0)


miles_label = Label(text="Miles")
miles_label.grid(column=2, row =0)

is_equal_label = Label(text="is equal to")
is_equal_label.grid(column=0, row=1)

kilometer_result_label = Label(text="0")
kilometer_result_label.grid(column=1,row=1)

kilometer_label = Label(text="Km")
kilometer_label.grid(column=2,row=1)

calculate_button = Button(text="Calculate", command=miles_to_km)
calculate_button.grid(column=1, row=2)


window.mainloop()

# #Button
# def button_clicked():
#     print("I got clicked")
#     new_text = input.get()
#     my_label.config (text=new_text)
#
# window = Tk()
# window.title("My first gui program")
# window.minsize(width=500,height=300)
# window.config(padx=20,pady=20)
#
# #label
# my_label = Label(text="I am a Label",font=("Arial",24,"bold"))
# my_label.config(text="New Text")
# my_label.grid(column=0,row=0)
# my_label.config(padx=50, pady=50)
#
# #Button
# button = Button(text="Click Me",command=button_clicked)
# button.grid(column=1, row=1)
#
# new_button = Button(text="New Button")
# new_button.grid(column=2, row=0)
#
# #Entry comment
# input = Entry(width=10)
# print(input.get())
# input.grid(column=3, row=2)




#Text





