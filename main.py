from question_model import Question
import data
from quiz_brain import QuizBrain
from quiz_setup import Setup
from ui import QuizInterface
from tkinter import messagebox as mb


def game():
    windows = Setup()
    windows.startup()

    question_data = data.request(windows.category, windows.num_of_question)
    question_bank = []
    for question in question_data:
        question_text = question["question"]
        question_answer = question["correct_answer"]
        new_question = Question(question_text, question_answer)
        question_bank.append(new_question)

    quiz = QuizBrain(question_bank)

    window = QuizInterface(quiz)


game()


res = mb.askquestion('Exit Application',
                     'Do you really want to exit')
if res == 'no':
    game()

