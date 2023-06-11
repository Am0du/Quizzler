from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#27374D"


class QuizInterface:
    def __init__(self, quiz_brain: QuizBrain) -> object:
        self.quiz = quiz_brain
        self.counter = 0
        self.window = Tk()
        self.window.title('Quizzler')
        self.window.config(bg=THEME_COLOR, pady=20, padx=20)
        true_img = PhotoImage(file='images/true.png')
        false_img = PhotoImage(file='images/false.png')

        self.score_label = Label(text=f'score:', bg=THEME_COLOR, fg='white', font=('ariel', 10, 'bold'))
        self.score_label.grid(column=1, row=0, )
        self.question_label = Label(text=f'Question: {self.counter} / {self.quiz.len_question}', bg=THEME_COLOR,
                                    fg='white', font=('ariel', 10, 'bold'))
        self.question_label.grid(column=0, row=0, )

        self.canvas = Canvas(height=250, width=300, bg='white', highlightthickness=0)
        self.text = self.canvas.create_text(150, 125, text='Test', width=280, fill=THEME_COLOR,
                                            font=('ariel', 20, 'italic'))
        self.canvas.grid(column=0, row=1, columnspan=2, pady=50)

        self.right_button = Button(image=true_img, highlightthickness=0, bd=0, command=self.right_answer)
        self.right_button.grid(column=0, row=2)
        self.wrong_button = Button(image=false_img, highlightthickness=0, bd=0, command=self.wrong_answer)
        self.wrong_button.grid(column=1, row=2)

        self.get_next_question()
        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(bg='white')
        self.score_label.config(text=f'Score: {self.quiz.score}')

        self.question_label.config(text=f'Question: {self.counter} / {self.quiz.len_question}')
        if self.quiz.still_has_questions():
            self.counter += 1
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.text, text=q_text, )
        else:
            self.canvas.itemconfig(self.text,
                                   text=f"You've reached the end of the quiz\ntotal Score : "
                                        f"{self.quiz.score}/{self.quiz.question_number} ")
            self.right_button.config(state='disabled')
            self.wrong_button.config(state='disabled')
            end_button = Button(text='END', bd=0, bg='red', font=('ariel', 20, 'italic'), highlightthickness=0, command=self.window.destroy)
            end_button.grid(column=0, row=3, columnspan=2, pady=20,)

    def right_answer(self):
        answer = 'true'
        self.feedback(self.quiz.check_answer(answer))

    def wrong_answer(self):
        answer = 'false'
        self.feedback(self.quiz.check_answer(answer))

    def feedback(self, is_right):
        if is_right:
            self.canvas.config(bg='green')
        else:
            self.canvas.config(bg='red')

        self.window.after(1000, self.get_next_question)

