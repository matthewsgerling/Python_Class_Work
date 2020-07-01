import tkinter


def pick_cis():
    label.config(text="Nice choice")


def pick_bis():
    label.config(text="Are you sure?")


m = tkinter.Tk()
m.title('Favorite Meal')
label = tkinter.Label(m, text="Waiting")
label.grid(row=4)
var1 = tkinter.IntVar()
check = tkinter.Checkbutton(m, text="Breakfast", variable=var1, command=pick_cis).grid(row=0)
var2 = tkinter.IntVar()
check2 = tkinter.Checkbutton(m, text="Second Breakfast", variable=var2, command=pick_bis).grid(row=1)
var3 = tkinter.IntVar()
check3 = tkinter.Checkbutton(m, text="Lunch", variable=var3, command=pick_bis).grid(row=2)
var4 = tkinter.IntVar()
check4 = tkinter.Checkbutton(m, text="Dinner", variable=var4, command=pick_bis).grid(row=3)
exit_button = tkinter.Button(m, text='Exit', width=25, command=m.destroy)
exit_button.grid(row=5)
m.mainloop()
