import tkinter as tk
from tkinter import messagebox
import time
import threading

saved_times = "tijden.txt"

def times_saved(minutes, seconds):
    with open(saved_times, "a") as file:
        file.write(f"{minutes},{seconds}\n")
    print(f"Tijd is opgeslagen in {saved_times}: {minutes} minuten, {seconds} secondes.")
def start_timer():
    try:
        minutes = int(entry_minutes.get())
        seconds = int(entry_seconds.get())
        total_seconds = minutes * 60 + seconds

        times_saved(minutes, seconds)

        if total_seconds <= 0:
            messagebox.showwarning("Ongeldige tijd", "Voer een tijd in die groter is dan 0.")
            return

        def countdown():
            nonlocal total_seconds
            while total_seconds > 0:
                mins, secs = divmod(total_seconds, 60)
                timer_label.config(text=f"{mins:02}:{secs:02}")
                time.sleep(1)
                total_seconds -= 1

            timer_label.config(text="00:00")
            messagebox.showinfo("Timer", "De tijd is om!")

        threading.Thread(target=countdown, daemon=True).start()

    except ValueError:
        messagebox.showwarning("Foutieve invoer", "Voer geldige getallen in voor minuten en seconden (beide velden moeten ingevuld worden).")

# Hoofdvenster
root = tk.Tk()
root.title("STEAM Timer")
root.geometry("500x400")
root.resizable(False, False)

# Titel
title_label = tk.Label(root, text="STEAM", font=("Helvetica", 36, "bold"), fg="black")
title_label.pack(pady=20)

instructie_label = tk.Label(root, text="Vul hieronder in hoelang je wilt gamen",
                            font=("Helvetica", 12), fg="gray")
instructie_label.pack(pady=5)

# Timer invoer
frame = tk.Frame(root)
frame.pack(pady=10)

entry_minutes = tk.Entry(frame, width=5, font=("Helvetica", 16))
entry_minutes.grid(row=0, column=0, padx=5)

entry_seconds = tk.Entry(frame, width=5, font=("Helvetica", 16))
entry_seconds.grid(row=0, column=1, padx=5)

minutes_label = tk.Label(frame, text="Min", font=("Helvetica", 12))
minutes_label.grid(row=1, column=0)

seconds_label = tk.Label(frame, text="Sec", font=("Helvetica", 12))
seconds_label.grid(row=1, column=1)

# Startknop
start_button = tk.Button(root, text="Start Timer", font=("Helvetica", 16), command=start_timer)
start_button.pack(pady=10)

# Timer label
timer_label = tk.Label(root, text="00:00", font=("Helvetica", 24, "bold"), fg="black")
timer_label.pack(pady=20)

# Hoofdloop
root.mainloop()