import tkinter as tk
from tkinter import ttk, simpledialog

class ToDoApp:
    def __init__(self, master):
        self.master = master
        master.title("To-Do App")

        # Create frames for different sections
        self.todo_frame = tk.Frame(master, bg="lightgray")
        self.sort_frame = tk.Frame(master, bg="lightgray")
        self.done_frame = tk.Frame(master, bg="lightgray")

        # Create labels for each section
        self.todo_label = tk.Label(self.todo_frame, text="To Do", font=("Arial", 14), bg="lightgray")
        self.sort_label = tk.Label(self.sort_frame, text="Sort", font=("Arial", 14), bg="lightgray")
        self.done_label = tk.Label(self.done_frame, text="Done", font=("Arial", 14), bg="lightgray")

        # Create a listbox to display to-do items
        self.todo_listbox = tk.Listbox(self.todo_frame, width=30, height=10, selectmode=tk.SINGLE)

        # Create a button to add a new to-do item
        self.add_button = tk.Button(self.todo_frame, text="Add Task", command=self.add_task)

        # Create a button to delete a to-do item
        self.delete_button = tk.Button(self.todo_frame, text="Delete Task", command=self.delete_task)

        # Create a label to display the number of tasks
        self.task_count_label = tk.Label(self.todo_frame, text=f"Tasks: {self.todo_listbox.size()}", font=("Arial", 10), bg="lightgray")

        # Create a combobox to sort to-do items
        self.sort_combobox = ttk.Combobox(self.sort_frame, values=["Priority", "Alphabetical", "Date"], state="readonly")
        self.sort_combobox.current(0)  # Default to "Priority"

        # Create a listbox to display done tasks
        self.done_listbox = tk.Listbox(self.done_frame, width=30, height=10)

        # Create a stack to hold completed tasks
        self.completed_tasks = []

        # Layout using grid
        self.todo_frame.grid(row=0, column=0, padx=10, pady=10)
        self.sort_frame.grid(row=0, column=1, padx=10, pady=10)
        self.done_frame.grid(row=0, column=2, padx=10, pady=10)

        # Pack widgets in the to-do frame
        self.todo_label.pack()
        self.todo_listbox.pack()
        self.add_button.pack()
        self.delete_button.pack()
        self.task_count_label.pack()

        # Pack widgets in the sort frame
        self.sort_label.pack()
        self.sort_combobox.pack()

        # Pack widgets in the done frame
        self.done_label.pack()
        self.done_listbox.pack()

        # Bind the combobox selection change to the sorting function
        self.sort_combobox.bind("<<ComboboxSelected>>", self.on_sort_combobox_change)

    def add_task(self):
        task = simpledialog.askstring("Add Task", "Enter task name:")
        if task:
            self.todo_listbox.insert(tk.END, task)
            self.update_task_count()

    def delete_task(self):
        selected_task_index = self.todo_listbox.curselection()
        if selected_task_index:
            task = self.todo_listbox.get(selected_task_index)
            self.todo_listbox.delete(selected_task_index)
            self.completed_tasks.append(task)
            self.done_listbox.insert(tk.END, task)
            self.update_task_count()

    def update_task_count(self):
        self.task_count_label.config(text=f"Tasks: {self.todo_listbox.size()}")

    def sort_tasks(self):
        sort_option = self.sort_combobox.get()
        tasks = list(self.todo_listbox.get(0, tk.END))
        if sort_option == "Priority":
            # Implement a simple priority sorting logic (for demonstration)
            tasks.sort(key=lambda x: (x.split()[1]))  # Assuming task format is "Task X"
        elif sort_option == "Alphabetical":
            tasks.sort()
        elif sort_option == "Date":
            pass  # Placeholder for date sorting logic
        self.todo_listbox.delete(0, tk.END)
        for task in tasks:
            self.todo_listbox.insert(tk.END, task)
        self.update_task_count()  # Update task count after sorting

    def on_sort_combobox_change(self, event):
        self.sort_tasks()

# Complete the main application loop
if __name__ == "__main__":
    root = tk.Tk()
    app = ToDoApp(root)
    root.mainloop()
