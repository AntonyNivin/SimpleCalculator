import tkinter as tk
import tkinter.font as font
def on_click(num):
    global expr
    expr=expr+str(num)
    input_text.set(expr)
def dis_clear():
    global expr
    clearscreen=" "
    input_text.set(clearscreen)
    expr=" "
def dis_total():
    try:
        global expr
        result=str(eval(expr))
        input_text.set(result)
        expr=" "
    except:
        input_text.set('error')
        expr=" "
expr=""
root =tk.Tk()
buttonFont = font.Font(family='questrial', size=20, weight='bold')
root['background']='black'
root.title("calculator")
root.geometry('400x650')
frame1=tk.Frame(root,bd=5,bg='#3090C7',height=100)
frame1.pack(side='top',fill='both')
frame2=tk.Frame(root,bd=5,bg='lightblue')
frame2.pack(side='top',expand=True,fill='both')
frame1.rowconfigure(tuple(range(1)), weight=1)
frame1.columnconfigure(tuple(range(1)), weight=1)

frame2.columnconfigure(tuple(range(4)), weight=1)
frame2.rowconfigure(tuple(range(4)), weight=1)
input_text=tk.StringVar()
caldisplay=tk.Entry(frame1,justify='right',font=('calibre',30,'normal'),textvariable=input_text)
caldisplay.grid(column=0,row=0,sticky='news',ipady=40)
btn1=tk.Button(frame2,text='1',bd=4,font=buttonFont,bg='white',command=lambda:on_click("1"))
btn1.grid(column=0, row=0, sticky="news")
btn2=tk.Button(frame2,text='2',bd=4,font=buttonFont,bg='white',command=lambda:on_click("2"))
btn2.grid(column=1, row=0, sticky="news")
btn3=tk.Button(frame2,text='3',bd=4,font=buttonFont,bg='white',command=lambda:on_click("3"))
btn3.grid(column=2, row=0, sticky="news")
btnadd=tk.Button(frame2,text='+',bd=4,font=buttonFont,bg='light yellow',command=lambda:on_click("+"))
btnadd.grid(column=3, row=0, sticky="news")
btn4=tk.Button(frame2,text='4',bd=4,font=buttonFont,bg='white',command=lambda:on_click("4"))
btn4.grid(column=0, row=1, sticky="news")
btn5=tk.Button(frame2,text='5',bd=4,font=buttonFont,bg='white',command=lambda:on_click("5"))
btn5.grid(column=1, row=1, sticky="news")
btn6=tk.Button(frame2,text='6',bd=4,font=buttonFont,bg='white',command=lambda:on_click("6"))
btn6.grid(column=2, row=1, sticky="news")
btnsub=tk.Button(frame2,text='-',bd=4,font=buttonFont,bg='light yellow',command=lambda:on_click("-"))
btnsub.grid(column=3, row=1, sticky="news")
btn7=tk.Button(frame2,text='7',bd=4,font=buttonFont,bg='white',command=lambda:on_click("7"))
btn7.grid(column=0, row=2, sticky="news")
btn8=tk.Button(frame2,text='8',bd=4,font=buttonFont,bg='white',command=lambda:on_click("8"))
btn8.grid(column=1, row=2, sticky="news")
btn9=tk.Button(frame2,text='9',bd=4,font=buttonFont,bg='white',command=lambda:on_click("9"))
btn9.grid(column=2, row=2, sticky="news")
btnmul=tk.Button(frame2,text='x',bd=4,font=buttonFont,bg='light yellow',command=lambda:on_click("*"))
btnmul.grid(column=3, row=2, sticky="news")
btnclear=tk.Button(frame2,text='C',bd=4,font=buttonFont,bg='#98AFC7',command=lambda:dis_clear())
btnclear.grid(column=0, row=3, sticky="news")
btn0=tk.Button(frame2,text='0',bd=4,font=buttonFont,bg='white',command=lambda:on_click("0"))
btn0.grid(column=1, row=3, sticky="news")
btnequal=tk.Button(frame2,text='=',bd=4,font=buttonFont,bg='light yellow',command=lambda:dis_total())
btnequal.grid(column=2, row=3, sticky="news")
btndiv=tk.Button(frame2,text='÷',bd=4,font=buttonFont,bg='light yellow',command=lambda:on_click("/"))
btndiv.grid(column=3, row=3, sticky="news")
root.mainloop()
