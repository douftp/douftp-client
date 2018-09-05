#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
"""关于窗口"""

import os
from tkinter import Label, Message, Tk, Toplevel

from PIL import Image, ImageTk

import lib.global_variable as glv
from lib.functions import set_window_center


class About(Toplevel):
    """关于"""

    def __init__(self, master=None):
        root = Toplevel(master=master)
        root.title("关于")
        set_window_center(root, 400, 400)
        root.resizable(False, False)
        
        self.app_name = glv.get_variable("APP_NAME")
        self.app_version = glv.get_variable("APP_VERSION")
        self.app_desc = "简述简述简述简述简述简述"
        self.app_url = "https://crogram.com"
        self.app_copyright = "Copyright © 2018 Crogram, Inc. All rights reserved."

        self.root = root
        self.init_page()

    def init_page(self):
        """加载控件"""

        # image_file = os.path.join(glv.get_variable("APP_PATH"), "resource", "image", "crogram.png")
        # print(image_file)
        # img = Image.open(image_file)  # 打开图片
        # image = ImageTk.PhotoImage(img)  # 用PIL模块的PhotoImage打开

        # Label(self.root, image=image).pack(fill="both")
        Label(self.root, text=self.app_name).pack()
        Label(self.root, text=self.app_version).pack()
        Label(self.root, text=self.app_url).pack()
        Label(self.root, text=self.app_copyright).pack()
        Message(self.root, text=self.app_desc).pack()
        # Label(self.root, text="你好你好你好你好").grid()
        # Label(self.root, text="类似于弹出窗口，具有独立的窗口属性。", width=150).grid()


if __name__ == "__main__":
    About()