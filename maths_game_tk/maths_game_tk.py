import tkinter as tk
from tkinter import ttk
import random

class User:
    def __init__(self):
        self.total_count: int = 0
        self.total_incorrect: int = 0
        self.count: int = 0
        self.incorrect: int = 0
        self.tables: str = ''
        self.theme: str = ''
        self.last_answer: str = ''
        self.last_theme: str = ''
        self.corrections_list : list[tuple[int, int, int, str]] = []

    def update_score(self):    
        self.total_count += self.count
        self.count = 0
        self.total_incorrect += self.incorrect
        self.incorrect = 0
        pass

class Game:

    player = User()

    def generate_question(self, operation: str, table: str) -> int:
        if table == 'All':
            b = random.randint(2,12)
        else:
            b = int(table)
        return b

    def addition(self):
        a = random.randint(1, 100)
        b = random.randint(1, 100)
        return a + b, a, b, '+'

    def subtraction(self):
        b = random.randint(1, 100)
        a = random.randint(b, 100)
        return a - b, a, b, '-'

    def multiplication(self):
        b = Game.generate_question(self, Game.player.theme, Game.player.tables)
        a = random.randint(2, 12)
        return a * b, a, b, 'x'

    def division(self):
        b = Game.generate_question(self, Game.player.theme, Game.player.tables)
        a = b * random.randint(2, 12)
        while a / b == Game.player.last_answer and a != b:
            a = b * random.randint(2, 12)
        return a // b, a, b, '÷'

    def randomise(self):
        operations = [Game.addition, Game.subtraction, Game.multiplication, Game.division]
        operation = random.choice(operations)
        while operation == Game.player.last_theme:
            operation = random.choice(operations)
        return operation(self)

class Operation:
    operations ={
        'Addition': Game.addition,
        'Subtraction': Game.subtraction,
        'Multiplication': Game.multiplication,
        'Division': Game.division,
        'Random': Game.randomise
    }

