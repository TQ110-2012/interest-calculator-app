import tkinter as tk
from tkinter import messagebox

def calculate_interest():
    try:
        p = float(entry_p.get())  # Principal
        t = float(entry_t.get())  # Time (years)
        r = float(entry_r.get())  # Rate (%)

        # Simple Interest: (P * T * R) / 100
        si = (p * t * r) / 100
        
        # Compound Interest: P * (1 + R/100)^T - P
        ci = p * (pow((1 + r / 100), t)) - p

        label_si.config(text=f"Simple Interest: ${si:.2f}")
        label_ci.config(text=f"Compound Interest: ${ci:.2f}")
    except ValueError:
        messagebox.showerror("Input Error", "Please enter valid numbers")

# UI Setup
root = tk.Tk()
root.title("Interest Calculator")
root.geometry("300x350")

# Input Fields
tk.Label(root, text="Principal Amount ($):").pack(pady=5)
entry_p = tk.Entry(root)
entry_p.pack()

tk.Label(root, text="Time Period (Years):").pack(pady=5)
entry_t = tk.Entry(root)
entry_t.pack()

tk.Label(root, text="Interest Rate (%):").pack(pady=5)
entry_r = tk.Entry(root)
entry_r.pack()

# Calculate Button
tk.Button(root, text="Calculate", command=calculate_interest, bg="blue", fg="white").pack(pady=20)

# Results
label_si = tk.Label(root, text="Simple Interest: $0.00", font=("Arial", 10, "bold"))
label_si.pack()

label_ci = tk.Label(root, text="Compound Interest: $0.00", font=("Arial", 10, "bold"))
label_ci.pack()

root.mainloop()
