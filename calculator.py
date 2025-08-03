import tkinter as tk

# Function to update expression in the entry field
def press(num):
    current = entry.get()
    entry.delete(0, tk.END)
    entry.insert(0, current + str(num))

# Function to evaluate the final expression
def equalpress():
    try:
        result = str(eval(entry.get()))
        entry.delete(0, tk.END)
        entry.insert(0, result)
    except:
        entry.delete(0, tk.END)
        entry.insert(0, "Error")

# Function to clear the entry field
def clear():
    entry.delete(0, tk.END)

# Create the main window
window = tk.Tk()
window.title("Simple Calculator")
window.geometry("320x400")
window.configure(bg="lightgray")

# Entry field for showing input and result
entry = tk.Entry(window, font=('Arial', 20), borderwidth=5, relief="ridge", justify='right')
entry.grid(row=0, column=0, columnspan=4, ipadx=8, ipady=15, padx=10, pady=20)

# Button layout
buttons = [
    ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
    ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
    ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
    ('C', 4, 0), ('0', 4, 1), ('=', 4, 2), ('+', 4, 3),
]

# Create and place buttons
for (text, row, col) in buttons:
    if text == '=':
        btn = tk.Button(window, text=text, padx=20, pady=20, font=('Arial', 14), bg='green', fg='white',
                        command=equalpress)
    elif text == 'C':
        btn = tk.Button(window, text=text, padx=20, pady=20, font=('Arial', 14), bg='red', fg='white',
                        command=clear)
    else:
        btn = tk.Button(window, text=text, padx=20, pady=20, font=('Arial', 14),
                        command=lambda t=text: press(t))
    btn.grid(row=row, column=col, padx=5, pady=5, sticky="nsew")

# Make all cells expand equally
for i in range(5):
    window.rowconfigure(i, weight=1)
    window.columnconfigure(i % 4, weight=1)

# Run the application
window.mainloop()