#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
"""DOUFTP CLIENT GUI VIEW"""

import os
import time
from ftplib import FTP
from tkinter import (Button, Entry, Frame, IntVar, Label, Listbox, Menu,
                     StringVar, Tk, filedialog)
from tkinter.ttk import Scrollbar, Treeview

import libs.global_variable as glv
from components import app_menu
from libs.functions import set_window_center


class ftp_client():
    def __init__(self, master):
        self.root = master

        self.root.title(glv._get("APP_NAME"))
        self.root.minsize(800, 600)
        set_window_center(self.root, 900, 600)
        # self.root.resizable(False, False)
        self.root.update()

        self.var_port = IntVar(value=3333)
        self.var_address = StringVar(value="0.0.0.0")
        self.default_timeout = IntVar(value=-999)
        self.path_remote = StringVar()
        self.path_local = StringVar()
        self.inputFileName = ""

        self.filelist_local = None
        self.filelist_remote = None

        self.toolbar_box = None  # 工具按钮栏
        self.quickbar_box = None  # 快速连接栏
        self.footer_box = None  # 底部状态栏
        self.content_box = None  # 主要内容视图容器
        self.remote_box = None  # 远程服务端资源
        self.local_box = None  # 本地资源

        self.ftp_connect = FTP()
        self.init_view()

    def init_view(self):
        """界面"""

        app_menu.AppMenu(self.root)
        self.init_frame()
        self.init_toolbar()
        self.init_header()
        self.init_remote()
        self.init_local()
        self.init_footer()

    def init_frame(self):
        """基本框架"""

        # 工具按钮栏
        self.toolbar_box = Frame(self.root, relief="ridge", bd=1)
        self.toolbar_box.pack(fill="x", expand=None, side="top", anchor="n")

        # 快速连接栏
        self.quickbar_box = Frame(self.root, relief="ridge", bd=1)
        self.quickbar_box.pack(fill="x", expand=None, side="top", anchor="n")

        # 底部状态栏
        self.footer_box = Frame(self.root, relief="ridge", bd=1)
        self.footer_box.pack(fill="x", expand=None, side="bottom", anchor="s")

        # 主要内容视图容器
        self.content_box = Frame(self.root, relief="ridge", bd=0)
        self.content_box.pack(fill="both", expand=True)

        # 远程服务端文件列表
        self.remote_box = Frame(self.content_box, relief="ridge", bd=0)
        self.remote_box.pack(fill="both", expand=True, side="right")

        # 本地文件列表
        self.local_box = Frame(self.content_box, relief="ridge", bd=0)
        self.local_box.pack(fill="both", expand=True, side="left")

    def init_header(self):
        """头部栏"""
        if not self.quickbar_box:
            return False

        Label(self.quickbar_box, text="主机:").pack(side="left")
        self.entry_ip = Entry(self.quickbar_box, textvariable=self.var_address)
        self.entry_ip["width"] = 15
        self.entry_ip.pack(side="left")

        Label(self.quickbar_box, text="账号:").pack(side="left")
        self.entry_user = Entry(self.quickbar_box, width=15)
        self.entry_user.pack(side="left")

        Label(self.quickbar_box, text="密码:").pack(side="left")
        self.entry_passwd = Entry(self.quickbar_box, show="*", width=15)
        self.entry_passwd.pack(side="left")

        Label(self.quickbar_box, text="端口:").pack(side="left")
        self.entry_port = Entry(self.quickbar_box, textvariable=self.var_port)
        self.entry_port["width"] = 5
        self.entry_port.pack(side="left")

        button_connect = Button(self.quickbar_box, text="快速连接")
        button_connect["command"] = self.ftp_login
        button_connect["width"] = 10
        button_connect.pack(side="left")

    def init_toolbar(self):
        """工具栏"""

        if not self.toolbar_box:
            return False

        button_connect = Button(self.toolbar_box, text="快速连接")
        button_connect["command"] = self.ftp_login
        button_connect.pack(side="left")

        button_disconnect = Button(self.toolbar_box, text="断开")
        button_disconnect["command"] = self.ftp_quit
        button_disconnect.pack(side="left")

        button_reflash = Button(self.toolbar_box, text="刷新")
        button_reflash["command"] = self.flash_remote
        button_reflash.pack(side="left")

        button_transfer = Button(self.toolbar_box, text="传输")
        # button_transfer["command"] = self.flash_remote
        button_transfer.pack(side="left")

        button_suspend = Button(self.toolbar_box, text="暂停")
        # button_suspend["command"] = self.flash_remote
        button_suspend.pack(side="left")

        button_stop = Button(self.toolbar_box, text="停止")
        # button_stop["command"] = self.flash_remote
        button_stop.pack(side="left")

        button_new_folder = Button(self.toolbar_box, text="新建文件夹")
        # button_new_folder["command"] = self.flash_remote
        button_new_folder.pack(side="left")

        button_new_file = Button(self.toolbar_box, text="新建文件")
        # button_new_file["command"] = self.flash_remote
        button_new_file.pack(side="left")

        button_edit = Button(self.toolbar_box, text="编辑")
        # button_edit["command"] = self.flash_remote
        button_edit.pack(side="left")

        button_preview = Button(self.toolbar_box, text="预览")
        # button_preview["command"] = self.flash_remote
        button_preview.pack(side="left")

        button_introduction = Button(self.toolbar_box, text="属性")
        # button_introduction["command"] = self.flash_remote
        button_introduction.pack(side="left")

        button_delete = Button(self.toolbar_box, text="删除")
        # button_delete["command"] = self.flash_remote
        button_delete.pack(side="left")

    def init_remote(self):
        """远程文件列表"""

        if not self.remote_box:
            return False

        btn_bar = Frame(self.remote_box, relief="ridge", bd=1)
        btn_bar.pack(fill="x", expand=False, side="top")
        Label(btn_bar, text="远程:").pack(fill="x", expand=None, side="left")
        path = Entry(btn_bar, textvariable=self.path_remote)
        path.pack(fill="x", expand=True, side="left")

        Button(
            btn_bar, text="打开", command=self.select_path_remote).pack(
                fill="x", expand=None, side="left")
        Button(btn_bar, text="重连", command=self.ftp_login).pack(side="left")
        Button(btn_bar, text="断开", command=self.ftp_quit).pack(side="left")
        Button(
            btn_bar, text="刷新", command=self.flash_remote).pack(
                fill="x", expand=None, side="right")

        file_list = Frame(self.remote_box, relief="ridge", bd=0)
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

        if not self.local_box:
            return False

        btns = Frame(self.local_box, relief="ridge", bd=1)
        btns.pack(fill="x", expand=False, side="top")
        Label(btns, text="本地:").pack(fill="x", expand=None, side="left")
        Entry(
            btns, textvariable=self.path_local).pack(
                fill="x", expand=True, side="left")
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
        """底部状态栏"""

        if not self.footer_box:
            return False

        Label(self.footer_box, text="欢迎使用").pack(side="left")
        Label(self.footer_box, text="欢迎使用").pack(fill="x", side="left")
        ct = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
        self.clock = Label(self.footer_box, text=ct)
        self.clock.pack(side="right")
        self.clock.after(1000, self.trickit)
        self.trickit()

    def trickit(self):
        ct = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
        self.clock["text"] = ct
        self.clock.update()
        self.clock.after(1000, self.trickit)

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
