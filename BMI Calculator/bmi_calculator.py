import tkinter as tk
from tkinter import messagebox

# Function to calculate BMI
def calculate_bmi():
    try:
        weight = float(entry_weight.get())
        height = float(entry_height.get())
        bmi = weight / (height ** 2)
        bmi = round(bmi, 2)
        category = categorize_bmi(bmi)
        label_result.config(text=f"BMI: {bmi}\nCategory: {category}")
    except ValueError:
        messagebox.showerror("Invalid input", "Please enter valid numbers.")

# Function to categorize BMI
def categorize_bmi(bmi):
    if bmi < 18.5:
        return "Underweight"
    elif 18.5 <= bmi < 24.9:
        return "Normal"
    elif 25 <= bmi < 29.9:
        return "Overweight"
    else:
        return "Obesity"

# Create the main window
root = tk.Tk()
root.title("BMI Calculator")
root.geometry("400x300")  # Set the window size
root.configure(bg="#f0f4f7")  # Background color

# Create a frame for the input fields
frame = tk.Frame(root, bg="#e0e6ed")
frame.pack(pady=20, padx=20, fill="both", expand=True)

# Create input fields for weight and height
label_weight = tk.Label(frame, text="Weight (kg):", bg="#e0e6ed", font=("Helvetica", 12))
label_weight.grid(row=0, column=0, padx=10, pady=10, sticky="w")
entry_weight = tk.Entry(frame, font=("Helvetica", 12), width=10)
entry_weight.grid(row=0, column=1, padx=10, pady=10)

label_height = tk.Label(frame, text="Height (m):", bg="#e0e6ed", font=("Helvetica", 12))
label_height.grid(row=1, column=0, padx=10, pady=10, sticky="w")
entry_height = tk.Entry(frame, font=("Helvetica", 12), width=10)
entry_height.grid(row=1, column=1, padx=10, pady=10)

# Create a button to calculate BMI
btn_calculate = tk.Button(frame, text="Calculate BMI", command=calculate_bmi, font=("Helvetica", 12), bg="#007acc", fg="white")
btn_calculate.grid(row=2, columnspan=2, pady=20)

# Create a label to display the result
label_result = tk.Label(root, text="", bg="#f0f4f7", font=("Helvetica", 14, "bold"))
label_result.pack(pady=20)

# Run the application
root.mainloop()
