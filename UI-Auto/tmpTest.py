# from selenium import webdriver
# from time import sleep
# from selenium.webdriver.common.action_chains import ActionChains
# from selenium.webdriver.common.by import By
#
# driver = webdriver.Chrome()
# driver.get("http://192.168.20.80:9000/#/login")
# driver.maximize_window()
# driver.find_element(By.XPATH,"//input[@placeholder='请输入用户名']").send_keys("liuquan")
# driver.find_element(By.XPATH,"//input[@placeholder='请输入密码']").send_keys("123456")
# driver.find_element(By.XPATH,"//button/span").click()
# sleep(2)
# ele = driver.find_element(By.XPATH,'//i[contains(@class,"iconfont") and contains(@class,"icon_top-menu")]')
# ActionChains(driver).move_to_element(ele).perform()