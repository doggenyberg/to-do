from tkinter import *
import json

# Root
root = Tk()
root.title("Att göra")
root.geometry("320x580")
root.resizable(False, False)

task_list = []


try:
    with open("tasks.json", "r") as outfile:
        json_object = json.load(outfile)
        task_list = json_object

except FileNotFoundError:
    print("'tasks.json' does not exist")


def addTask():
    task = task_entry.get()
    if task == "":
        print("nej")
    else:
        task_entry.delete(0, END)
        task_list.append(task)
        listbox.insert(END, task)
        with open("tasks.json", "w") as outfile:
            outfile.write(json.dumps(task_list))


def deleteTask():
    task = str(listbox.get(ANCHOR))
    if task in task_list:
        task_list.remove(task)
        listbox.delete(ANCHOR)

        with open("tasks.json", "w") as outfile:
            outfile.write(json.dumps(task_list))


# Icon
image_icon = PhotoImage(file="img_lib/task.png")
root.iconphoto(False, image_icon)


# Top bar
top_image= PhotoImage(file="img_lib/topbar.png")
Label(root, image=top_image).pack()


# Note image
note_image = PhotoImage(file="img_lib/task.png")
Label(root, image=note_image, bg="#32405b"). place(x=170, y=20)


# Header
header = Label(root, text="ATT GÖRA", font="Arial 20 bold", fg="White", bg="#32405b").place(x=10, y=20)


# Main
frame = Frame(root, width=320, height=50, bg="#d1d1d1")
frame.place(x=0, y=90)

task = StringVar()
task_entry = Entry(frame, width=24, font="Calibri 14", bd=0)
task_entry.place(x=10, y=12)
task_entry.focus()

add_button = Button(frame, text="+", font="Arial 14", fg="White", bg="#657ba6", width=2, height=0, bd=2, command=addTask)
add_button.place(x=270, y=5)


# Listbox
list_frame = Frame(root, bd=3, width=520, height=900, bg="white")
list_frame.place(x=12, y=160)

listbox = Listbox(list_frame, font="arial 12", width=30, height=16, bg="white", cursor="hand2", bd=0)
listbox.pack(side=LEFT, fill=BOTH)

scrollbar = Scrollbar(list_frame)
scrollbar.pack(side=RIGHT, fill=BOTH)

listbox.config(yscrollcommand=scrollbar.set)
scrollbar.config(command=listbox.yview)


# Delete button
delete_icon = PhotoImage(file="img_lib/delete.png")
Button(root, image=delete_icon, bd=0, command=deleteTask).pack(side=BOTTOM, pady=20)


# Update list & sort
for task in task_list:
    listbox.insert(END, task)


# Mainloop
root.mainloop()