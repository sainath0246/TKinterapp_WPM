import random
import time
from tkinter import *

global checker, start, T, Label_2, Label_3, st_d_2, st_d_5, string_list
import pandas as pd
import re
import random

df = pd.read_csv('texts_typing.csv', encoding='cp1252')
df = df.dropna()
l = df['Text']


def start_configuring():
    global start, checker, T, Label_2, Label_3, st_d_2, st_d_5, string_list
    start = time.time()
    st = random.choice(l)
    print(st)
    print(len(st))
    st_2 = st.split(' ')
    print(len(st_2))
    st_d_1 = st[0:100]
    st_d_2 = st[100:200]
    st_d_3 = st[200:300]
    st_d_4 = st[300:400]
    print(st_d_1)
    print(st_d_2)
    print(st_d_3)
    print(st_d_4)
    if len(st) > 500:
        st_d_5 = st[400:500]
        print(st_d_5)
    Label_2 = Label(text=f"{st_d_1} ", font=('Arial', 12, 'normal'), fg='green')
    Label_2.grid(row=2, column=1)
    Label_3 = Label(text=f"{st_d_2} ", font=('Arial', 12, 'normal'), fg='green')
    Label_3.grid(row=3, column=1)
    Label_4 = Label(text=f"{st_d_3} ", font=('Arial', 12, 'normal'), fg='green')
    Label_4.grid(row=4, column=1)
    Label_4 = Label(text=f"{st_d_4} ", font=('Arial', 12, 'normal'), fg='green')
    Label_4.grid(row=5, column=1)
    if len(st) > 500:
        Label_4 = Label(text=f"{st_d_5} ", font=('Arial', 12, 'normal'), fg='green')
        Label_4.grid(row=6, column=1)
    # Add a text in Canvas
    label.config(text=f" ", font=('Arial', 25, 'normal'), fg='green')
    start_calculating_button = Button(text="calculate_Typing_speed", command=start_calculating)
    start_calculating_button.grid(row=12, column=1)
    if len(st) < 500:
        st_new = st[:len(st)]
    else:
        st_new = st[:500]
    with open(file='info.txt', mode='w') as f:
        f.writelines(st_new)
    string_list = st_new.split(' ')

    T = Text(windows, height=6, width=70)
    T.grid(row=8, column=1)


def start_calculating():
    global checker, start, string_list
    checker = T.get("1.0", 'end-1c')

    if checker == "":
        label.config(text=f"Type before you check. Press 'type or retype button' ", font=('Arial', 25, 'normal'),
                     fg='green')
    else:
        end = time.time()
        time_taken = end - start
        time_taken_min = time_taken / 60
        checker_words = checker.split(' ')
        print(f"{string_list}\n{len(string_list)}")
        print(f"{checker_words}\n{len(checker_words)}")
        count = 0
        g=[]
        for i in checker_words:
            if i in string_list:
                count += 1
            else:
                g.append(i)
        accuracy = (count / len(string_list)) * 100
        print(accuracy)
        accuracy_rounded = round(accuracy)
        typing_speed = round(len(checker_words) / time_taken_min)
        print(f"The typing speed is {round(len(checker_words) / time_taken_min)} words per minute")
        label.config(text=f"You typing speed is {typing_speed} WPM and accuracy of {accuracy_rounded} if you want to "
                          f"check"
                          f"again press type or retype ",
                     font=('Arial', 16, 'normal'), fg='blue')
        label_10 = Label(text=f"Wrong words you typed are : {g} ", fg='red', font=('Arial', 20))
        label_10.grid(row=21, column=1)


windows = Tk()
windows.title("Password Manager")
windows.config(padx=20, pady=20)
canvas = Canvas(height=300, width=300)
logo_image = PhotoImage(file="typing.png")
canvas.create_image(150, 150, image=logo_image)
canvas.grid(row=0, column=1)
label = Label(text="Text:", fg='red', font=('Arial', 20))
label.grid(row=8, column=0)
inputtxt = Entry(width=100)
calculate_WPM = Button(text="Press to Type or retype", command=start_configuring)
calculate_WPM.grid(row=10, column=1)
label = Label(text="", fg='green', font=('Arial', 20))
label.grid(row=20, column=1)

windows.mainloop()
