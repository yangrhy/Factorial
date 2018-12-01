from tkinter import *

def Factorial(n):
    fact = 1
    if n <= 1:
        return 1
    else:
        for i in range(1, n+1):
            fact *= i
        return fact
    
def DisplayString(factString):
    n = int(factString)
    newString = str(Factorial(n))
    entry2 = Entry(master)
    entry2.grid(row = 1, column = 1)
    entry2.insert(0,newString)

    
master = Tk()
master.title("Factorial Calculator")
master.geometry("300x100+0+0")

Label(master, text = "N:").grid(row = 0)
Label(master, text = "N!:").grid(row = 1)

entry1 = Entry(master)
entry1.grid(row = 0, column = 1)

factButton = Button(master, text = "Calculate", width = 10, command = lambda: DisplayString(entry1.get())).grid(row = 2, column = 1)

mainloop()