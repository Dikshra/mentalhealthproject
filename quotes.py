# quotes.py

import tkinter as tk
import random

mental_health_quotes = [
    "“You don’t have to control your thoughts. You just have to stop letting them control you.” – Dan Millman",
    "“Almost everything will work again if you unplug it for a few minutes, including you.” – Anne Lamott",
    "“Mental health… is not a destination, but a process.” – Noam Shpancer",
    "“Just when the caterpillar thought the world was over, it became a butterfly.” – Anonymous",
    "“Healing takes time, and asking for help is a courageous step.” – Mariska Hargitay",
    "“Happiness can be found even in the darkest of times, if one only remembers to turn on the light.” – J.K. Rowling",
    "“Self-care is how you take your power back.” – Lalah Delia",
    "“You are not alone. You are seen. I am with you. You are not alone.” – Shonda Rhimes",
]

def show_quotes(root):
    for widget in root.winfo_children():
        widget.destroy()

    quote = random.choice(mental_health_quotes)

    frame = tk.Frame(root, padx=40, pady=40)
    frame.pack(expand=True)

    tk.Label(frame, text="💬 Mental Health Quote", font=("Arial", 18, "bold"),
             fg="#2c3e50").pack(pady=20)

    tk.Label(frame, text=f"{quote}", font=("Arial", 12, "italic"),
             wraplength=500, justify="center", fg="#7f8c8d").pack(pady=20)

    tk.Button(root, text="Back to Menu", command=lambda: __import__('main').show_main_menu(root),
              font=("Arial", 12), bg="#34495e", fg="white", padx=10, pady=5).pack(pady=30)
