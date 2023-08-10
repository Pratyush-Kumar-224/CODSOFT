import tkinter as tk
from tkinter import messagebox

class QuizApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Quiz Game")

        self.questions = [
            {"question": "What is the capital of France?", "options": ["London", "Berlin", "Paris", "Madrid"], "answer": "Paris"},
            {"question": "Which gas is responsible for the greenhouse effect?", "options": ["Oxygen", "Carbon Dioxide", "Nitrogen", "Hydrogen"], "answer": "Carbon Dioxide"},
            {"question": "Which planet is known as the Red Planet?", "options": ["Mars", "Venus", "Jupiter", "Saturn"], "answer": "Mars"},
            {"question": "What is the largest mammal?", "options": ["Elephant", "Giraffe", "Blue Whale", "Lion"], "answer": "Blue Whale"},
            {"question": "What is the capital of Japan?", "options": ["Beijing", "Seoul", "Tokyo", "Bangkok"], "answer": "Tokyo"}
            # Add more questions here with options and answers
        ]

        self.score = 0
        self.current_question = 0

        self.question_label = tk.Label(root, text="", wraplength=300)
        self.question_label.pack(pady=10)

        self.answer_var = tk.StringVar()
        self.answer_var.set(None)

        self.options_radios = []
        for i in range(4):
            option_radio = tk.Radiobutton(root, text="", variable=self.answer_var, value=i)
            option_radio.pack(anchor=tk.W)
            self.options_radios.append(option_radio)

        self.clear_button = tk.Button(root, text="Clear Answer", command=self.clear_answer)
        self.clear_button.pack()

        self.submit_button = tk.Button(root, text="Submit", command=self.check_answer)
        self.submit_button.pack()

        self.score_label = tk.Label(root, text="Score: 0")
        self.score_label.pack(pady=10)

        self.play_again_button = tk.Button(root, text="Play Again", command=self.play_again)
        self.play_again_button.pack()
        self.play_again_button.pack_forget()

        self.next_question()

    def next_question(self):
        if self.current_question < len(self.questions):
            question_data = self.questions[self.current_question]
            self.question_label.config(text=question_data["question"])
            self.answer_var.set(None)
            for i in range(4):
                self.options_radios[i].config(text=question_data["options"][i])
            self.clear_button.config(state=tk.NORMAL)
        else:
            self.display_results()

    def check_answer(self):
        if self.answer_var.get() is not None:
            user_choice = self.answer_var.get()
            correct_answer = self.questions[self.current_question]["options"].index(self.questions[self.current_question]["answer"])
            if user_choice == str(correct_answer):
                self.score += 1
                messagebox.showinfo("Correct", "Your answer is correct!")
            else:
                correct_option = self.questions[self.current_question]["answer"]
                messagebox.showerror("Incorrect", f"Sorry, the correct answer is {correct_option}.")
            self.current_question += 1
            self.score_label.config(text=f"Score: {self.score}")
            self.clear_button.config(state=tk.DISABLED)
            self.next_question()
        else:
            messagebox.showwarning("No Answer", "Please select an answer.")

    def clear_answer(self):
        self.answer_var.set(None)

    def display_results(self):
        messagebox.showinfo("Quiz Complete", f"Quiz complete! Your final score is {self.score}")
        self.submit_button.pack_forget()
        self.clear_button.pack_forget()
        self.play_again_button.pack()

    def play_again(self):
        self.score = 0
        self.current_question = 0
        self.score_label.config(text="Score: 0")
        self.play_again_button.pack_forget()
        self.submit_button.pack()
        self.clear_button.pack()
        self.next_question()

def main():
    root = tk.Tk()
    app = QuizApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()