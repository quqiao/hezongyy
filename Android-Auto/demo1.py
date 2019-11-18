# coding: utf-8
import uiautomator2 as u2

u = u2.connect_usb()
u.toast.show("test001", 3)