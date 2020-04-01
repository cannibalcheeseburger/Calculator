from tkinter import *

root = Tk()
root.title("MOTHER FUCKING CALCULATOR. BITCH!")

Enter = Entry(root,width = 60,borderwidth = 5)
Enter.grid(row = 0,column = 0,columnspan = 4,padx = 9,pady = 10)

def ins(number):
    number = Enter.get() + number
    Enter.delete(0,END)
    Enter.insert(0,number)

def clr():
    Enter.delete(0,END)

def eq():
    answer = eval(Enter.get())
    Enter.delete(0,END)
    Enter.insert(0,answer)

button_1 = Button(root,text = "1",padx = 40,pady = 20,command = lambda : ins("1")).grid(row = 1, column = 0)
button_2 = Button(root,text = "2",padx = 40,pady = 20,command = lambda : ins("2")).grid(row = 1, column = 1)
button_3 = Button(root,text = "3",padx = 40,pady = 20,command = lambda : ins("3")).grid(row = 1, column = 2)
button_add = Button(root,text = "+",padx = 40,pady = 20,command = lambda : ins("+")).grid(row = 1, column = 3)

button_4 = Button(root,text = "4",padx = 40,pady = 20,command = lambda : ins("4")).grid(row = 2, column = 0)
button_5 = Button(root,text = "5",padx = 40,pady = 20,command = lambda : ins("5")).grid(row = 2, column =1)
button_6 = Button(root,text = "6",padx = 40,pady = 20,command = lambda : ins("6")).grid(row = 2, column = 2)
button_sub = Button(root,text = "- ",padx = 40,pady = 20,command = lambda : ins("-")).grid(row = 2, column = 3)

button_7 = Button(root,text = "7",padx = 40,pady = 20,command = lambda : ins("7")).grid(row = 3, column = 0)
button_8 = Button(root,text = "8",padx = 40,pady = 20,command = lambda : ins("8")).grid(row = 3, column = 1)
button_9 = Button(root,text = "9",padx = 40,pady = 20,command = lambda : ins("9")).grid(row = 3, column = 2)
button_mul = Button(root,text = "* ",padx = 40,pady = 20,command = lambda : ins("*")).grid(row = 3, column = 3)

button_dot = Button(root,text = ". ",padx = 40,pady = 20,command = lambda : ins(".")).grid(row = 4, column = 0)
button_0 = Button(root,text = "0",padx = 40,pady = 20,command = lambda : ins("0")).grid(row = 4, column = 1)
button_clear = Button(root,text = "clr " ,padx = 35,pady = 20,command = lambda : clr()).grid(row = 4, column = 2)
button_div = Button(root,text = "%",padx = 39,pady = 20,command = lambda : ins("/")).grid(row = 4, column = 3)

button_equ = Button(root,text = "= ",padx = 181,pady = 20,command = lambda : eq()).grid(row = 5, column = 0,columnspan = 4)

root.mainloop()