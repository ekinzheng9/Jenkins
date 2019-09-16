from selenium import webdriver
# 账号密码 都是admin admin
# 把会员中心-教师列表-添加教师业务流做完
import time
from selenium import webdriver

## 函数化
url = 'http://localhost/admin.php?m=mgr/admin.login'

# 打开浏览器
def createDriver():
    driver = webdriver.Chrome()
    driver.get(url)
    driver.implicitly_wait(10)
    return driver

# 登录管理后台
def login(driver):
    # 输入管理后台账户名，密码
    driver.find_element_by_id('username').send_keys('admin')
    driver.find_element_by_id('password').send_keys('admin')
    driver.find_element_by_xpath('//*[@id="loginFrm"]/input').click()

# 进入会员中心
def memberCenter(driver):
    # 点击会员中心
    driver.find_element_by_link_text('会员中心').click()

# 添加教师业务流
def addTeacher(driver):
    # 点击教师列表
    driver.find_element_by_link_text('教师列表').click()
    # 切入Iframe框操作教师列表里面的内容
    ele = driver.find_element_by_id('mainframe')
    driver.switch_to.frame(ele)
    # 添加教师
    driver.find_element_by_xpath('/html/body/div[2]/h3/a[2]/span').click()
    # 填写教师详情的信息
    driver.find_element_by_id('username').send_keys('13800000005')
    driver.find_element_by_id('realname').send_keys('真的是麦克陈2')
    driver.find_element_by_id('password').send_keys('12345678')
    # 选择性别
    driver.find_element_by_xpath('//*[@id="form"]/div/div[4]/div/label[1]/input').click()
    # 下来选择角色
    from selenium.webdriver.support.ui import Select

    # 方式一选择角色
    select_role = driver.find_element_by_name('roleid')
    Select(select_role).select_by_value('7')
    # 方式二选择机构
    select_organ = driver.find_element_by_id('oneCategory')
    Select(select_role).select_by_index(1)
    # 选择邮箱
    driver.find_element_by_id('email').send_keys('aaa@163.com')
    # 选择手机
    driver.find_element_by_id('phone').send_keys('1378988777')
    # 下拉地址
    select_city = driver.find_element_by_name('location_p')
    Select(select_city).select_by_index(1)
    # 下拉区
    select_area1 = driver.find_element_by_name('location_c')
    Select(select_area1).select_by_index(1)
    select_area2 = driver.find_element_by_name('location_c')
    Select(select_area2).select_by_index(1)
    # 详细地址
    driver.find_element_by_id('address').click()
    driver.find_element_by_id('address').send_keys('你爸爸家')
    # 个人介绍
    driver.find_element_by_id('introduce').click()
    driver.find_element_by_id('introduce').send_keys('我是爸爸')
    # 确定保存
    driver.find_element_by_xpath('//*[@id="btn_sub"]/span').click()
    time.sleep(5)
    # 弹出确认成功框
    driver.switch_to.alert.accept()

# 获取校验信息
def getVerifyData(driver):
    # 返回列表确认是否添加成功
    driver.find_element_by_xpath('/html/body/div[2]/h3/a/span').click()

    # 获取标签的文本值
    data = driver.find_element_by_xpath('//*[@id="recordList"]/tr[1]/td[2]/div/a').text
    return data

