import tkinter as tk

app = tk.Tk()
app.geometry("300x350")

app.config(background ="#000000")
app.title("Calculator")
equation =""

def show(value):
    global equation
    equation +=value
    label_result.config(text=equation)

def clear():
        global equation
        equation =""
        label_result.config(text=equation)

def calculate():
    global equation
    result=""
    if equation !="":
        try:
            result=eval(equation)

        except:
            result="error"
            equation =""

        result=round(result,2)
    label_result.config(text=result)


label_result = tk.Label(app,width=300,height=2,text ="",font=("arial",30))
label_result.pack()
tk.Button(app,text="C",width=5,height=1,font=("arial",15,"bold"),bd=1,fg="#fff",bg="#3697f5",command=lambda:clear()).place(x=5,y=100)
tk.Button(app,text="/",width=5,height=1,font=("arial",15,"bold"),bd=1,fg="#fff",bg="#262525",command=lambda:show("/")).place(x=80,y=100)
tk.Button(app,text="%",width=5,height=1,font=("arial",15,"bold"),bd=1,fg="#fff",bg="#262525",command=lambda:show("%")).place(x=155,y=100)
tk.Button(app,text="*",width=5,height=1,font=("arial",15,"bold"),bd=1,fg="#fff",bg="#262525",command=lambda:show("*")).place(x=230,y=100)

tk.Button(app,text="7",width=5,height=1,font=("arial",15,"bold"),bd=1,fg="#fff",bg="#262525",command=lambda:show("7")).place(x=5,y=150)
tk.Button(app,text="8",width=5,height=1,font=("arial",15,"bold"),bd=1,fg="#fff",bg="#262525",command=lambda:show("8")).place(x=80,y=150)
tk.Button(app,text="9",width=5,height=1,font=("arial",15,"bold"),bd=1,fg="#fff",bg="#262525",command=lambda:show("9")).place(x=155,y=150)
tk.Button(app,text="-",width=5,height=1,font=("arial",15,"bold"),bd=1,fg="#fff",bg="#262525",command=lambda:show("-")).place(x=230,y=150)

tk.Button(app,text="4",width=5,height=1,font=("arial",15,"bold"),bd=1,fg="#fff",bg="#262525",command=lambda:show("4")).place(x=5,y=200)
tk.Button(app,text="5",width=5,height=1,font=("arial",15,"bold"),bd=1,fg="#fff",bg="#262525",command=lambda:show("5")).place(x=80,y=200)
tk.Button(app,text="6",width=5,height=1,font=("arial",15,"bold"),bd=1,fg="#fff",bg="#262525",command=lambda:show("6")).place(x=155,y=200)
tk.Button(app,text="+",width=5,height=1,font=("arial",15,"bold"),bd=1,fg="#fff",bg="#262525",command=lambda:show("+")).place(x=230,y=200)

tk.Button(app,text="1",width=5,height=1,font=("arial",15,"bold"),bd=1,fg="#fff",bg="#262525",command=lambda:show("1")).place(x=5,y=250)
tk.Button(app,text="2",width=5,height=1,font=("arial",15,"bold"),bd=1,fg="#fff",bg="#262525",command=lambda:show("2")).place(x=80,y=250)
tk.Button(app,text="3",width=5,height=1,font=("arial",15,"bold"),bd=1,fg="#fff",bg="#262525",command=lambda:show("3")).place(x=155,y=250)
tk.Button(app,text="0",width=10,height=1,font=("arial",15,"bold"),bd=1,fg="#fff",bg="#262525",command=lambda:show("0")).place(x=5,y=300)

tk.Button(app,text="0",width=11,height=1,font=("arial",15,"bold"),bd=1,fg="#fff",bg="#262525",command=lambda:show("0")).place(x=5,y=300)
tk.Button(app,text=".",width=5,height=1,font=("arial",15,"bold"),bd=1,fg="#fff",bg="#262525",command=lambda:show(".")).place(x=155,y=300)

tk.Button(app,text="=",width=5,height=3,font=("arial",15,"bold"),bd=1,fg="#fff",bg="#f58a42",command=lambda:calculate()).place(x=230,y=250)


app.mainloop()



