from tkinter import *
import operator

ops = {
    '+': operator.add,
    '-': operator.sub,
    '*': operator.mul,
    '/': operator.truediv,
    '%': operator.mod,
    '^': operator.xor,
}
# setting order to do the operation
calc_order = ['*', '/', '+', '-', '^']

root = Tk()
root.title('Calculator')
tk_input = Entry(root, width="40")

tk_input.grid(row=0, column=0, columnspan=3, padx=2, pady=2, ipady=3)


def button00():
    tk_input.insert(len(tk_input.get()) + 1, '1')


def button01():
    tk_input.insert(len(tk_input.get()) + 1, '2')


def button02():
    tk_input.insert(len(tk_input.get()) + 1, '3')


def button03():
    tk_input.insert(len(tk_input.get()) + 1, '4')


def button04():
    tk_input.insert(len(tk_input.get()) + 1, '5')


def button05():
    tk_input.insert(len(tk_input.get()) + 1, '6')


def button06():
    tk_input.insert(len(tk_input.get()) + 1, '7')


def button07():
    tk_input.insert(len(tk_input.get()) + 1, '8')


def button08():
    tk_input.insert(len(tk_input.get()) + 1, '9')


def button09():
    tk_input.insert(len(tk_input.get()) + 1, '0')


def button_plus():
    tk_input.insert(len(tk_input.get()) + 1, ' + ')


def button_subtract():
    tk_input.insert(len(tk_input.get()) + 1, ' - ')


def button_multiply():
    tk_input.insert(len(tk_input.get()) + 1, ' * ')


def button_divide():
    tk_input.insert(len(tk_input.get()) + 1, ' / ')


def button_equal():
    # Calculation based on operation
    def cal_operation(i, j):
        answer[j - 1:j + 2] = [str(int(ops[i](int(answer[j - 1]), int(answer[j + 1]))))]

    # answer takes input value from the textbox of tkinter
    answer = list(tk_input.get().split())
    # loops through the list and calculate based on --> calc_order
    [[cal_operation(i, j) for i, j in zip(reversed(answer), reversed(range(len(answer)))) if x == i] for x in
     calc_order]
    # clear the textbox of tkinter and displays the answer
    tk_input.delete(0, END)
    tk_input.insert(0, answer)


def button_clear():
    tk_input.delete(0, END)


button1 = Button(root, text='1', padx=32, pady=10, command=button00)
button2 = Button(root, text='2', padx=32, pady=10, command=button01)
button3 = Button(root, text='3', padx=32, pady=10, command=button02)
button4 = Button(root, text='4', padx=32, pady=10, command=button03)
button5 = Button(root, text='5', padx=32, pady=10, command=button04)
button6 = Button(root, text='6', padx=32, pady=10, command=button05)
button7 = Button(root, text='7', padx=32, pady=10, command=button06)
button8 = Button(root, text='8', padx=32, pady=10, command=button07)
button9 = Button(root, text='9', padx=32, pady=10, command=button08)
button0 = Button(root, text='0', padx=32, pady=10, command=button09)
button_plus = Button(root, text='+', padx=31, pady=10, command=button_plus)
button_subtract = Button(root, text='-', padx=32, pady=10, command=button_subtract)
button_multiply = Button(root, text='*', padx=32, pady=10, command=button_multiply)
button_divide = Button(root, text='/', padx=32, pady=10, command=button_divide)
button_equal = Button(root, text='=', padx=32, pady=10, command=button_equal)
button_clear = Button(root, text='Clear', padx=105, pady=10, command=button_clear)

button1.grid(row=3, padx=2, pady=2, column=0)
button2.grid(row=3, padx=2, pady=2, column=1)
button3.grid(row=3, padx=2, pady=2, column=2)

button4.grid(row=2, padx=2, pady=2, column=0)
button5.grid(row=2, padx=2, pady=2, column=1)
button6.grid(row=2, padx=2, pady=2, column=2)

button7.grid(row=1, padx=2, pady=2, column=0)
button8.grid(row=1, padx=2, pady=2, column=1)
button9.grid(row=1, padx=2, pady=2, column=2)

button_plus.grid(row=4, padx=2, pady=2,  column=0)
button0.grid(row=4, padx=2, pady=2,  column=1)
button_subtract.grid(row=4, padx=2, pady=2,  column=2)

button_multiply.grid(row=5, padx=2, pady=2,  column=0)
button_divide.grid(row=5, padx=2, pady=2,  column=1)
button_equal.grid(row=5, padx=2, pady=2, column=2)

button_clear.grid(row=6, column=0, columnspan=3)
root.mainloop()
