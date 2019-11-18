# coding: utf-8
import uiautomator2 as u2

u = u2.connect_usb()
sess = u.session("com.hz.purchase")  # 启动药易购
sess(resourceId="com.hz.purchase:id/iv_icon").click()