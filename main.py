from cgitb import text
import math
from tkinter import *

app = Tk()
app.title("Calculator")
#app setting
wind = Entry(app, width=35, borderwidth=5)
wind.grid(row = 0, column = 0, columnspan = 3, padx = 10, pady = 10)

"""
    Global Variable in Python = ตัวแปรที่สร้างขึ้นนอก ฟังก์ชัน เรียกว่าตัวแปรโกลบอล 
    ทุกคนสามารถเข้าถึงตัวแปรส่วนกลางได้ทั้งภายในและภายนอกฟังก์ชัน
"""

#Button add,clear,click,equal def

def button_clear():
     wind.delete(0, END)

def button_click(number):
    current = wind.get()
    wind.insert(0 ,str(current) + str(number))

def button_add():
    first_number = wind.get()
    global f_num
    global math
    math = "addition"
    f_num = int(first_number)
    wind.delete(0, END)

def button_subtract():
    first_number = wind.get()
    global f_num
    global math
    math = "subtraction"
    f_num = int(first_number)
    wind.delete(0, END)

def button_multiply():
    first_number = wind.get()
    global f_num
    global math
    math = "multiplication"
    f_num = int(first_number)
    wind.delete(0, END)

def button_divide():
    first_number = wind.get()
    global f_num
    global math
    math = "division"
    f_num = int(first_number)
    wind.delete(0, END)

def button_EQ():
    second_number = wind.get()  
    wind.delete(0, END)
    if math == "addition" :
        wind.insert(0, f_num + int(second_number))
    if math == "subtraction" :
        wind.insert(0, f_num - int(second_number))
    if math == "multiplication" :
        wind.insert(0, f_num * int(second_number))  
    if math == "division" :
        wind.insert(0, f_num / int(second_number))

"""
    lambda = arrow function(javaScrip)
    Python lambda คือ anonymous function หมายถึง ฟังก์ชันที่ไม่ต้องมีชื่อ
    โดย argument(ข้อโต้แย้ง) จะรับกี่ตัวก็ได้ สามารถระบุเพิ่มได้โดยคั่นแต่ละตัวด้วย comma(,) 
    และการทำงานของ Lambda จะรีเทิร์นผลลัพธ์จาก expression(การแสดงออก) กลับมาเสมอ
"""

#Button list

# padx = กว้าง
# pady = สูง

button_1 = Button(app, text="1", padx=40, pady=20, command=lambda: button_click(1))
button_2 = Button(app, text="2", padx=40, pady=20, command=lambda: button_click(2))
button_3 = Button(app, text="3", padx=40, pady=20, command=lambda: button_click(3))
button_4 = Button(app, text="4", padx=40, pady=20, command=lambda: button_click(4))
button_5 = Button(app, text="5", padx=40, pady=20, command=lambda: button_click(5))
button_6 = Button(app, text="6", padx=40, pady=20, command=lambda: button_click(6))
button_7 = Button(app, text="7", padx=40, pady=20, command=lambda: button_click(7))
button_8 = Button(app, text="8", padx=40, pady=20, command=lambda: button_click(8))
button_9 = Button(app, text="9", padx=40, pady=20, command=lambda: button_click(9))
button_0 = Button(app, text="0", padx=40, pady=20, command=lambda: button_click(0)) 

button_eq    = Button(app, text="=", padx=88, pady=20, command= button_EQ)
button_Clear = Button(app, text="Clear", padx=79, pady=20, command= button_clear)

button_Add       = Button(app, text="+", padx=39, pady=20, command= button_add)
button_Subtract  = Button(app, text="-", padx=41, pady=20, command= button_subtract)
button_Multiply  = Button(app, text="*", padx=40, pady=20, command= button_multiply)
button_Divide    = Button(app, text="/", padx=41, pady=20, command= button_divide)
#row    = แถว
#column = ลำดับ
 
button_1.grid(row=3, column=0)
button_2.grid(row=3, column=1)
button_3.grid(row=3, column=2)

button_4.grid(row=2, column=0)
button_5.grid(row=2, column=1)
button_6.grid(row=2, column=2)

button_7.grid(row=1, column=0)
button_8.grid(row=1, column=1)
button_9.grid(row=1, column=2)

button_0.grid(row=4 , column=0)

button_Clear.grid(row=4, column=1, columnspan=2)
button_eq.grid(row=5, column=1, columnspan=2)

button_Add.grid(row=5, column=0)
button_Subtract.grid(row=6 , column=0)
button_Multiply.grid(row=6 , column=1)
button_Divide.grid(row=6 , column=2)

app.mainloop()
