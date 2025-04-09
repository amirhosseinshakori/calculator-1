import tkinter as tk
from math import sqrt

def click(event):
    text = event.widget.cget("text")
    
    if text == "=":
        try:
            result = str(eval(entry.get()))
            entry.delete(0, tk.END)
            entry.insert(tk.END, result)
        except:
            entry.delete(0, tk.END)
            entry.insert(tk.END, "خطا")
    
    elif text == "AC":
        entry.delete(0, tk.END)
    
    elif text == "CE":
        current = entry.get()
        entry.delete(0, tk.END)
        entry.insert(0, current[:-1])
    
    elif text == "√":
        try:
            result = sqrt(float(entry.get()))
            entry.delete(0, tk.END)
            entry.insert(tk.END, str(result))
        except:
            entry.delete(0, tk.END)
            entry.insert(tk.END, "خطا")
    
    elif text == "^":
        entry.insert(tk.END, "**")
    
    elif text == "%":
        entry.insert(tk.END, "/100")
    
    else:
        entry.insert(tk.END, text)

# طراحی پنجره
win = tk.Tk()
win.title("ماشین حساب")
win.geometry("400x550")
win.configure(bg="#1e1e1e")

# ورودی
entry = tk.Entry(win, font="Arial 24", bg="#252526", fg="white", bd=0, relief=tk.FLAT, justify="right")
entry.pack(fill=tk.BOTH, ipadx=8, ipady=15, padx=10, pady=15)

# دکمه‌ها
button_frame = tk.Frame(win, bg="#1e1e1e")
button_frame.pack()

buttons = [
    ['AC', 'CE', '(', ')'],
    ['7', '8', '9', '/'],
    ['4', '5', '6', '*'],
    ['1', '2', '3', '-'],
    ['0', '.', '=', '+'],
    ['√', '^', '%']
]

for row in buttons:
    row_frame = tk.Frame(button_frame, bg="#1e1e1e")
    row_frame.pack(expand=True, fill="both", pady=3)
    for btn_text in row:
        btn = tk.Button(row_frame, text=btn_text, font="Arial 18", bg="#3c3c3c", fg="white",
                        activebackground="#007acc", activeforeground="white", height=2, width=6, bd=0)
        btn.pack(side='left', expand=True, fill='both', padx=3)
        btn.bind("<Button-1>", click)

win.mainloop()