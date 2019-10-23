#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
"""关于窗口"""

import os
import webbrowser as wb
from tkinter import Label, Message, Tk, Toplevel
from tkinter.font import Font

from PIL import Image, ImageTk

import libs.global_variable as glv
from libs.functions import set_window_center


class About(Toplevel):
    """关于"""

    def __init__(self, master=None):
        root = Toplevel(master=master)
        root.title("关于")
        set_window_center(root, 400, 400)
        root.resizable(False, False)

        self.app_name = glv._get("APP_NAME")
        self.app_version = glv._get("APP_VERSION")
        self.app_desc = "开源 免费 安全"
        self.app_url = "http://douftp.com"
        self.app_copyright = "Copyright © 2019 DouFTP All rights reserved."

        self.root = root
        self.init_page_about()

    def init_page_about(self):
        """加载控件"""

        # image_file = os.path.join(glv._get("APP_PATH"), "resource", "image", "crogram.png")
        # print(image_file)
        # img = Image.open(image_file)  # 打开图片
        # image = ImageTk.PhotoImage(img)  # 用PIL模块的PhotoImage打开

        # Label(self.root, image=image).pack(fill="both")
        Label(self.root, text=self.app_name).pack()
        Label(self.root, text=self.app_version).pack()
        urlLabel = Label(self.root, text=self.app_url, cursor="hand")
        urlLabel["font"] = Font(family='Arial', underline=1)
        urlLabel.bind("<ButtonPress-1>", self.open_url)
        urlLabel.pack()
        Label(self.root, text=self.app_copyright).pack()
        Message(self.root, text=self.app_desc).pack()
        # Label(self.root, text="你好你好你好你好").grid()
        # Label(self.root, text="类似于弹出窗口，具有独立的窗口属性。", width=150).grid()

    def open_url(self, event=None):
        wb.open_new_tab(self.app_url)


if __name__ == "__main__":
    About()
