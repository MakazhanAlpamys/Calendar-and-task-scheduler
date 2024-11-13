
import tkinter as tk
from tkinter import ttk

def add_task():
    minute = entry_minute.get()
    hour = entry_hour.get()
    day = entry_day.get()
    month = entry_month.get()
    task = entry_task.get()

    if minute and hour and day and month and task:
        task_info = f"{minute} мин, {hour} сағ, {day} күн, {month} ай - {task}"
        task_listbox.insert(tk.END, task_info)

        entry_minute.delete(0, tk.END)
        entry_hour.delete(0, tk.END)
        entry_day.delete(0, tk.END)
        entry_month.delete(0, tk.END)
        entry_task.delete(0, tk.END)

root = tk.Tk()
root.title("Күнтізбе және тапсырмаларды жоспарлаушы")
root.geometry("600x400")

frame_inputs = tk.Frame(root)
frame_inputs.pack(pady=10)

tk.Label(frame_inputs, text="Минута (0-59):").grid(row=0, column=0, padx=5, pady=5)
entry_minute = tk.Entry(frame_inputs, width=5)
entry_minute.grid(row=0, column=1, padx=5, pady=5)

tk.Label(frame_inputs, text="Сағат (0-23):").grid(row=0, column=2, padx=5, pady=5)
entry_hour = tk.Entry(frame_inputs, width=5)
entry_hour.grid(row=0, column=3, padx=5, pady=5)

tk.Label(frame_inputs, text="Күн (1-31):").grid(row=1, column=0, padx=5, pady=5)
entry_day = tk.Entry(frame_inputs, width=5)
entry_day.grid(row=1, column=1, padx=5, pady=5)

tk.Label(frame_inputs, text="Ай (1-12):").grid(row=1, column=2, padx=5, pady=5)
entry_month = tk.Entry(frame_inputs, width=5)
entry_month.grid(row=1, column=3, padx=5, pady=5)

tk.Label(frame_inputs, text="Тапсырма:").grid(row=2, column=0, padx=5, pady=5)
entry_task = tk.Entry(frame_inputs, width=30)
entry_task.grid(row=2, column=1, columnspan=3, padx=5, pady=5)

add_button = tk.Button(root, text="Қосу", command=add_task)
add_button.pack(pady=10)

task_listbox = tk.Listbox(root, width=80, height=10)
task_listbox.pack(pady=10)

def delete_task():
    selected_task_index = task_listbox.curselection()
    if selected_task_index:
        task_listbox.delete(selected_task_index)

delete_button = tk.Button(root, text="Таңдалған тапсырманы өшіру", command=delete_task)
delete_button.pack(pady=5)

root.mainloop()
