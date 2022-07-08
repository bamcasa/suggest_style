from tkinter import *
import json

####################################
# json 파일 불러오기
json_directory = "style_data.json"

with open('style_data.json', encoding="utf-8") as f:  # 데이터 불러오기
    data = json.load(f)


result = set()  # 표시될 폰트들의 집합


def add_font():
    global result, small_lb_list
    index = big_lb.get(big_lb.curselection())
    result = result | set(data[index])  # 합집합

    # small_lb에 값 넣기
    small_lb_list = list(result)

    change_small_lb()
    # var.set(result)


def remove_font():
    global result, small_lb_list
    index = big_lb.get(big_lb.curselection())
    result = result - set(data[index])  # 차집합

    # small_lb에 값 넣기
    small_lb_list = list(result)

    change_small_lb()
    # var.set(result)


def change_small_lb():
    global small_lb_list, small_lb
    small_lb.delete(0, 1090000)  # 초기화

    for i in range(len(small_lb_list)):
        small_lb.insert(i, small_lb_list[i])


####################################
# thinter part
ws = Tk()
ws.title('Python Guides')
ws.geometry('400x500')
ws.config(bg='#FFFFFF')

var = StringVar()

width = 50
height = 10

big_lb = Listbox(ws, width=width, height=height)
big_lb.pack()

big_lb.insert(0, '타이틀')
big_lb.insert(1, '본문')
big_lb.insert(2, '포스터')


small_lb = Listbox(ws, width=width, height=height)
small_lb.pack()

small_lb_list = []

disp = Label(ws, textvariable=var)
disp.pack(pady=20)
Button(ws, text='추가', command=add_font).pack()
Button(ws, text='제거', command=remove_font).pack()

ws.mainloop()
