from tkinter import*
from reportlab.lib.units import inch,cm
from reportlab.pdfgen import canvas
import datetime
from PIL import Image
import os
import ctypes

d_date = datetime.datetime.now()
reg_format_date = d_date.strftime("  %d-%m-%Y   %I:%M:%S %p")


root=Tk()
root.geometry('600x600')
root.configure(background='lightblue')
root.title("Vismera Technology")

label = Label(root, text="Course Bill Generator",bg='lightblue',width=20,font=("bold", 25))
label.place(x=95,y=53)

label_1 = Label(root, text="FullName",bg='lightblue',width=20,font=("bold", 15))
label_1.place(x=80,y=130)
textBox=Text(root,height=1.5,width=22)
textBox.place(x=260,y=130)

label_2= Label(root, text="Mobile No",width=20,bg='lightblue',font=("bold", 15))
label_2.place(x=80,y=180)
textBox1=Text(root,height=1.50,width=22)
textBox1.place(x=260,y=180)

label_g= Label(root, text="Gender",width=20,bg='lightblue',font=("bold", 15))
label_g.place(x=80,y=230)
var = IntVar()
Radiobutton(root, text="Male  ",padx = 6, variable=var,bg='lightblue',font=("bold",12), value=1).place(x=260,y=230)
Radiobutton(root, text="Female",padx = 10, variable=var,bg='lightblue',font=("bold",12),value=2).place(x=325,y=230)


label_3= Label(root, text="Email",width=20,bg='lightblue',font=("bold", 15))
label_3.place(x=80,y=280)
textBox2=Text(root,height=1.50,width=22)
textBox2.place(x=260,y=280)


label_4= Label(root, text="Course",width=20,bg='lightblue',font=("bold", 15))
label_4.place(x=80,y=330)
textBox3=Text(root,height=1.50,width=22)
textBox3.place(x=260,y=330)

label_5= Label(root, text="Fees",width=20,bg='lightblue',font=("bold", 15))
label_5.place(x=80,y=380)
textBox4=Text(root,height=1.50,width=22)
textBox4.place(x=260,y=380)


buttonCommit=Button(root,height=2,width=15,bg='lightpink',text="Submit",font=("bold", 15),command=lambda:retrieve_input())
buttonCommit.place(x=90,y=450)

button1=Button(root,height=2,width=15,bg='lightpink',text="Cancel",font=("bold",15),command=lambda:retrieve_input1())
button1.place(x=300,y=450)



def retrieve_input():
    inputValue=(textBox.get("1.0","end-1c"),textBox1.get("1.0","end-1c"),textBox2.get("1.0","end-1c"),textBox3.get("1.0","end-1c"),textBox4.get("1.0","end-1c"))
    c=canvas.Canvas(str(inputValue[0])+d_date.strftime("%d-%m-%Y")+'.pdf')
    c.setFont("Times-Italic",12)
    c.drawString(275,795,"     Bill/Invoice")
    c.setFont("Times-Roman",12)
    c.drawImage("comp.jfif",225,700,width=7*cm,height=3*cm)
    c.drawString(55,680,"   Email:info@vismera.in                       Website:www.vismera.in                             Ph:7090261897")
    c.line(55,670,560,670)
    c.rect(55,560,500,100)
    c.line(308,660,308,560)
    c.drawString(65,630," Date:")
    c.line(100,630,200,630)
    c.drawString(103,632, d_date.strftime("%d-%m-%Y"))
    c.drawString(65,610,"Time:")
    c.line(100,610,200,610)
    c.drawString(103,612, d_date.strftime("%I:%M:%S %p"))
    
    c.drawString(320,630,"To Mr/Ms:")
    c.drawString(382,632,str(inputValue[0]))
    c.line(380,630,520,630)
    
    c.drawString(320,610,"MobileNo:")
    c.drawString(382,612,str(inputValue[1]))            
    c.line(380,610,520,610)
    
    c.drawString(320,590," Email-id:")
    c.drawString(382,592,str(inputValue[2]))
    c.line(380,590,520,590)
                 
    c.rect(55,520,500,40)
    c.drawString(65,535,"SI No.                  DESCRIPTION                      QTY                    RATE                   AMOUNT  ")
    c.drawString(72,495,"1")
    c.drawString(152,495,str(inputValue[3]))
    c.drawString(320,495,"1")
    c.drawString(385,495,str(inputValue[4]))
    c.drawString(470,495,str(inputValue[4]))
    
    
    c.rect(55,280,500,240)
    c.rect(55,210,500,70)
    c.rect(55,140,500,70)
    c.line(105,560,105,280)
    c.line(285,560,285,280)
    c.line(340,560,340,210)
    c.line(440,560,440,210)
    c.drawString(65,240," Rupees:")
    c.line(120,240,210,240)
    c.drawString(122,242,str(inputValue[4]))
    c.drawString(370,240,"Total")
    c.line(70,175,180,175)
    c.drawString(470,240,str(inputValue[4]))
    c.drawString(70,160,"Customer Signature")
    c.drawString(420,160,"Director Signature")
    c.line(420,175,520,175)
    c.setFont("Times-Italic",12)
    c.drawString(120,50,"    An investment in Vismera Technology pays the best Knowledge as interest")
    c.drawString(275,30,"  Thank you")
    c.save()
def retrieve_input1():
    exit()
    c.save()
mainloop()
