from tkinter import *
import os

st = Tk()
st.title("Shoutdown App")
st.geometry("500x500")
st.config(bg="blue")

r_button = Button(st, text="restart",font=("Time New Roman",30,"bold"),relief=RAISED,cursor="plus")
r_button.place(x=200,y=60,height=50,width=200)

st.mainloop()