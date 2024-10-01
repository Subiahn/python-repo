import tkinter
from tkinter import *

window = tkinter.Tk()
window.title("My First GUI Program")
window.minsize(width=500, height=300)

#Label
my_label = tkinter.Label(text="I am a Label", font=("Arial", 24)) #

# 만들고 배치 하기 배치 안하면 안보임 packer 에 대한 설명을 읽어보자
my_label.pack()
my_label["text"] = "New Text"
my_label.config(text="New Text")

# 버튼 만들기

def button_clicked():
    print("I got clicked")
    print(f"I got {input.get()} clicked")
    new_text = input.get()
    my_label.config(text=new_text)


button = tkinter.Button(text="Click Me", command=button_clicked)
button.pack()

# Entry
input = tkinter.Entry(width=10)
input.pack()
input.get()
print(input.get())


# import turtle
# tim = turtle.Turtle()
# tim.write("Some text", font=("Times New Roman", 80, "bold"))

# 맨아래로 !!
window.mainloop()