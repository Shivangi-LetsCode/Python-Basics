# Graphical User Inteface
import tkinter as tk
def save_tasks():
    with open("tasks.txt", "w") as file:
        tasks = task_list.get(0, tk.END)
        for task in tasks:
            file.write(task + "\n")

def add_task():
    task = task_entry.get()
    if task != "":
        task_list.insert(tk.END,task)
        task_entry.delete(0,tk.END)
        save_tasks()
    else:
        tk.messagebox.showwarning("Input Error","Please Enter a Task to Add")
    
def remove_task():
    try:
        selected = task_list.curselection()
        task_list.delete(selected)
    except:
        messagebox.showwarning("Selection Error", "No Task Selected to Delete")
        



# ROOT WINDOW
root = tk.Tk()
root.title("To-Do-List")
root.geometry("400x500")
root.configure(bg="green")

# TASK ENTRY
task_entry = tk.Entry(root, width=30)
task_entry.pack(pady=30)
'''
  pady stands for padding in Y vertical(direction) (top-bottom)
  padx : adds horizontal space (left-right)
'''

add_button = tk.Button(root,text="Add Task", command=add_task)
add_button.pack(pady=5)

task_list = tk.Listbox(root, width=30, height=10)
task_list.pack(pady=20)


delete_button = tk.Button(root,text="Delete Task",command=remove_task)
delete_button.pack(pady=5)

