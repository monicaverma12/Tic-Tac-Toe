from tkinter import*
from tkinter import messagebox


tk = Tk()
tk.title("TIC- TAC- TOE")
#tk.geometry("288x480")
#tk.config(bg = "#1da6ab")
count = 0
turn = True
#disable all buttons

def disable_all_buttons():
  b1.config(state=DISABLED)
  b2.config(state=DISABLED)
  b3.config(state=DISABLED)
  b4.config(state=DISABLED)
  b5.config(state=DISABLED)
  b6.config(state=DISABLED)
  b7.config(state=DISABLED)
  b8.config(state=DISABLED)
  b9.config(state=DISABLED)

# check to see if someone won
def checkifwon():
  global winner, win
  winner = False
  if b1["text"]== b2["text"]  and b2["text"] == b3["text"] and b1["text"]!= " ":
    b1.config(bg="red")
    b2.config(bg="red")
    b3.config(bg="red")
    winner = True
    win = b1["text"]
    messagebox.showinfo("tic tak toe", "CONGRATUALTIONS! "+win+" Wins!!")
    disable_all_buttons()
  elif b4["text"]== b5["text"]  and b5["text"] == b6["text"]and b4["text"]!= " ":
    b4.config(bg="red")
    b5.config(bg="red")
    b6.config(bg="red")
    winner = True
    win = b4["text"]
    messagebox.showinfo("tic tak toe", "CONGRATUALTIONS! "+win+" Wins!!")
    disable_all_buttons()
  elif b7["text"]== b8["text"]  and b8["text"] == b9["text"]and b7["text"]!= " ":
    b7.config(bg="red")
    b8.config(bg="red")
    b9.config(bg="red")
    winner = True
    win = b7["text"]
    messagebox.showinfo("tic tak toe", "CONGRATUALTIONS! "+win+" Wins!!")
    disable_all_buttons()
  elif b1["text"]== b4["text"]  and b4["text"] == b7["text"]and b1["text"]!= " ":
    b1.config(bg="red")
    b4.config(bg="red")
    b7.config(bg="red")
    winner = True
    win = b1["text"]
    messagebox.showinfo("tic tak toe", "CONGRATUALTIONS! "+win+" Wins!!")
    disable_all_buttons()
  elif b2["text"]== b5["text"]  and b5["text"] == b8["text"]and b2["text"]!= " ":
    b2.config(bg="red")
    b5.config(bg="red")
    b8.config(bg="red")
    winner = True
    win = b2["text"]
    messagebox.showinfo("tic tak toe", "CONGRATUALTIONS! "+win+" Wins!!")
    disable_all_buttons()
  elif b3["text"]== b6["text"]  and b6["text"] == b9["text"]and b3["text"]!= " ":
    b3.config(bg="red")
    b6.config(bg="red")
    b9.config(bg="red")
    winner = True
    win = b3["text"]
    messagebox.showinfo("tic tak toe", "CONGRATUALTIONS! "+win+" Wins!!")
    disable_all_buttons()
  elif b1["text"]== b5["text"]  and b5["text"] == b9["text"]and b1["text"]!= " ":
    b1.config(bg="red")
    b5.config(bg="red")
    b9.config(bg="red")
    winner = True
    win = b1["text"]
    messagebox.showinfo("tic tak toe", "CONGRATUALTIONS! "+win+" Wins!!")
    disable_all_buttons()
  elif b7["text"]== b5["text"]  and b5["text"] == b3["text"]and b3["text"]!= " ":
    b7.config(bg="red")
    b5.config(bg="red")
    b3.config(bg="red")
    win = b3["text"]
    winner = True
    messagebox.showinfo("tic tak toe", "CONGRATUALTIONS! "+win+" Wins!!")
    disable_all_buttons()



# button click filter
def b_click(b):
  global count,turn
  if b["text"]== " " and turn == True:
    b["text"]= "X"
    turn = False
    count += 1
 
  elif b["text"]== " " and turn == False:
    b["text"]= "O"
    turn = True
    count += 1

  else:
    messagebox.showerror("Tic tak toe","you cannotselect this place")
  checkifwon()
  


def reset():
  global b1,b2,b3,b4,b5,b6,b7,b8,b9
  global count,turn
  count = 0
  turn = True
    # build buttons
  b1 = Button(tk,text=" ",height=3, width=6, bg="white",command=lambda: b_click(b1))
  b2 = Button(tk,text=" ",height=3, width=6, bg="white",command=lambda: b_click(b2))
  b3 = Button(tk,text=" ",height=3, width=6, bg="white",command=lambda: b_click(b3))

  b4 = Button(tk,text=" ",height=3, width=6, bg="white",command=lambda: b_click(b4))
  b5 = Button(tk,text=" ",height=3, width=6, bg="white",command=lambda: b_click(b5))
  b6 = Button(tk,text=" ",height=3, width=6, bg="white",command=lambda: b_click(b6))

  b7 = Button(tk,text=" ",height=3, width=6, bg="white",command=lambda: b_click(b7))
  b8 = Button(tk,text=" ",height=3, width=6, bg="white",command=lambda: b_click(b8))
  b9 = Button(tk,text=" ",height=3, width=6, bg="white",command=lambda: b_click(b9))

#Grid our buttons

  b1.grid(row=0, column=0)
  b2.grid(row=0, column=1)
  b3.grid(row=0, column=2)

  b4.grid(row=1, column=0)
  b5.grid(row=1, column=1)
  b6.grid(row=1, column=2)

  b7.grid(row=2, column=0)
  b8.grid(row=2, column=1)
  b9.grid(row=2, column=2)




my_menu = Menu(tk)
tk.config(menu=my_menu)

options_menu = Menu(my_menu)
my_menu.add_cascade(label = "options", menu=options_menu)
options_menu.add_command(label="Reset", command = reset)

reset()


tk.mainloop()
