from selenium import webdriver
import time

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("http://www.baidu.com")

# 获得百度搜索窗口句柄
sreach_windows = driver.current_window_handle

driver.find_element_by_link_text('登录').click()
time.sleep(5)
driver.find_element_by_link_text("立即注册").click()

# 获得当前所有打开的窗口的句柄
all_handles = driver.window_handles

print(all_handles)
# 进入注册窗口
for handle in all_handles:
    if handle != sreach_windows:
        driver.switch_to.window(handle)
        print('now register window!')
        driver.find_element_by_xpath("//*[@id=\"TANGRAM__PSP_4__userName\"]").send_keys('username')
        # driver.find_element_by_name('password').send_keys('password')
        time.sleep(2)
        # ……
time.sleep(5)

driver.quit()