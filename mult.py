import tkinter as tk

def print_table():
    try:
        number = int(number_entry.get())
        result = ""
        for i in range(1, 11):
            result += f"{number} x {i} = {number * i}\n"
        result_label.config(text=result)
    except ValueError:
        result_label.config(text="Please enter a valid number.")


root = tk.Tk()
root.title("Multiplication Table App")


prompt_label = tk.Label(root, text="Enter a number:")
prompt_label.pack(pady=5)

number_entry = tk.Entry(root)
number_entry.pack(pady=5)

get_table_button = tk.Button(root, text="Get Multiplication Table", command=print_table)
get_table_button.pack(pady=10)

result_label = tk.Label(root, text="", font=("Helvetica", 14), justify=tk.LEFT)
result_label.pack(pady=20)


root.mainloop()
