# main.py

import tkinter as tk
from questions import questions
from show_result import show_result
from quotes import show_quotes

current_question = 0
score = 0
selected_option = None  # Initialize variable after root exists

def start_quiz(root):
    global current_question, score
    current_question = 0
    score = 0
    load_question(root)

def load_question(root):
    global current_question, score, selected_option

    for widget in root.winfo_children():
        widget.destroy()

    if current_question >= len(questions):
        show_result(root, score)
        return

    question_data = questions[current_question]
    selected_option = tk.StringVar(root)  # Initialize StringVar AFTER root exists

    # Stylish header
    header_frame = tk.Frame(root, bg="#34495e", padx=30, pady=20)
    header_frame.pack(fill="x")
    tk.Label(header_frame, text=f"Question {current_question + 1} of {len(questions)}",
             font=("Roboto", 16), fg="white", bg="#34495e").pack()

    tk.Label(root, text=question_data["text"], font=("Arial", 16, "bold"),
             wraplength=500, justify="center", fg="#2c3e50", pady=20).pack(pady=(10, 20))

    for text, value in question_data["options"]:
        # Stylish RadioButtons
        tk.Radiobutton(root, text=text, variable=selected_option, value=value,
                       font=("Arial", 12), wraplength=400, anchor="w", 
                       bg="#ecf0f1", activebackground="#bdc3c7", relief="flat", 
                       highlightbackground="#2c3e50", highlightthickness=3).pack(anchor="w", padx=100, pady=5)

    def next_question():
        global score, current_question
        val = selected_option.get()
        if val:
            score += int(val)
            current_question += 1
            load_question(root)

    # Shiny Next Button
    tk.Button(root, text="Next ➡️", command=next_question, bg="#27ae60", fg="white",
              font=("Arial", 12, "bold"), padx=20, pady=10, relief="flat",
              activebackground="#2ecc71").pack(pady=20)

def show_main_menu(root):
    for widget in root.winfo_children():
        widget.destroy()

    # Gradient Background
    root.configure(bg="#f5f5f5")

    # Title Frame with Glow Effect
    title_frame = tk.Frame(root, bg="#2c3e50", padx=50, pady=40)
    title_frame.pack(fill="x")
    tk.Label(title_frame, text="🧠 Mental Health Detection", font=("Roboto", 24, "bold"), fg="white", bg="#2c3e50").pack()

    # Buttons with shiny and hover effects
    tk.Button(root, text="Start Detection 🎯", command=lambda: start_quiz(root),
              font=("Arial", 14), bg="#3498db", fg="white", width=30, pady=15, relief="flat",
              activebackground="#2980b9", activeforeground="white").pack(pady=10)

    tk.Button(root, text="Mental Health Quotes 💬", command=lambda: show_quotes(root),
              font=("Arial", 14), bg="#9b59b6", fg="white", width=30, pady=15, relief="flat",
              activebackground="#8e44ad", activeforeground="white").pack(pady=10)

    tk.Button(root, text="Exit ❌", command=root.quit, font=("Arial", 12), bg="#e74c3c", fg="white",
              width=15, pady=10, relief="flat", activebackground="#c0392b").pack(pady=30)

# Launch app
if __name__ == "__main__":
    root = tk.Tk()
    root.title("Calm Within")
    root.geometry("700x700")
    root.resizable(False, False)
    show_main_menu(root)
    root.mainloop()
