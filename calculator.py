import tkinter as tk
def convert(list1):
    string=""
    for ele in list1:
        string+=ele
    return string
expression=[]
def operations(symbol):
    global expression
    expression.append(str(symbol))
    resultfield.delete(1.0,tk.END)
    resultfield.insert(1.0,convert(expression))

def clearing():
    global expression
    expression=[]
    resultfield.delete("1.0",tk.END)
def evaluate():
    global expression
    try:
        result=str(eval(convert(expression)))
        expression=list(result)
        resultfield.delete("1.0",tk.END)
        resultfield.insert("1.0",result)
    except ZeroDivisionError:
        clearing()
        resultfield.insert("1.0","ERROR")
def delete():
    global expression
    expression.pop()
    resultfield.delete(1.0,tk.END)
    resultfield.insert(1.0,convert(expression))



root=tk.Tk()
root.geometry("444x400")
root.configure(bg="black")
resultfield=tk.Text(root,bg="black",fg="white",height=2,width=20,font=("Arial",30))
resultfield.grid(columnspan=5)
btn1=tk.Button(root,text="1",bd=0,bg="black",fg="white",command=lambda:operations(1),width=5,font=("arial",16))
btn1.grid(row=4,column=1)
btn2=tk.Button(root,text="2",bd=0,bg="black",fg="white",command=lambda:operations(2),width=5,font=("arial",16))
btn2.grid(row=4,column=2)
btn3=tk.Button(root,text="3",bd=0,bg="black",fg="white",command=lambda:operations(3),width=5,font=("arial",16))
btn3.grid(row=4,column=3)
btn4=tk.Button(root,text="4",bd=0,bg="black",fg="white",command=lambda:operations(4),width=5,font=("arial",16))
btn4.grid(row=3,column=1)
btn5=tk.Button(root,text="5",bd=0,bg="black",fg="white",command=lambda:operations(5),width=5,font=("arial",16))
btn5.grid(row=3,column=2)
btn6=tk.Button(root,text="6",bd=0,bg="black",fg="white",command=lambda:operations(6),width=5,font=("arial",16))
btn6.grid(row=3,column=3)
btn7=tk.Button(root,text="7",bd=0,bg="black",fg="white",command=lambda:operations(7),width=5,font=("arial",16))
btn7.grid(row=2,column=1)
btn8=tk.Button(root,text="8",bd=0,bg="black",fg="white",command=lambda:operations(8),width=5,font=("arial",16))
btn8.grid(row=2,column=2)
btn9=tk.Button(root,text="9",bd=0,bg="black",fg="white",command=lambda:operations(9),width=5,font=("arial",16))
btn9.grid(row=2,column=3)
btn0=tk.Button(root,text="0",bd=0,bg="black",fg="white",command=lambda:operations(0),width=5,font=("arial",16))
btn0.grid(row=5,column=2)
btnp1=tk.Button(root,text="(",bd=0,bg="black",fg="white",command=lambda:operations("("),width=5,font=("arial",16))
btnp1.grid(row=5,column=1)
btnp2=tk.Button(root,text=")",bd=0,bg="black",fg="white",command=lambda:operations(")"),width=5,font=("arial",16))
btnp2.grid(row=5,column=3)

btnadd=tk.Button(root,text="+",bd=0,bg="black",fg="#FF7A33",command=lambda:operations("+"),width=5,font=("arial",20))
btnadd.grid(row=2,column=4)
btnsub=tk.Button(root,text="-",bd=0,bg="black",fg="#FF7A33",command=lambda:operations("-"),width=5,font=("arial",20))
btnsub.grid(row=3,column=4)
btnmult=tk.Button(root,text="x",bd=0,bg="black",fg="#FF7A33",command=lambda:operations("*"),width=5,font=("arial",20))
btnmult.grid(row=4,column=4)
btndiv=tk.Button(root,text="÷",bd=0,bg="black",fg="#FF7A33",command=lambda:operations("/"),width=5,font=("arial",20))
btndiv.grid(row=5,column=4)
btnpercent=tk.Button(root,text="%",bd=0,bg="black",fg="#FF7A33",command=lambda:operations("/100"),width=5,font=("arial",20))
btnpercent.grid(row=6,column=3)



btnclear=tk.Button(root,text="C",bd=0,bg="black",fg="#FF7A33",command=clearing,width=5,font=("arial",20))
btnclear.grid(row=6,column=1)
btnequal=tk.Button(root,text="=",bd=0,bg="#FF7A33",fg="white",command=evaluate,width=5,font=("arial",20))
btnequal.grid(row=6,column=4)
btndel=tk.Button(root,text="Del",bd=0,bg="black",fg="#FF7A33",command=delete,width=5,font=("arial",20))
btndel.grid(row=6,column=2)



root.mainloop()

