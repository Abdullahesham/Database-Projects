#import tkinter
from tkinter  import *
import sqlite3

conn = sqlite3.connect("db.db")
c = conn.cursor()
c.execute("CREATE TABLE IF NOT EXISTS t(id INT PRIMARY KEY,Name TEXT,grade REAL)")

root =Tk()
root.geometry("400x200+200+200") #width * height + left + top
root.title("DB Lab")


Tops = Frame(root, width = 300 , height = 100)
Tops.pack(side = TOP)

f1 = Frame(root, width = 300 ,height = 200)
f1.pack(side = LEFT )

f2 = Frame(root, width = 200 ,height = 200)
f2.pack(side = RIGHT)

lbl = Label(Tops, font =('arial',30,'bold'), text ="DB Lab",  bd =10 , anchor = 'w')
lbl.grid(row=0,column = 0)

lbl1 = Label(f1, font =('arial',10,'bold'), text ="ID",  bd =10 , anchor = 'w')
lbl1.grid(row=0,column = 0)
lbl2 = Label(f1, font =('arial',10,'bold'), text ="Name",  bd =10 , anchor = 'w')
lbl2.grid(row=1,column = 0)
lbl3 = Label(f1, font =('arial',10,'bold'), text ="Grade",  bd =10 , anchor = 'w')
lbl3.grid(row=2,column = 0)

txt1 = Entry(f1,font =('arial',10,'bold'))
txt1.grid(row=0, column = 1)

txt2 = Entry(f1,font =('arial',10,'bold'))
txt2.grid(row=1, column = 1)

txt3 = Entry(f1,font =('arial',10,'bold'))
txt3.grid(row=2, column = 1)

def callback1():    
    try:
        c.execute("INSERT INTO t VALUES("+txt1.get()+",'"+txt2.get()+"','"+txt3.get()+"')")
        conn.commit()
    except:
        print("INSERT INTO t VALUES("+txt1.get()+",'"+txt2.get()+"','"+txt3.get()+"')")  
        print("Failed to insert")

def callback2():    
    try:
        c.execute("UPDATE t SET grade = "+txt3.get()+" WHERE id = "+txt1.get()+"")
        conn.commit()
    except:
        print("UPDATE t SET grade = "+txt3.get()+" WHERE id = "+txt1.get()+"")  
        print("Failed to update")


def callback3():    
    try:
        c.execute("DELETE FROM t WHERE id ="+ txt1.get()+"")
        conn.commit()
    except:
        print("DELETE FROM t WHERE id ="+ txt1.get()+"")  
        print("Failed to delete")
        
b1=Button(f2,command=callback1,text="Insert",width = 10).grid(row=0)
b2=Button(f2,command=callback2,text="Update",width = 10).grid(row=1)
b3=Button(f2,command=callback3,text="Delete",width = 10).grid(row=2)

root.mainloop()
c.close()
conn.close()
