from tkinter import*

def gombkat(numbers) :
    global operator
    operator=operator + str(numbers)
    text_input.set(operator)

def törlés():
    global operator
    operator=""
    text_input.set("")

def eredmény():
    global operator
    sumup=str(eval(operator))
    text_input.set(sumup)
    operator=""

cal = Tk()
cal.title("Szamologep")
operator=""
text_input =StringVar()

Entry(cal,font=('arial', 20 ,'bold'),textvariable=text_input,bd=30,insertwidth=4,
    bg='powder blue', justify='right').grid(columnspan=4)



gomb7=Button(cal,padx=16,bd=8, fg="black", font=('arial', 20 ,'bold'),
            text="7", command=lambda:gombkat(7), bg='gray').grid(row=1,column=0)

gomb8=Button(cal,padx=16,bd=8, fg="black", font=('arial', 20 ,'bold'),
            text="8", command=lambda:gombkat(8),bg='gray').grid(row=1,column=1)

gomb9=Button(cal,padx=16,bd=8, fg="black", font=('arial', 20 ,'bold'),
            text="9", command=lambda:gombkat(9),bg='gray').grid(row=1,column=2)

Összeadás=Button(cal,padx=16,bd=8, fg="black", font=('arial', 20 ,'bold'),
            text="+", command=lambda:gombkat("+"),bg='gray').grid(row=1,column=3)

#---------------MÁSODIK SOR--------------------


gomb4=Button(cal,padx=16,bd=8, fg="black", font=('arial', 20 ,'bold'),
            text="4", command=lambda:gombkat(4),bg='gray').grid(row=2,column=0)

gomb5=Button(cal,padx=16,bd=8, fg="black", font=('arial', 20 ,'bold'),
            text="5", command=lambda:gombkat(5),bg='gray').grid(row=2,column=1)

gomb6=Button(cal,padx=16,bd=8, fg="black", font=('arial', 20 ,'bold'),
            text="6", command=lambda:gombkat(6),bg='gray').grid(row=2,column=2)

Kivonás=Button(cal,padx=16,bd=8, fg="black", font=('arial', 20 ,'bold'),
            text="-", command=lambda:gombkat("-"),bg='gray').grid(row=2,column=3)


#---------------HARMADIK SOR--------------------


gomb1=Button(cal,padx=16,bd=8, fg="black", font=('arial', 20 ,'bold'),
            text="1", command=lambda:gombkat(1),bg='gray').grid(row=3,column=0)

gomb2=Button(cal,padx=16,bd=8, fg="black", font=('arial', 20 ,'bold'),
            text="2", command=lambda:gombkat(2),bg='gray').grid(row=3,column=1)

gomb3=Button(cal,padx=16,bd=8, fg="black", font=('arial', 20 ,'bold'),
            text="3", command=lambda:gombkat(3),bg='gray').grid(row=3,column=2)

szorzás=Button(cal,padx=16,bd=8, fg="black", font=('arial', 20 ,'bold'),
            text="*", command=lambda:gombkat("*"),bg='gray').grid(row=3,column=3)

#---------------NEGYEDIK SOR--------------------


gomb0=Button(cal,padx=16, pady=16, bd=8, fg="black", font=('arial', 20 ,'bold'),
            text="0", command=lambda:gombkat(0),bg='gray').grid(row=4,column=0)

törlés=Button(cal,padx=16, pady=16, bd=8, fg="black", font=('arial', 20 ,'bold'),
            text="C", command= törlés, bg='gray').grid(row=4,column=1)

egyenlő=Button(cal,padx=16, pady=16,bd=8, fg="black", font=('arial', 20 ,'bold'),
            text="=", command=eredmény,bg='gray').grid(row=4,column=2)

osztás=Button(cal,padx=16,pady=16, bd=8, fg="black", font=('arial', 20 ,'bold'),
            text="/", command=lambda:gombkat("/"),bg='gray').grid(row=4,column=3)


cal.mainloop()

