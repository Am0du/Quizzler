from tkinter import *
from tkinter import ttk

THEME_COLOR = "#27374D"


class Setup:
    def __init__(self):
        self.num_of_question = 0
        self.category = ''

    def startup(self):

        window = Tk()
        window.title('Quizzler setup')
        window.geometry('500x300')
        window.config(bg=THEME_COLOR, pady=50, padx=20,)

        num_question = Label(text='Number of question:', bg=THEME_COLOR, fg='white')
        num_question.grid(row=0, column=0)
        num = IntVar(value=10)
        radio_1 = Radiobutton(text='10', bg=THEME_COLOR, value=10, variable=num)
        radio_1.grid(row=1, column=0)
        radio_2 = Radiobutton(text='20', bg=THEME_COLOR, value=20, variable=num)
        radio_2.grid(row=1, column=1)
        radio_3 = Radiobutton(text='30', bg=THEME_COLOR, value=30, variable=num)
        radio_3.grid(row=1, column=2)

        cat = Label(text=f'Category:', bg=THEME_COLOR, fg='white')
        cat.grid(row=2, column=0)
        n = StringVar()
        combo = ttk.Combobox(width=27, textvariable=n)
        combo['value'] = ('General Knowledge', 'Animal', 'celebrities', 'Computer')
        combo.grid(row=2, column=1, pady=20, padx=20)
        combo.current(0)

        def sub():
            self.num_of_question = num.get()
            self.category = n.get()
            window.destroy()
        submit = Button(text='Submit', command=sub)
        submit.grid(row=2, column=2)

        window.mainloop()
        
