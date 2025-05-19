# show_result.py

import tkinter as tk

def show_result(root, score):
    for widget in root.winfo_children():
        widget.destroy()

    # Score ranges from -60 to +60 (30 questions × ±2)
    if score >= 45:
        mood = "🌈 Extremely Happy"
        tip = "Keep doing what you're doing! Your positivity is contagious."
        quote = "“Happiness is not something ready made. It comes from your own actions.” – Dalai Lama"
        color = "#27ae60"
    elif 30 <= score < 45:
        mood = "😊 Happy"
        tip = "You’re doing well! Stay connected with the things that bring you joy."
        quote = "“The greatest wealth is to live content with little.” – Plato"
        color = "#2ecc71"
    elif 10 <= score < 30:
        mood = "😌 Neutral / Okay"
        tip = "You’re holding steady. A little self-care could uplift you more!"
        quote = "“Almost everything will work again if you unplug it for a few minutes, including you.” – Anne Lamott"
        color = "#f1c40f"
    elif -10 <= score < 10:
        mood = "😟 Low"
        tip = "It’s okay to not feel okay. A short walk or music might help."
        quote = "“You don’t have to control your thoughts. You just have to stop letting them control you.” – Dan Millman"
        color = "#e67e22"
    else:
        mood = "😢 Stressed / Sad"
        tip = "You're going through a rough patch. Reach out to someone. You're not alone."
        quote = "“You are not your illness. You have an individual story to tell.” – Julian Seifter"
        color = "#e74c3c"

    # Main frame for result
    result_frame = tk.Frame(root, bg=color, padx=30, pady=30)
    result_frame.pack(pady=30)

    tk.Label(result_frame, text=f"Your Mood: {mood}", font=("Arial", 20, "bold"), bg=color, fg="white").pack(pady=10)
    tk.Label(result_frame, text=f"Tip: {tip}", font=("Arial", 12), wraplength=400, bg=color, fg="white", justify="center").pack(pady=5)
    tk.Label(result_frame, text=f"\n{quote}", font=("Arial", 10, "italic"), wraplength=400, bg=color, fg="#ecf0f1", justify="center").pack(pady=10)

    tk.Button(root, text="Exit ❌", command=root.quit, font=("Arial", 12), bg="#34495e", fg="white").pack(pady=20)
