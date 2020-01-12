#coding: utf-8
from math import *
from tkinter import *
w = 500; h = 500
root = Tk()
root.title("Вычисление экстремума функции методом дихотомии")

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
canv.create_line(dw/2, zh, dw*16, zh, fill='black', arrow=LAST)
canv.create_text(dw*15.7, dh*14.5, text='x',font=('Times New Roman',12))
canv.create_line(dw, dh*16, dw, dh, fill='black', arrow=LAST)
canv.create_text(dw*1.7, dh, text='f(x)', font=('Times New Roman',12))

t=0
dt=16
while t<dt:
    canv.create_line(zw+(dw*t), zh+5, zw+(dw*t), zh-5, fill='black', dash=4)
    canv.create_text(zw+(dw*t)+10, zh+10, text=str(t), font=('Times New Roman', 10))
    canv.create_line(zw-5, zh-(t*30), zw+5, zh-(t*30), fill='black', dash=4)
    canv.create_text(zw-10, zh-(t*30)-10, text=str(t*30), font=('Times New Roman', 10))
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

lb_eps = Label(pn_control, text=u"Точность эпсилон")
lb_eps.pack(side = 'left')
ed_eps = Entry(pn_control, width = 4)
ed_eps.pack(side = 'left')

#-- Счётчик количества итераций
n = 0

#-- Остановка обработки события мыши
work_stop = True

def calc(p,xx):
    return pow(2*p*(xx-10),2)

#-- Рисуем график функции
xg = 2; p = 1
yg = zh-calc(p,xg)
for xx in range(xg,16, 1):
    yy = zh-calc(p,xx)
    canv.create_line(zw+xg*dw, yg, zw+xx*dw, yy, fill='blue')
    xg = xx; yg = yy
canv.create_text(dw*14, dh*1.3, text='y  = 2px', font=('Times New Roman', 24))
canv.create_text(dw*13.2, dh, text='2', font=('Times New Roman', 12))

#-- Слушатель событий мыши
def listener(event):
    global n,work_stop
    if work_stop == True:
        ed_a.configure(state="disabled"); ed_b.configure(state="disabled"); ed_eps.configure(state="disabled")
        a = ed_a.get(); b = ed_b.get(); eps = ed_eps.get()
        if a != '' and b != '' and eps != '':
            a = int(a); b = int(b); eps = int(eps);
            if a>0 and a<dt and b>0 and b<dt and eps>0 and eps<dt:
                #-- Отобразить границы начального интервала
                canv.create_line(zw+(dw*a), zh, zw+(dw*a), dh, fill='black', dash=4)
                canv.create_line(zw+(dw*b), zh, zw+(dw*b), dh, fill='black', dash=4)
                #-- Отобразить середину начального интервала
                canv.create_line(zw+(dw*((a+b)/2)), zh, zw+(dw*((a+b)/2)), zh-dh*8, fill='black', dash=4)
                #-- Отобразить границы точности начального интервала
                canv.create_line(zw+(dw*((a+b-(eps/2))/2)), zh, zw+(dw*((a+b-(eps/2))/2)), zh-dh*8, fill='black', dash=4)
                canv.create_line(zw+(dw*((a+b+(eps/2))/2)), zh, zw+(dw*((a+b+(eps/2))/2)), zh-dh*8, fill='black', dash=4)
                while (b-a) > eps:
                    x1 = (a+b-(eps/2))/2
                    x2 = (a+b+(eps/2))/2
                    n = n + 1
                    if calc(p,x2) > calc(p,x1): b = x2
                    elif calc(p,x2) < calc(p,x1): a = x1
                x_zv = (a+b)/2
                fx = calc(p,x_zv)
                canv.create_text(dw*9.5, dh*5, text='x* = min{x : f('+str(a)+'), f('+str(b)+')}', font=('Times New Roman', 14))
                canv.create_text(dw*9.5, dh*6, text='x* = '+str(x_zv)+', f(x*) = '+str(fx)+', n = '+str(n), font=('Times New Roman', 14))
                work_stop = False

canv.bind('<Button-1>', listener)

root.mainloop()
