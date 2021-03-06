from selenium import webdriver

# 问题1：谷歌浏览器页面上下滚动问题
# 解决方法：
# js = "var q=document.body.scrollTop=0"
# driver.execute_script(js)

# 问题2：切换网页后失去焦点问题。需重新定位，元素聚焦
# 解决方法：
# target = driver.find_element_by_xxxx()
# driver.execute_script("arguments[0].scrollIntoView();", target)

# 问题3：参数传参问题‘*self’
# 解决方法：
# *self._args 表示接受元组类参数
# **kwargs 标识接受字典类参数

# 问题4：购物车中删除商品，已收藏等操作的元素定位，自带cartID且是动态变化的，
# 解决方法：
# 需考虑其他的定位方式，考虑是否可用

# 问题5：测试环境中，开发一直在对测试环境变动，
# 解决方法：
# 需要一个专门的测试环境，随时都在变动时根本无法调试

# 问题6：测试执行中，使用页面切换时句柄所在的页面切换总会出现问题
# 解决方法：
# 还需不断调试下，找出根本原因

# 问题7：莫名其妙的无法定位元素
# 解决方法：
# 增加sleep时间

# 问题8：部分弹出框过段时间就会消失，不好定位
# 解决方法：
# 定位时通过网页的source ---> debugger开始按钮，等弹出框出现后暂停起来调试

# 问题9：通过className定位时，不好定位
# 解决方法：
# 元素复制和定位的不一致。例如：复制一个className:tb2_td11 subtotal要写成"tb2_td11.subtotal"

# 问题10：ClassName定位问题，class.xxx定位，
# 解决方法：
# class.xxx后面相同的内容可以根据find_elements 列表来读取

# 问题11：assert判断时，判断错误后，后面的步骤不再执行
# 解决方法：
# 每条case中assert后面不再添加步骤

# 问题12：生成的报告，错误的内容有时会出现无截图的情况
#

# 问题13：select框，元素识别执问题

# 问题14：组合识别元素，组合定位

# 问题15：pycharm在git clone项目文件时会出现失败的现象
# 解决方法：
# SSL错误
# 因为服务器的SSL证书没有经过第三方机构的签署，所以才报错。
# 解决方案如下：
# 第一步，克隆远程仓库时，用env命令设置GIT_SSL_NO_VERIFY环境变量为”ture”，并同时调用正常的git clone命令。完整的命令如下：
#
# env GIT_SSL_NO_VERIFY=true git clone https://<host_name/git/project.git
# 第二步，在克隆完毕的仓库中将http.sslVerify设置为”false”。完整的命令如下：
#
# git config http.sslVerify "false"




