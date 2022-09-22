import tkinter as tk

cal = ""

def add_cal(symbol):
    global cal
    cal += str(symbol)
    text_result.delete(1.0, "end")
    text_result.insert(1.0, cal)
def evalute_cal():
    global cal
    try:
        cal = str(eval(cal))
        text_result.delete(1.0, "end")
        text_result.insert(1.0, cal)

    except:
        clear_field()
        text_result.insert(1.0, "error")


def clear_field():
    global cal
    cal = ""
    text_result.delete(1.0, 'end')

root = tk.Tk()
root.geometry('425x400')
root.title("Cal")
text_result = tk.Text(root, height=3, width=28, font =("Consolas", 20 ))
text_result.grid(columnspan=5)
#buttons for numbers below
but_1 = tk.Button(root, text ='1', command=lambda: add_cal(1), width =5, font = ("Consolas", 20 ))
but_1.grid(row = 2, column=1)
but_2 = tk.Button(root, text ='2', command=lambda: add_cal(2), width =5, font = ("Consolas", 20 ))
but_2.grid(row = 2, column=2)
but_3 = tk.Button(root, text ='3', command=lambda: add_cal(3), width =5, font = ("Consolas", 20 ))
but_3.grid(row = 2, column=3)
but_4 = tk.Button(root, text ='4', command=lambda: add_cal(4), width =5, font = ("Consolas", 20 ))
but_4.grid(row = 3, column=1)
but_5 = tk.Button(root, text ='5', command=lambda: add_cal(5), width =5, font = ("Consolas", 20 ))
but_5.grid(row = 3, column=2)
but_6 = tk.Button(root, text ='6', command=lambda: add_cal(6), width =5, font = ("Consolas", 20 ))
but_6.grid(row = 3, column=3)
but_7 = tk.Button(root, text ='7', command=lambda: add_cal(7), width =5, font = ("Consolas", 20 ))
but_7.grid(row = 4, column=1)
but_8 = tk.Button(root, text ='8', command=lambda: add_cal(8), width =5, font = ("Consolas", 20 ))
but_8.grid(row = 4, column=2)
but_9 = tk.Button(root, text ='9', command=lambda: add_cal(9), width =5, font = ("Consolas", 20 ))
but_9.grid(row = 4, column=3)
but_0 = tk.Button(root, text ='0', command=lambda: add_cal(0), width =5, font = ("Consolas", 20 ))
but_0.grid(row = 5, column=2)
#buttons for operators
but_plus = tk.Button(root, text ='+', command=lambda: add_cal("+"), width =5, font = ("Consolas", 20 ))
but_plus.grid(row = 2, column=4)
but_minus = tk.Button(root, text ='-', command=lambda: add_cal('-'), width =5, font = ("Consolas", 20 ))
but_minus.grid(row = 3, column=4)
but_times= tk.Button(root, text ='*', command=lambda: add_cal("*"), width =5, font = ("Consolas", 20 ))
but_times.grid(row = 4, column=4)
but_divide = tk.Button(root, text ='/', command=lambda: add_cal("/"), width =5, font = ("Consolas", 20 ))
but_divide.grid(row = 5, column=4)
#buttons for parathesis
but_open = tk.Button(root, text ='(', command=lambda: add_cal("("), width =5, font = ("Consolas", 20 ))
but_open.grid(row = 5, column=1)
but_close = tk.Button(root, text =')', command=lambda: add_cal(")"), width =5, font = ("Consolas", 20 ))
but_close.grid(row = 5, column=3)
#buttons for clear and eval functions
but_equal = tk.Button(root, text ='=', command=evalute_cal, width =12, font = ("Consolas", 20 ))
but_equal.grid(row = 6, column=3,columnspan=2)
but_clear = tk.Button(root, text ='Clear', command = clear_field, width =12, font = ("Consolas", 20 ))
but_clear.grid(row = 6, column=1, columnspan=2)

root.mainloop()

