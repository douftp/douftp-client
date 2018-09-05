#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
"""菜单"""

from tkinter import Menu
from window import win_about


class AppMenu():
    """菜单类"""

    def __init__(self, master=None):
        self.root = master
        self.menu_bar = None
        self.menu_file = None
        self.menu_edit = None
        self.menu_view = None
        self.menu_bookmark = None
        self.menu_window = None
        self.menu_help = None

        self.init_menu()

        self.window_about = None

    def init_menu(self):

        menu_bar = Menu(self.root)
        self.menu_bar = menu_bar

        self.init_menu_file()
        self.init_menu_edit()
        self.init_menu_view()
        self.init_menu_server()
        self.init_menu_bookmark()
        self.init_menu_window()
        self.init_menu_help()

        self.root["menu"] = menu_bar

    def init_menu_file(self):

        menu_file = Menu(self.menu_bar)
        menu_file.add_command(label="新建文件", accelerator="Command+Shift+N")
        menu_file.add_command(label="新建文件夹", accelerator="Command+N")
        menu_file.add_separator()
        menu_file.add_command(label="新建窗口", accelerator="Shift+N")
        menu_file.add_command(label="新建标签", accelerator="Shift+T")
        menu_file.add_separator()
        menu_file.add_command(label="关闭窗口", accelerator="Shift+Alt+N")
        menu_file.add_command(label="关闭标签", accelerator="Shift+Alt+T")
        menu_file.add_separator()
        menu_file.add_command(label="打开", accelerator="Command+Q")
        menu_file.add_command(label="最近文件", accelerator="Command+Q")
        menu_file.add_separator()
        menu_file.add_command(label="保存")
        menu_file.add_command(label="另存为")
        menu_file.add_separator()
        menu_file.add_command(label="关闭")
        menu_file.add_separator()
        menu_file.add_command(label="显示正在被编辑的文件")
        menu_file.add_separator()
        menu_file.add_command(label="退出", command=self.app_exit)
        self.menu_bar.add_cascade(label="文件", menu=menu_file)
        self.menu_file = menu_file

    def init_menu_edit(self):

        menu_edit = Menu(self.menu_bar)
        menu_edit.add_command(label="复制", accelerator="Command+C")
        menu_edit.add_command(label="粘贴", accelerator="Command+V")
        menu_edit.add_command(label="移动", accelerator="Command+M")
        menu_edit.add_command(label="重命名")
        menu_edit.add_separator()
        menu_edit.add_command(label="查找", accelerator="Command+F")
        menu_edit.add_command(label="全选", accelerator="Command+A")
        menu_edit.add_command(label="取消全选", accelerator="Command+Shift+A")
        menu_edit.add_separator()
        menu_edit.add_command(label="复制到", accelerator="Command+Alt+C")
        menu_edit.add_command(label="移动到", accelerator="Command+Alt+M")
        menu_edit.add_separator()
        menu_edit.add_command(label="复制文件名", accelerator="Command+Shift+C")
        menu_edit.add_command(label="复制当前路径", accelerator="Command+Shift+D")
        menu_edit.add_command(label="复制当前文件夹", accelerator="Command+Shift+C")
        menu_edit.add_separator()
        menu_edit.add_command(label="预览", accelerator="Command+Alt+P")
        menu_edit.add_command(label="查看信息", accelerator="Command+Alt+I")
        menu_edit.add_separator()
        menu_edit.add_command(label="删除")
        menu_edit.add_command(label="移到回收站")
        self.menu_bar.add_cascade(label="编辑", menu=menu_edit)
        self.menu_edit = menu_edit

    def init_menu_view(self):

        menu_view = Menu(self.menu_bar)
        menu_view.add_checkbutton(label="工具栏")
        menu_view.add_checkbutton(label="快速连接栏")
        menu_view.add_checkbutton(label="本地文件")
        menu_view.add_checkbutton(label="状态栏")
        menu_view.add_separator()
        menu_view.add_command(label="刷新", accelerator="Command+R")
        menu_view.add_separator()

        menu_sort = Menu(self.menu_bar)
        menu_sort.add_command(label="文件名")
        menu_sort.add_command(label="文件大小")
        menu_sort.add_command(label="文件类型")
        menu_sort.add_command(label="修改时间")
        menu_view.add_cascade(label="排序", menu=menu_sort)

        self.menu_bar.add_cascade(label="查看", menu=menu_view)
        self.menu_view = menu_view

    def init_menu_server(self):

        menu_server = Menu(self.menu_bar)
        menu_server.add_command(label="取消操作", accelerator="Command+N")
        menu_server.add_command(label="暂停操作")
        menu_server.add_command(label="重新连接", accelerator="Command+R")
        menu_server.add_command(label="断开连接", accelerator="Command+D")
        menu_server.add_separator()
        menu_server.add_command(label="传输", accelerator="Alt+H")
        menu_server.add_command(label="队列")
        menu_server.add_command(label="同步")
        menu_server.add_command(label="续传")
        menu_server.add_command(label="续传暂停的队列")
        menu_server.add_separator()
        menu_server.add_command(label="搜索远程文件", accelerator="Ctrl+S")
        menu_server.add_command(label="发送Raw命令")
        menu_server.add_command(label="发送Shell命令")
        menu_server.add_command(label="输入自定义命令", accelerator="Ctrl+C")
        menu_server.add_separator()
        menu_server.add_command(label="显示文件后缀名", accelerator="Ctrl+N")
        menu_server.add_command(label="显示隐藏文件", accelerator="Ctrl+N")
        menu_server.add_separator()
        menu_server.add_command(label="连接信息")
        self.menu_bar.add_cascade(label="服务器", menu=menu_server)
        self.menu_server = menu_server

    def init_menu_bookmark(self):

        menu_bookmark = Menu(self.menu_bar)
        menu_bookmark.add_command(label="添加书签", accelerator="Command+B")
        menu_bookmark.add_command(label="添加到书签", accelerator="Command+Shift+B")
        menu_bookmark.add_command(label="管理书签", accelerator="Ctrl+B")
        menu_bookmark.add_command(label="导入书签", accelerator="Ctrl+I")
        menu_bookmark.add_cascade(label="最近连接")
        self.menu_bookmark = menu_bookmark
        self.menu_bar.add_cascade(label="书签", menu=menu_bookmark)

    def init_menu_window(self):

        menu_window = Menu(self.menu_bar)
        menu_window.add_command(label="最小化", accelerator="Command+H", command=self.app_mini)
        menu_window.add_command(label="缩放")

        menu_window.add_separator()
        menu_window.add_command(label="全屏")
        menu_window.add_command(label="置顶")
        menu_window.add_separator()
        menu_window.add_command(label="12323456")
        menu_window.add_command(label="343453455")
        self.menu_bar.add_cascade(label="窗口", menu=menu_window)
        self.menu_window = menu_window

    def init_menu_help(self):

        menu_help = Menu(self.menu_bar)
        menu_help.add_command(label="检查更新", accelerator="Ctrl+N")
        menu_help.add_command(label="显示欢迎对话框", accelerator="Ctrl+W")
        menu_help.add_separator()
        menu_help.add_command(label="获得帮助", accelerator="Ctrl+G")
        menu_help.add_command(label="报告问题", accelerator="Ctrl+R")
        menu_help.add_command(label="关于我们", accelerator="Ctrl+A", command=self.about)
        self.menu_help = menu_help
        self.menu_bar.add_cascade(label="帮助", menu=menu_help)

    def app_exit(self):
        self.root.quit()

    def app_mini(self):
        self.root.iconify()

    def about(self):
        if self.window_about is not None:
            # self.window_about.destroy()
            print("已打开")
        else:
            self.window_about = win_about.About(self.root)
            self.window_about.protocol(name="WM_DELETE_WINDOW", func=self.close_about)	

    def close_about(self):
        print("已关闭-关于")
        # self.window_about.destroy()
        self.window_about = None