class MathsGameApp:
    def __init__(self, master):

        self.round_length = 5
        self.master = master
        self.master.title("Maths Game")
        
        self.label = ttk.Label(master, text="Welcome to the Maths Game!")
        self.label.pack(pady=10)
        
        self.start_button = ttk.Button(master, text="Start Game", command=self.start_game)
        self.start_button.pack(pady=5)

        self.next_question_button = ttk.Button(master, text="Next Question", command=self.next_question)

        self.total_score_label = ttk.Label(master, text="")
        self.accuracy_label = ttk.Label(master, text="")
        self.total_accuracy_label = ttk.Label(master, text="")
        self.please_select_label = ttk.Label(master, text="Please select a valid option!")

        self.try_again_button = ttk.Button(self.master, text="Try Again", command=self.retry_question)
        self.check_button = ttk.Button(self.master, text="Check Answer", command=self.check_answer)
        self.go_again_button = ttk.Button(self.master, text="Play Again", command=self.start_game)
        self.finish_button = ttk.Button(self.master, text="Finish Practice", command=self.finish_practice)
        self.check_retry_button = ttk.Button(self.master, text="Check Answer", command=self.check_retry)

        self.quit_button = ttk.Button(master, text="Quit", command=master.quit)
        self.quit_button.pack(pady=5)

    def start_game(self):
        self.accuracy_label.pack_forget()
        self.total_accuracy_label.pack_forget()
        self.total_score_label.pack_forget()
        self.go_again_button.pack_forget()
        self.start_button.pack_forget()
        self.quit_button.pack_forget()
        self.label.config(text="Which operation would you like to practice?")
        self.operations_menu = ttk.Menubutton(self.master, text="Select Operation")
        operations_menu = tk.Menu(self.operations_menu, tearoff=0)
        operations = ['Addition', 'Subtraction', 'Multiplication', 'Division', 'Random']
        for operation in operations:
            operations_menu.add_radiobutton(label=operation, command=lambda op=operation: self.operations_menu.config(text=op), value=operation)
        self.operations_menu['menu'] = operations_menu
        self.operations_menu.pack(pady=5)
        self.label.config(text=f"What would you like to practice?")
        self.tables_menu = ttk.Menubutton(self.master, text="Select Tables")
        tables_menu = tk.Menu(self.tables_menu, tearoff=0)
        for i in range(2, 13):
            tables_menu.add_radiobutton(label=str(i), command=lambda x=i: self.tables_menu.config(text=f"{x} Times Tables"), value=str(i))
        tables_menu.add_radiobutton(label="All", command=lambda: self.tables_menu.config(text="All Times Tables"), value="Random")
        self.tables_menu["menu"] = tables_menu
        self.tables_menu.pack(pady=5)
        self.submit_button = ttk.Button(self.master, text="Submit", command=lambda: self.start_practice(self.operations_menu.cget("text"), self.tables_menu.cget("text").split()[0]))
        self.submit_button.pack(pady=5)

    def start_practice(self, operation, tables):
        if operation == 'Select Operation' or tables == 'Select':
            self.please_select_label.pack(pady=5)
            return
        self.please_select_label.pack_forget()
        Game.player.theme = operation
        Game.player.tables = tables
        self.operations_menu.pack_forget()
        self.tables_menu.pack_forget()
        self.submit_button.pack_forget()
        self.label.config(text=f'Practicing {operation} tables: {tables}')
        self.correct_answer, self.num1, self.num2, self.symbol = Operation.operations[operation](self)
        self.question_text = ttk.Label(self.master, text=f'What is {self.num1} {self.symbol} {self.num2}?')
        self.question_text.pack(pady=5)
        self.answer_entry = ttk.Entry(self.master)
        self.answer_entry.pack(pady=5)
        self.check_button.config(text="Check Answer", command=self.check_answer)
        self.check_button.pack(pady=5)

    def retry_question(self):
        self.try_again_button.pack_forget()
        self.next_question_button.pack_forget()
        self.question_text.config(text=f'What is {self.num1} {self.symbol} {self.num2}?')
        self.answer_entry.pack(pady=5)
        self.check_retry_button.config(text="Check Answer", command=self.check_retry)
        self.check_retry_button.pack(pady=5)
    
    def next_question(self):
        self.label.pack_forget()
        if Game.player.count >= self.round_length:
            self.finish_practice()
        else:
            self.next_question_button.pack_forget()
            self.correct_answer, self.num1, self.num2, self.symbol = Operation.operations[Game.player.theme](self)
            self.question_text.config(text=f'What is {self.num1} {self.symbol} {self.num2}?')
            self.answer_entry.delete(0, tk.END)
            self.answer_entry.pack(pady=5)
            self.check_button.config(text="Check Answer", command=self.check_answer)
            self.check_button.pack(pady=5)

    def review_corrections(self):
        self.next_question_button.pack_forget()
        self.next_question_button.pack_forget()
        if Game.player.corrections_list:
            self.label.config(text="Reviewing answers:")
            self.corrections_questions(Game.player.corrections_list[0])

    def corrections_questions(self, correction):
        self.correct_answer, self.num1, self.num2, self.symbol = correction
        self.question_text.config(text=f'What is {self.num1} {self.symbol} {self.num2}?')
        self.answer_entry.delete(0, tk.END)
        self.answer_entry.pack(pady=5)
        self.check_button.config(text="Check Answer", command=self.check_corrections)
        self.check_button.pack(pady=5)
        
    def check_corrections(self):
        self.answer_entry.pack_forget()
        self.check_button.pack_forget()
        user_answer = self.answer_entry.get()
        if str(user_answer) == str(self.correct_answer):
            self.question_text.config(text="Correct!")
        else:
            self.question_text.config(text=f'Incorrect! The correct answer was {self.correct_answer}.')
        Game.player.corrections_list.pop(0)
        if Game.player.corrections_list:
            self.next_question_button.config(text="Next Correction", command=lambda: self.corrections_questions(Game.player.corrections_list[0]))
            self.next_question_button.pack(pady=5)
        else:
            self.finish_button.pack(pady=5)

    def next_correction(self):
        if Game.player.corrections_list:
            self.next_question_button.config(text="Next Correction", command=lambda: self.corrections_questions(Game.player.corrections_list[0]))
            self.next_question_button.pack(pady=5)
        else:
            self.finish_practice()

    def check_answer(self):
        self.answer_entry.pack_forget()
        self.check_button.pack_forget()
        user_answer = self.answer_entry.get()
        Game.player.last_answer = user_answer
        Game.player.last_theme = Game.player.theme
        self.label.config(text=f'You answered: {user_answer}')
        if str(user_answer) == str(self.correct_answer):
            self.question_text.config(text="Correct!")
            self.next_question_button.config(text="Next Question", command=self.next_question)
            self.next_question_button.pack(pady=5)
        else:
            self.question_text.config(text=f'Incorrect!')
            Game.player.incorrect += 1
            Game.player.corrections_list.append((self.correct_answer, self.num1, self.num2, self.symbol))
            self.try_again_button.pack(pady=5)
        Game.player.count += 1
        if Game.player.count >= self.round_length and not Game.player.corrections_list:
            self.next_question_button.pack_forget()
            self.finish_button.pack(pady=5)

    def check_retry(self):
        self.check_retry_button.pack_forget()
        self.answer_entry.pack_forget()
        self.check_button.pack_forget()
        user_answer = self.answer_entry.get()
        if str(user_answer) == str(self.correct_answer):
            self.question_text.config(text="Correct!")
            self.next_question_button.config(text="Next Question", command=self.next_question)
            self.next_question_button.pack(pady=5)
        else:
            self.question_text.config(text=f'Incorrect!')
            self.try_again_button.pack(pady=5)

    def finish_practice(self):
        if Game.player.corrections_list:
            Game.player.corrections_list = list(set(Game.player.corrections_list))
            self.review_corrections()
            return
        self.next_question_button.pack_forget()
        self.question_text.pack_forget()
        self.answer_entry.pack_forget()
        self.check_button.pack_forget()
        self.finish_button.pack_forget()
        self.label.config(text=f'Practice Finished! You got {Game.player.count - Game.player.incorrect} out of {Game.player.count} correct.')
        self.accuracy_label.config(text=f'Accuracy: {((Game.player.count - Game.player.incorrect) / Game.player.count) * 100:.2f}%')
        Game.player.update_score()
        self.total_score_label.config(text=f'Total Score: {Game.player.total_count - Game.player.total_incorrect} out of {Game.player.total_count}')
        self.total_accuracy_label.config(text=f'Total Accuracy: {((Game.player.total_count - Game.player.total_incorrect) / Game.player.total_count) * 100:.2f}%')
        self.label.pack(pady=5)
        self.accuracy_label.pack(pady=5)
        self.total_score_label.pack(pady=5)
        self.total_accuracy_label.pack(pady=5)
        self.go_again_button.pack(pady=5)
        self.quit_button.pack(pady=5)

if __name__ == "__main__":
    root = tk.Tk()
    root.title("Maths Game")

    window_width = 300
    window_height = 200

    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()

    center_x = int(screen_width/2 - window_width / 2)
    center_y = int(screen_height/2 - window_height / 2)
    
    root.geometry(f"{window_width}x{window_height}+{center_x}+{center_y}")
    root.resizable(True, True)
    app = MathsGameApp(root)
    root.mainloop()