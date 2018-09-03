#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
"""FTP客户端GUI"""

import os
import time
from ftplib import FTP
from tkinter import (Button, Entry, Frame, IntVar, Label, Listbox, Menu,
                     StringVar, Tk, filedialog)
from tkinter.ttk import Scrollbar, Treeview


class ftp_client():
    def __init__(self):
        root = Tk()
        self.root = root

        root.title("FTP客户端GUI")
        self.set_window_center(root, 800, 600)
        root.minsize(800, 600)
        # root.resizable(False, False)

        self.var_port = IntVar(value=3333)
        self.var_address = StringVar(value="0.0.0.0")
        self.default_timeout = IntVar(value=-999)
        self.path_remote = StringVar()
        self.path_local = StringVar()
        self.inputFileName = ""

        self.filelist_local = None
        self.filelist_remote = None

        self.ftp_connect = FTP()
        self.init_view()
        root.mainloop()


    def init_view(self):
        """界面"""
        self.init_menu()

        self.btn_box = Frame(self.root, relief="ridge", borderwidth=0)
        self.btn_box.pack(fill="x", expand=None, side="top", anchor="n")

        self.head_box = Frame(self.root, relief="ridge", borderwidth=0)
        self.head_box.pack(fill="x", expand=None, side="top", anchor="n")

        self.content_box = Frame(
            self.root, relief="ridge", borderwidth=0, bd=1)
        self.content_box.pack(fill="both", expand=True)

        self.remote_box = Frame(
            self.content_box, relief="ridge", borderwidth=0)
        self.remote_box.pack(fill="both", expand=True, side="right")

        self.local_box = Frame(self.content_box, relief="ridge", borderwidth=0)
        self.local_box.pack(fill="both", expand=True, side="left")

        self.footer_box = Frame(self.root, relief="ridge", borderwidth=0, bd=1)
        self.footer_box.pack(fill="x", expand=None, side="bottom", anchor="s")

        self.init_btns()
        self.init_header()
        self.init_remote()
        self.init_local()
        self.init_footer()

    def init_header(self):
        """头部栏"""

        label_ip = Label(self.head_box, text="主机:")
        label_ip.pack(side="left")
        self.entry_ip = Entry(
            self.head_box, textvariable=self.var_address, width=15)
        self.entry_ip.pack(side="left")

        label_user = Label(self.head_box, text="账号:")
        label_user.pack(side="left")
        self.entry_user = Entry(self.head_box, width=15)
        self.entry_user.pack(side="left")

        label_passwd = Label(self.head_box, text="密码:")
        label_passwd.pack(side="left")
        self.entry_passwd = Entry(self.head_box, show="*", width=15)
        self.entry_passwd.pack(side="left")

        label_port = Label(self.head_box, text="端口:")
        label_port.pack(side="left")
        self.entry_port = Entry(
            self.head_box, textvariable=self.var_port, width=5)
        self.entry_port.pack(side="left")

        button_connect = Button(
            self.head_box, text="快速连接", width=10, command=self.ftp_login)
        button_connect.pack(side="left")

    def init_btns(self):

        button_connect = Button(
            self.btn_box, text="快速连接", command=self.ftp_login)
        button_connect.pack(side="left")

        button_disconnect = Button(
            self.btn_box, text="断开", command=self.ftp_quit)
        button_disconnect.pack(side="left")

        button_reflash = Button(
            self.btn_box, text="刷新", command=self.flash_remote)
        button_reflash.pack(side="left")

    def init_remote(self):
        """远程文件列表"""

        btns = Frame(self.remote_box, relief="ridge", borderwidth=0)
        btns.pack(fill="x", expand=False, side="top")
        Label(btns, text="远程:").pack(fill="x", expand=None, side="left")
        Entry(
            btns, textvariable=self.path_remote).pack(
                fill="x", expand=None, side="left")
        Button(
            btns, text="打开", command=self.select_path_remote).pack(
                fill="x", expand=None, side="left")
        Button(btns, text="重连", command=self.ftp_login).pack(side="left")
        Button(btns, text="断开", command=self.ftp_quit).pack(side="left")
        Button(
            btns, text="刷新", command=self.flash_remote).pack(
                fill="x", expand=None, side="right")

        file_list = Frame(self.remote_box, relief="ridge", borderwidth=0)
        file_list.pack(fill="both", expand=True, side="top")
        # Listbox
        # self.filelist_remote = Listbox(self.remote_box)
        # self.filelist_remote.bind("<Double-Button-1>", self.click_db)
        # self.filelist_remote.pack(fill="both", expand=True, side="top")

        tree = Treeview(file_list, show="headings")
        # 列索引ID
        tree["columns"] = ("pra", "id", "user", "group", "size", "date",
                           "name")
        # 表头设置
        tree.heading("pra", text="权限")
        tree.heading("id", text="ID")
        tree.heading("user", text="用户")
        tree.heading("group", text="组")
        tree.heading("size", text="大小")
        tree.heading("date", text="最后修改日期")
        tree.heading("name", text="文件名")

        tree.column("pra", width="100")
        tree.column("id", width="50", anchor="center")
        tree.column("user", width="50")
        tree.column("group", width="50")
        tree.column("size", width="50")
        tree.column("date", width="50")
        tree.column("name", width="50")

        self.filelist_remote = tree

        vbar = Scrollbar(file_list, orient="vertical", command=tree.yview)
        tree.configure(yscrollcommand=vbar.set)
        tree.grid(row=0, column=0, sticky="nswe")
        vbar.grid(row=0, column=1, sticky="ns")

    def init_local(self):
        """本地文件列表"""

        btns = Frame(self.local_box, relief="ridge", borderwidth=0)
        btns.pack(fill="x", expand=False, side="top")
        Label(btns, text="本地:").pack(fill="x", expand=None, side="left")
        Entry(
            btns, textvariable=self.path_local).pack(
                fill="x", expand=None, side="left")
        Button(
            btns, text="打开", command=self.select_path_local).pack(
                fill="x", expand=None, side="left")
        Button(
            btns, text="刷新", command=self.flash_local).pack(
                fill="x", expand=None, side="right")

        self.filelist_local = Listbox(self.local_box)
        self.filelist_local.bind("<Double-Button-1>", self.click_db)
        self.filelist_local.pack(fill="both", expand=True, side="top")

    def init_footer(self):

        Label(self.footer_box, text="欢迎使用").pack(side="left")
        Label(self.footer_box, text="欢迎使用").pack(fill="x", side="left")
        self.clock = Label(
            self.footer_box,
            text=time.strftime('%Y-%m-%d %H:%M:%S',
                               time.localtime(time.time())))
        self.clock.pack(side="right")
        self.clock.after(1000, self.trickit)
        self.trickit()

    def trickit(self):
        currentTime = time.strftime('%Y-%m-%d %H:%M:%S',
                                    time.localtime(time.time()))
        self.clock["text"] = currentTime
        self.clock.update()
        self.clock.after(1000, self.trickit)

    def init_menu(self):

        self.menubar = Menu(self.root)

        self.menu_f = Menu(self.menubar, tearoff=0)
        for each in ["打开", "保存", "另存为", "关闭"]:
            self.menu_f.add_command(label=each)
        self.menu_f.add_separator()
        self.menu_f.add_command(label="退出", command=self.quit)
        self.menubar.add_cascade(label="文件", menu=self.menu_f)

        self.menu_e = Menu(self.menubar, tearoff=0)
        for each in ["复制", "剪切", "粘贴"]:
            self.menu_e.add_command(label=each)
        self.menubar.add_cascade(label="编辑", menu=self.menu_e)

        self.menu_v = Menu(self.menubar, tearoff=0)
        self.menu_v.add_command(label="状态")
        self.menubar.add_cascade(label="查看", menu=self.menu_v)

        self.t_menu = Menu(self.menubar)
        self.t_menu.add_command(label="状态", accelerator='Alt+H')
        self.menubar.add_cascade(label="传输", menu=self.t_menu)

        self.menu_s = Menu(self.menubar)
        self.menu_s.add_command(label="状态", accelerator='Ctrl+N')
        self.menubar.add_cascade(label="服务器", menu=self.menu_s)

        self.menu_b = Menu(self.menubar)
        self.menu_b.add_command(label="状态")
        self.menubar.add_cascade(label="书签", menu=self.menu_b)

        self.menu_h = Menu(self.menubar, tearoff=1)
        self.menu_h.add_separator()
        self.menu_h.add_command(label="版本信息")
        self.menu_h.add_separator()
        self.menu_h.add_command(label="关于我们")
        self.menubar.add_cascade(label="帮助", menu=self.menu_h)

        self.root["menu"] = self.menubar

    def ftp_login(self):
        self.ftp_connect.connect(self.var_address.get().strip(),
                                 int(self.entry_port.get().strip()))
        self.ftp_connect.login(self.entry_user.get(), self.entry_passwd.get())
        self.flash_remote()  # 加载列表

    def ftp_quit(self):
        if self.ftp_connect is not None:
            self.ftp_connect.quit()

    def ftp_close(self):
        if self.ftp_connect is not None:
            self.ftp_connect.close()

    def flash_remote(self):
        file_list = []
        self.ftp_connect.dir("", file_list.append)
        for x in file_list:
            i = x.split()  # 或者filename = x.split("\t")[列的起始值:列的终止值]
            self.filelist_remote.insert(
                "",
                "end",
                text="",
                values=(i[0], i[1], i[2], i[3], i[4], i[5:8], i[-1]))

    def flash_local(self):
        filelist = os.listdir(self.path_local.get())
        print(filelist)
        if self.filelist_local.size() > 0:
            self.filelist_local.delete(0, "end")

        for i in range(len(filelist)):
            self.filelist_local.insert("end", filelist[i])

        # file_list = []
        # self.ftp_connect.dir("", file_list.append)
        # for x in file_list:
        #     i = x.split()  # 或者filename = x.split("\t")[列的起始值:列的终止值]
        #     self.filelist_local.insert(
        #         "",
        #         "end",
        #         text="",
        #         values=(i[0], i[1], i[2], i[3], i[4], i[5:8], i[-1]))

    def click_db(self, event):
        self.download()

    def download(self):
        inputFileName = self.filelist_remote.get(
            self.filelist_remote.curselection())
        file_handler = open(self.path_remote.get() + "/" + inputFileName,
                            "wb").write
        self.ftp_connect.retrbinary(
            "RETR %s" % os.path.basename(inputFileName), file_handler, 1024)

    def select_path_local(self):
        path = filedialog.askdirectory()
        if os.path.isdir(path):
            self.path_local.set(path)

    def select_path_remote(self):
        path = filedialog.askdirectory()
        if os.path.isdir(path):
            self.path_remote.set(path)

    def quit(self):
        self.root.quit()

    def set_window_center(self, window, width, height):
        """设置窗口宽高及居中"""
        # 获取屏幕 宽、高
        w_s = window.winfo_screenwidth()
        h_s = window.winfo_screenheight()
        # 计算 x, y 位置
        x_co = (w_s - width) / 2
        y_co = (h_s - height) / 2 - 50
        window.geometry("%dx%d+%d+%d" % (width, height, x_co, y_co))
        window.minsize(width, height)

# def main():
#     ftp_client()

if __name__ == "__main__":
    ftp_client()
