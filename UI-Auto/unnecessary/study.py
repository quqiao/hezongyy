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

