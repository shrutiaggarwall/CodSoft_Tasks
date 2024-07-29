from tkinter import *
from tkinter import messagebox

def newTask():
    t= my_entry.get()
    if t!= "":
        lb.insert(END, t)
        my_entry.delete(0, "end")
    else:
        messagebox.showwarning("warning", "Please enter some task.")

def deleteTask():
    lb.delete(ANCHOR)
    
s = Tk()
s.geometry('500x450+500+200')
s.title('My To-Do List')
s.config(bg='#F4D03F')
s.resizable(width=False, height=False)

frame = Frame(s)
frame.pack(pady=10)

lb = Listbox(
    frame,
    width=25,
    height=8,
    font=('Times', 18),
    bd=0,
    fg='#464646',
    highlightthickness=0,
    selectbackground='#a6a6a6',
    activestyle="none",
    
)
lb.pack(side=LEFT, fill=BOTH)

task_list = [
    'write content',
    'watch series',
    'go gym',
    'write documentation',
    'take a nap',
    'Learn something',
    'Write journal',
    'Practice DSA',
    'Dance' 
    ]

for item in task_list:
    lb.insert(END, item)

sb = Scrollbar(frame)
sb.pack(side=RIGHT, fill=BOTH)

lb.config(yscrollcommand=sb.set)
sb.config(command=lb.yview)

my_entry = Entry(
    s,
    font=('times', 24)
    )

my_entry.pack(pady=20)

button_frame = Frame(s)
button_frame.pack(pady=20)

add_btn = Button(
    button_frame,
    text='Add Task',
    font=('times 14'),
    bg='#52BE80',
    padx=20,
    pady=10,
    command=newTask
)
add_btn.pack(fill=BOTH, expand=True, side=LEFT)

delTask_btn = Button(
    button_frame,
    text='Delete Task',
    font=('times 14'),
    bg='#DE3163',
    padx=20,
    pady=10,
    command=deleteTask
)
delTask_btn.pack(fill=BOTH, expand=True, side=LEFT)


s.mainloop()