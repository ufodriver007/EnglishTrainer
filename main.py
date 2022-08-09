from tkinter import *
from tkinter import messagebox

window = Tk()

window.title("English Trainer")

window.geometry('600x500')

#messagebox.showinfo('Message title','Message content')
radSelected = IntVar()

lbl = Label(window, text="Particular", font=("Arial Bold", 50))
lbl.place(x=180, y=100)
lblAnswer = Label(window, text="особый", font=("Arial", 30))
lblAnswer.place(x=180, y=200)

def btnEng_clicked():
    lbl.configure(text="Button was clicked !!")

def btnRus_clicked():
    lbl.configure(text="Button was clicked !!")

def btnGram_clicked():
    lbl.configure(text="Button was clicked !!")

def btnTab_clicked():
    lbl.configure(text="Button was clicked !!")

def btnNext_clicked():
    lbl.configure(text=radSelected.get())

radBasic = Radiobutton(window,text='800 words', value=0, variable=radSelected)
radBasic.grid(column=0, row=0)
rad3000 = Radiobutton(window,text='3000 words', value=1, variable=radSelected)
rad3000.grid(column=1, row=0)

btnEng = Button(window, text="Английские слова", command=btnEng_clicked, padx=5, pady=5)
btnEng.grid(column=0, row=1)

btnRus = Button(window, text="Русские слова", command=btnRus_clicked, padx=16, pady=5)
btnRus.grid(column=0, row=2)

btnGram = Button(window, text="Правила", command=btnGram_clicked, padx=31, pady=5)
btnGram.grid(column=0, row=3)

btnTab = Button(window, text="Таблицы", command=btnTab_clicked, padx=30, pady=5)
btnTab.grid(column=0, row=4)

btnNext = Button(window, text="Далее", font=("Arial Bold", 50), bg='#567', command=btnNext_clicked)
#btnNext.grid(column=5, row=7)
btnNext.place(x=180, y=300)

window.mainloop()