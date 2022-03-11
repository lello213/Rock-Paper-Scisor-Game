import tkinter as tk
import random
from tkinter import *
from tkinter import messagebox

a = ["Rock", "Paper", "Scisor"]

def cpu_play():
    v=random.choice(a)
    return v

def btn_click(item):
    v=cpu_play()
    if item=="Rock":
        if v=="Scisor":
            messagebox.showinfo("Result", "CPU choose Scisor...You Win!")
        elif v=="Paper":
            messagebox.showinfo("Result", "CPU choose Paper...You Loose!")
        elif v=="Rock":
            messagebox.showinfo("Result", "CPU choose Rock...Tie!")
    elif item=="Paper":
        if v == "Scisor":
            messagebox.showinfo("Result", "CPU choose Scisor...You Loose!")
        elif v == "Paper":
            messagebox.showinfo("Result", "CPU choose Paper...Tie!")
        elif v == "Rock":
            messagebox.showinfo("Result", "CPU choose Rock...You Win!")
    elif item=="Scisor":
        if v == "Scisor":
            messagebox.showinfo("Result", "CPU choose Scisor...Tie!")
        elif v == "Paper":
            messagebox.showinfo("Result", "CPU choose Paper...You Win!")
        elif v == "Rock":
            messagebox.showinfo("Result", "CPU choose Rock...You Loose!")

window = tk.Tk()

label = tk.Label(
    text="Rock, Paper or Scisor?",
    width=33,
    fg="white",
    bg="blue",
)
label.pack(fill=tk.BOTH, expand=True)

def play():
    rock = tk.Button(
        text="Rock",
        width=32,
        bg="blue",
        fg="yellow",
        command=lambda:btn_click("Rock")
    )
    rock.pack(fill=tk.BOTH, expand=True)

    paper = tk.Button(
        text="Paper",
        width=32,
        bg="blue",
        fg="yellow",
        command=lambda:btn_click("Paper")
    )
    paper.pack(fill=tk.BOTH, expand=True)

    scisor = tk.Button(
        text="Scisor",
        width=32,
        bg="blue",
        fg="yellow",
        command=lambda:btn_click("Scisor")
    )
    scisor.pack(fill=tk.BOTH, expand=True)

play()
window.mainloop()