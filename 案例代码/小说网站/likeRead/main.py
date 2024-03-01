import tkinter as tk
import search
import chapterList
from tkinter import *
from PIL import Image, ImageTk
import threading,os
import platform

if __name__ == '__main__':
    root = Tk()
    curWidth = 450
    curHight = 170
    root.title("小说下载器")
    if not curWidth:
        '''获取窗口宽度，默认200'''
        curWidth = root.winfo_width()
    if not curHight:
        '''获取窗口高度，默认200'''
        curHight = root.winfo_height()
    # print(curWidth, curHight)

    # 获取屏幕宽度和高度
    scn_w, scn_h = root.maxsize()
    # print(scn_w, scn_h)

    # 计算中心坐标
    cen_x = (scn_w - curWidth) / 2
    cen_y = (scn_h - curHight) / 2
    # print(cen_x, cen_y)

    # 设置窗口初始大小和位置
    size_xy = '%dx%d+%d+%d' % (curWidth, curHight, cen_x, cen_y)
    root.geometry(size_xy)

    # 做成背景的装饰
    pic1 = Image.open('static/bg.png').resize((600, 600))  # 加载图片并调整大小至窗口大小
    pic = ImageTk.PhotoImage(pic1)
    render = Label(root, image=pic, compound=tk.CENTER, justify=tk.LEFT)
    render.place(x=0, y=0)

    # 标签 and 输入框
    label1 = Label(root, text='输入小说名在线搜索:', font=('微软雅黑', 15), fg='black')
    label1.grid(row=0, column=0, sticky=W)
    entry1 = Entry(root, font=('宋体', 15), width=15)
    entry1.grid(row=0, column=1, sticky=W)
    button1 = Button(root,text='点击搜索', font=('宋体', 12), width=10,command=lambda :thread_it(tk_search,))
    button1.grid(row=0, column=2, sticky=W)

    def tk_search():
        search_result = entry1.get().replace(" ", "").replace('\n', '').replace('"', '')
        if search_result:
            search.search(search_result)
        else:
            print("请输入小说名")



    label2 = Label(root, text='输入小说目录页地址:', font=('微软雅黑', 15))
    label2.grid(row=1, column=0, sticky=W, pady=25)
    entry2 = Entry(root, font=('宋体', 15), width=15)
    entry2.grid(row=1, column=1, sticky=W)
    button2 = Button(root,text='点击下载', font=('宋体', 12), width=10,command=lambda :thread_it(tk_search2,))
    button2.grid(row=1, column=2, sticky=W)

    def tk_search2():
        search_result = entry2.get().replace(" ", "").replace('\n', '').replace('"', '')
        if search_result:
            book = False
            try:
                book = chapterList.classify(search_result)
                print("保存结束！")
            except:
                print('下载异常')
            if book:
                print("保存结束！")


    def thread_it(func, *args):
        t = threading.Thread(target=func, args=args)
        t.setDaemon(True)
        t.start()


    def open_txt():
        if platform.system().lower() == 'windows':
            os.system('notepad ./static/readme.txt')
        else:
            os.system('open -t ./static/readme.txt')


    '查看目前支持爬取的网站'
    befeidfp = tk.Button(root,activebackground='#ccc',text='工具声明',command=lambda :thread_it(open_txt,),font=('微软雅黑',12))
    befeidfp.grid(row=2,column=2)

    root.mainloop()
