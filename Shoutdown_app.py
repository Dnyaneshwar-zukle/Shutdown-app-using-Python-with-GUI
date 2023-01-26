from tkinter import *
import os

def restart():
    os.system("shoutdown /r /t 1")
def retsrat_time():
    os.system("shoutdown /r /t 20")
def logout():
    os.system("shoutdown -1")
def shoutdown():
      os.system("shoutdown /s /t 1")   
      
st = Tk()
st.title("ShoutDown App")
st.geometry("500x500")
st.config(bg="blue")

r_button = Button(st, text="Restart",font=("Time New Roman",30,"bold"),
                   relief=RAISED,cursor="plus",command=restart)
r_button.place(x=150,y=60,height=50,width=200)

rt_button = Button(st, text="Restart time",font=("Time New Roman",20,"bold"),
                   relief=RAISED,cursor="plus",command=retsrat_time)
rt_button.place(x=150,y=170,height=50,width=200)

lg_button = Button(st, text="Log Out",font=("Time New Roman",20,"bold"),
                                            relief=RAISED,cursor="plus",command=logout)
lg_button.place(x=150,y=270,height=50,width=200)

lgl_button = Button(st, text="ShoutDown",font=("Time New Roman",20,"bold"),
                                                relief=RAISED,cursor="plus",command=shoutdown)
lgl_button.place(x=150,y=370,height=50,width=200)

st.mainloop()