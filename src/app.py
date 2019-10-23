#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
"""DOUFTP CLIENT APPLICATION"""

import os
from tkinter import Tk

import libs.global_variable as gv
from components import app_view

gv._init()
gv._set("APP_NAME", "FTP客户端GUI")
gv._set("APP_PATH", os.path.dirname(__file__))  # 当前目录
gv._set("APP_VERSION", "0.1.1")


class App(Tk):
    """Application Class"""

    def __init__(self):
        Tk.__init__(self)
        app_view.ftp_client(self)
        self.mainloop()


if __name__ == "__main__":
    App()
