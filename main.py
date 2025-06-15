import tkinter as tk
import random
def f ():
    a = entry1.get()
    b = Answer1.get()
    c = random.randint(1,3)
    if c == 1 and b == 1:
        label4.configure(text="Draw")
        label5.configure(image=photo)
    elif c == 2 and b == 2:
        label4.configure(text="Draw")
        label5.configure(image=photo1)
    elif c == 3 and b == 3:
        label4.configure(text="Draw")
        label5.configure(image=photo2)
    elif c == 1 and b == 2:
        label4.configure(text="Computer wins!")
        label5.configure(image=photo)
    elif c == 1 and b == 3:
        label4.configure(text=f"{a} won!")
        label5.configure(image=photo)
    elif c == 2 and b == 1:
        label4.configure(text=f"{a} won!")
        label5.configure(image=photo1)
    elif c == 2 and b == 3:
        label4.configure(text="Computer wins!")
        label5.configure(image=photo1)
    elif c == 3 and b == 1:
        label4.configure(text="computer wins!")
        label5.configure(image=photo2)
    elif c == 3 and b == 2:
        label4.configure(text=f"{a} won!")
        label5.configure(image=photo2)
win = tk.Tk()
win.geometry("3000x2000")
win.config(bg="#2BBDBD")
label1 = tk.Label(win, text="Rock Paper Scissors Game", font=("Arial", 50), bg="#26D4D4")
label1.place(relx=0.25, rely=0.1)
label2 = tk.Label(win, text="Choose an option", font=("Arial", 30), bg="#26D4D4")
label2.place(relx=0.1, rely=0.375)
photo = tk.PhotoImage(file="Paper.png")
label3 = tk.Label(win, text="Enter a Username", font=("Arial", 30), bg="#26D4D4")
label3.place(relx=0.1, rely=0.225)
label4 = tk.Label(win, font=("Arial", 30), bg="#26D4D4")
label4.place(relx=0.6, rely=0.375)
label5 = tk.Label(win, font=("Arial", 30), bg="#26D4D4")
label5.place(relx=0.7, rely=0.45)
entry1 = tk.Entry(win, font=("Arial", 30))
entry1.place(relx=0.1, rely=0.3)
button1 = tk.Button(win, text="Submit", font=("Arial", 50), bg="#26D4D4", command=f)
button1.place(relx=0.4, rely=0.75)
Answer1 = tk.IntVar()
radio1 = tk.Radiobutton(win, image=photo, value=1, variable=Answer1)
radio1.place(relx=0.1, rely=0.475)
photo1 = tk.PhotoImage(file="Rock.png")
radio2 = tk.Radiobutton(win, image=photo1, value=2, variable=Answer1)
radio2.place(relx=0.25, rely=0.475)
photo2 = tk.PhotoImage(file="Scissors.png")
radio3 = tk.Radiobutton(win, image=photo2, value=3, variable=Answer1)
radio3.place(relx=0.4, rely=0.475)
win.mainloop()