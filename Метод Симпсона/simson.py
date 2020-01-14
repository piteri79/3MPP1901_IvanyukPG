#coding: utf-8
from math import *
from tkinter import *
w = 500; h = 500
root = Tk()
root.title("Вычисление площади криволинейной трапеции методом симпсона")

# -- панели формы для тестовых полей и области графика
pn_control = Frame(root)
pn_control.pack()
pn_graph = Frame(root)
pn_graph.pack()

# -- панели формы для области графика
canv = Canvas(root, width=w, height=h)
canv.pack()

dw = (w/100)*6 #-- цена деления по оси абцисс
dh = (h/100)*6    #-- цена деления по оси ординат
zw = dw #-- начало координат по оси абцисс
zh = dh*15    #-- начало координат по оси ординат

#-- Рисуем координатную плоскость с подписями осей
canv.create_line(dw/2, zh, dw*16.5, zh, fill='black', arrow=LAST)
canv.create_text(dw*15.7, dh*14.5, text='x',font=('Times New Roman',12))
canv.create_line(dw, dh*16, dw, dh/2, fill='black', arrow=LAST)
canv.create_text(dw*1.7, dh, text='f(x)', font=('Times New Roman',12))

t=0
dt=16
while t<dt:
    canv.create_line(zw+(t*dw), zh+5, zw+(t*dw), zh-5, fill='black', dash=4)
    canv.create_text(zw+(t*dh)+10, zh+10, text=str(t), font=('Times New Roman', 10))
    canv.create_line(zw-5, zh-(t*dh), zw+5, zh-(t*dh), fill='black', dash=4)
    canv.create_text(zw-10, zh-(t*dh)-10, text=str(t), font=('Times New Roman', 10))
    t += 1

lb_txt = Label(pn_control, text=u"Введите начальную и конечную точки и точность вычисления и кликните левой кнопкой мыши")
lb_txt.pack()

lb_a = Label(pn_control, text=u"Точка а")
lb_a.pack(side = 'left')
ed_a = Entry(pn_control, width = 4)
ed_a.pack(side = 'left')

lb_b = Label(pn_control, text=u"Точка b")
lb_b.pack(side = 'left')
ed_b = Entry(pn_control, width = 4)
ed_b.pack(side = 'left')

#-- Остановка обработки события мыши
work_stop = True

def calc(xx):
    return sin(xx)*10

#-- Рисуем график функции
xg = 4; p = 1
yg = zh-200-calc(xg)
for xx in range(xg,12, 1):
    yy = zh-200-calc(xx)
    canv.create_line(zw+xg*dw, yg, zw+xx*dw, yy, fill='blue')
    xg = xx; yg = yy
canv.create_text(dw*14, dh*1.3, text='y = sin(x)', font=('Times New Roman', 24))

#-- Слушатель событий мыши
def listener(event):
    global n,work_stop
    if work_stop == True:
        ed_a.configure(state="disabled"); ed_b.configure(state="disabled")
        a = ed_a.get(); b = ed_b.get()
        if a != '' and b != '':
            a = int(a); b = int(b)
            if a>0 and a<dt and b>0 and b<dt:
                #-- Счётчик количества итераций
                n = 1; S = 0
                S0 = S; n = 2*n
                h = (b-a)/n
                x0 = a; x1 = x0 + h; x2 = x1 + h
                fa = calc(x0)
                fh = calc(x1)
                fb = calc(x2)
                S = h/3*(x0 + 4*x1 + x2)
                #-- Отобразить границы интервалов
                canv.create_line(zw+(dw*a), zh, zw+(dw*a), zh-200-fa, fill='black', dash=4)
                canv.create_line(zw+(dw*b), zh, zw+(dw*b), zh-200-fb, fill='black', dash=4)
                canv.create_line(zw+(dw*(h+a)), zh, zw+(dw*(h+a)), zh-200-h, fill='black', dash=4)
                #-- Отобразить подпись границ интервалов
                canv.create_text(zw+(dw*x0), zh+25, text='x0', font=('Times New Roman', 12))
                canv.create_text(zw+(dw*x1), zh+25, text='x1', font=('Times New Roman', 12))
                canv.create_text(zw+(dw*x2), zh+25, text='x2', font=('Times New Roman', 12))
                #-- Отобразить подпись границ интервалов
                canv.create_text(zw+(dw*x0), zh-205, text='f0', font=('Times New Roman', 12))
                canv.create_text(zw+(dw*x1), zh-220, text='f1', font=('Times New Roman', 12))
                canv.create_text(zw+(dw*x2), zh-205, text='f2', font=('Times New Roman', 12))
                canv.create_text(dw*8, dh*6, text='S = ' + str(S), font=('Times New Roman', 14))
                work_stop = False

canv.bind('<Button-1>', listener)

root.mainloop()
