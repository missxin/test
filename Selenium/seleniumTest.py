import time

from selenium import webdriver



"""加载浏览器驱动"""
from selenium.webdriver import ActionChains
dirver=webdriver.Chrome()

"""打开网页"""
dirver.maximize_window()
dirver.get('http://www.gongcbao.com/page/account/login.html?backUrl=/')
print(dirver.title)
time.sleep(3)
"""登录"""
dirver.find_element_by_id("account").send_keys("ctjrdzsw")
time.sleep(1)
dirver.find_element_by_id("password").send_keys("111111")
time.sleep(1)
dirver.find_element_by_xpath("//*[@id=\"login_txt\"]").click()
time.sleep(1)
print(dirver.title)

"""点击保函申请、项目名称搜索"""
dirver.find_element_by_xpath("//*[@id=\"navBar\"]/ul/li[2]/a").click()

#跳转至ifram
dirver.switch_to.frame(dirver.find_element_by_xpath("//iframe[contains(@id,'bhapplyindex')]"))
# dirver.find_element_by_xpath("//*[@id='key']").send_keys("保险屋")
# time.sleep(1)
# #点击搜索
# dirver.find_element_by_xpath("/html/body/div[1]/form/blockquote/div/div[6]/button").click()
# time.sleep(2)
# #点击清空
# dirver.find_element_by_xpath("//*[@id=\"reset\"]").click()

# """选择区域测试"""
# dirver.find_element_by_xpath("/html/body/div[1]/form/blockquote/div/div[2]/div").click()
# dirver.find_element_by_xpath("/html/body/div[1]/form/blockquote/div/div[2]/div/dl/dd[14]").click()
# dirver.find_element_by_xpath("/html/body/div[1]/form/blockquote/div/div[3]").click()
# time.sleep(1)
# dirver.find_element_by_xpath("/html/body/div[1]/form/blockquote/div/div[3]/div/dl/dd[3]").click()
# #点击搜索
# dirver.find_element_by_xpath("/html/body/div[1]/form/blockquote/div/div[6]/button").click()
# time.sleep(2)
# #点击清空
# dirver.find_element_by_xpath("//*[@id=\"reset\"]").click()

# """选中项目类型"""
# dirver.find_element_by_xpath("/html/body/div[1]/form/blockquote/div/div[4]/div").click()
# dirver.find_element_by_xpath("/html/body/div[1]/form/blockquote/div/div[4]/div/div/dl/dd[2]").click()
# #点击搜索
# dirver.find_element_by_xpath("/html/body/div[1]/form/blockquote/div/div[6]/button").click()
# time.sleep(2)
# #点击清空
# dirver.find_element_by_xpath("//*[@id=\"reset\"]").click()

# """#选中保函品种"""
# dirver.find_element_by_xpath("/html/body/div[1]/form/blockquote/div/div[5]/div").click()
# time.sleep(1)
# dirver.find_element_by_xpath("/html/body/div[1]/form/blockquote/div/div[5]/div/div/dl/dd[2]").click()
# #点击搜索
# dirver.find_element_by_xpath("/html/body/div[1]/form/blockquote/div/div[6]/button").click()
# time.sleep(2)
# #点击清空
# dirver.find_element_by_xpath("//*[@id=\"reset\"]").click()

"""立即办理保函"""
dirver.find_element_by_xpath("/html/body/div[1]/form/blockquote/div/div[6]/button").click()
time.sleep(2)
dirver.find_element_by_xpath("/html/body/div[1]/div[1]/div/div/div[2]/table/tbody/tr[7]/td[9]/div/span").click()
time.sleep(2)
dirver.find_element_by_xpath("//*[@id=\"applay\"]").click()
time.sleep(2)
dirver.find_element_by_xpath("//*[@id=\"next\"]").click()
dirver.find_element_by_xpath("//*[@id=\"checkbox\"]/i").click()
dirver.find_element_by_xpath("//*[@id=\"pay_div\"]").click()

# dirver.back()
#从ifram跳转出来
dirver.switch_to.default_content()
time.sleep(20)
dirver.find_element_by_xpath("//*[@id=\"confirmSubmit\"]").click()
time.sleep(2)
dirver.find_element_by_xpath("//*[@id=\"smsval\"]").send_keys("999999")
time.sleep(2)
dirver.find_element_by_xpath("//*[@id=\"smspanel\"]/div/div/div/a[1]").click()
time.sleep(10)
dirver.switch_to.frame(dirver.find_element_by_xpath("//iframe[contains(@id,'bhapplyindex')]"))
dirver.find_element_by_xpath("//*[@id=\"pay_text\"]").click()
dirver.switch_to.default_content()
time.sleep(10)
dirver.switch_to.window()
dirver.find_element_by_xpath("//*[@id=\"confirm\"]").click()
dirver.find_element_by_xpath("//*[@id=\"debitCard\"]").click()
dirver.find_element_by_xpath("//*[@id=\"kqDebitCardBankList\"]/li[8]").click()
dirver.find_element_by_xpath("//*[@id=\"bankCardNext\"]/span").click()
dirver.find_element_by_xpath("//*[@id=\"quick_cardNo\"]").send_keys("622908121000127512")
dirver.find_element_by_xpath("//*[@id=\"user_name\"]").send_keys("傅天一")
dirver.find_element_by_xpath("//*[@id=\"cert_no\"]").send_keys("360101198803170012")
dirver.find_element_by_xpath("//*[@id=\"card_phone\"]").send_keys("18650119319")
dirver.find_element_by_xpath("//*[@id=\"getIdenCodeBtn\"]").click()
time.sleep(60)
dirver.find_element_by_xpath("//*[@id=\"bankCardConfirm\"]/span").click()

# time.sleep(1)
# #点击订单管理
# dirver.find_element_by_xpath("//*[@id=\"navBar\"]/ul/li[3]/a").click()
# time.sleep(1)
# #点击我的保函
# dirver.find_element_by_xpath("//*[@id=\"navBar\"]/ul/li[4]").click()
# time.sleep(1)
# #点击企业信息
# dirver.find_element_by_xpath("//*[@id=\"navBar\"]/ul/li[5]").click()
# time.sleep(1)
# #点击我的发票
# dirver.find_element_by_xpath("//*[@id=\"navBar\"]/ul/li[6]").click()
# time.sleep(1)
# #点击帮助中心
# dirver.find_element_by_xpath("//*[@id=\"navBar\"]/ul/li[7]").click()
# time.sleep(1)
# #点击系统设置
# dirver.find_element_by_xpath("//*[@id=\"navBar\"]/ul/li[8]").click()
# time.sleep(1)
# #点击员工管理
# dirver.find_element_by_xpath("//*[@id=\"navBar\"]/ul/li[8]/dl/dd[1]").click()
# time.sleep(1)
# #点击角色管理
# dirver.find_element_by_xpath("//*[@id=\"navBar\"]/ul/li[8]/dl/dd[2]").click()
# time.sleep(1)
# #点击日志管理
# dirver.find_element_by_xpath("//*[@id=\"navBar\"]/ul/li[8]/dl/dd[3]").click()
# time.sleep(1)
# 退出
# dirver.quit()