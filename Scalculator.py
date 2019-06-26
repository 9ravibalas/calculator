from tkinter import *

root =Tk()
root.title('Calculator')
root.configure(bg='darkgray')

def closew(self,event=''):
			exit()


globals()['operator']=''
tv1=StringVar()


def buttonclick(number):	
	globals()['operator']=globals()['operator']+str(number)
	tv1.set(globals()['operator'])

def bclear():
	globals()['operator']=''
	tv1.set(globals()['operator'])

def result():
	if globals()['operator']=="":
		tv1.set("0")
	else:
		s1=eval(globals()['operator'])
		globals()['operator']=str(s1)
	tv1.set(globals()['operator'])
def oneclear():
	globals()['operator']=globals()['operator'][0:len(globals()['operator'])-1]
	tv1.set(globals()['operator'])
	

screen=Entry(root,font=('arial',20,'bold'),bd=30,justify='right',insertwidth=4	,textvariable=tv1).grid(columnspan=4)

bclear=Button(root,text='C',padx=16,pady=16,bg='powder blue',command=bclear,      font=('arial',20,'bold'),bd=10).grid(row=1,column=0)
boneclear=Button(root,text=' <',padx=16,pady=16,bg='powder blue',command=oneclear,font=('arial',20,'bold'),bd=10).grid(row=1,column=1)
mod=Button(root,text='%',padx=16,pady=16,bg='powder blue',command=lambda:buttonclick('%'),font=('arial',20,'bold'),bd=10).grid(row=1,column=2)
b1=Button(root,text='1',padx=16,pady=16,bg='powder blue',command=lambda:buttonclick(1),font=('arial',20,'bold'),bd=10).grid(row=2,column=0)
b2=Button(root,text='2',padx=16,pady=16,bg='powder blue',command=lambda:buttonclick(2),font=('arial',20,'bold'),bd=10).grid(row=2,column=1)
b3=Button(root,text='3',padx=16,pady=16,bg='powder blue',command=lambda:buttonclick(3),font=('arial',20,'bold'),bd=10).grid(row=2,column=2)
b4=Button(root,text='4',padx=16,pady=16,bg='powder blue',command=lambda:buttonclick(4),font=('arial',20,'bold'),bd=10).grid(row=3,column=0)
b5=Button(root,text='5',padx=16,pady=16,bg='powder blue',command=lambda:buttonclick(5),font=('arial',20,'bold'),bd=10).grid(row=3,column=1)
b6=Button(root,text='6',padx=16,pady=16,bg='powder blue',command=lambda:buttonclick(6),font=('arial',20,'bold'),bd=10).grid(row=3,column=2)
b7=Button(root,text='7',padx=16,pady=16,bg='powder blue',command=lambda:buttonclick(7),font=('arial',20,'bold'),bd=10).grid(row=4,column=0)
b8=Button(root,text='8',padx=16,pady=16,bg='powder blue',command=lambda:buttonclick(8),font=('arial',20,'bold'),bd=10).grid(row=4,column=1)
b9=Button(root,text='9',padx=16,pady=16,bg='powder blue',command=lambda:buttonclick(9),font=('arial',20,'bold'),bd=10).grid(row=4,column=2)
b0=Button(root,text='0',padx=16,pady=16,bg='powder blue',command=lambda:buttonclick(0),font=('arial',20,'bold'),bd=10).grid(row=5,column=0)
dot=Button(root,text='.',padx=16,pady=16,bg='powder blue',command=lambda:buttonclick('.'),font=('arial',20,'bold'),bd=10).grid(row=5,column=1)
bans=Button(root,  text='=',padx=32,pady=16,bg='powder blue',command=result,font=('arial',20,'bold'),bd=10).grid(columnspan=2,row=5,column=2)
bplus=Button(root, text='+',padx=16,pady=16,bg='powder blue',command=lambda:buttonclick('+'),font=('arial',20,'bold'),bd=10).grid(row=1,column=3)
bminus=Button(root,text='-',padx=16,pady=16,bg='powder blue',command=lambda:buttonclick('-'),font=('arial',20,'bold'),bd=10).grid(row=2,column=3)
bmul=Button(root,  text='*',padx=16,pady=16,bg='powder blue',command=lambda:buttonclick('*'),font=('arial',20,'bold'),bd=10).grid(row=3,column=3)
bdiv=Button(root,  text='/',padx=16,pady=16,bg='powder blue',command=lambda:buttonclick('/'),font=('arial',20,'bold'),bd=10).grid(row=4,column=3)



root.mainloop()







