import time
from selenium import webdriver
# 导入处理alert所需要的包
from selenium.common.exceptions import NoAlertPresentException
import traceback
import datetime
import argparse

def auto_login(weburl, username, password):
    driver = webdriver.Chrome()  # 选择Chrome浏览器
    driver.get(weburl)  # 打开网站
    driver.maximize_window()  # 最大化谷歌浏览器

    time.sleep(2)

    # 处理alert弹窗
    try:
        alert1 = driver.switch_to.alert  # switch_to.alert点击确认alert
    except NoAlertPresentException as e:
        print("no alert")
        traceback.print_exc()
    else:
        at_text1 = alert1.text
        print("at_text:" + at_text1)

    time.sleep(2)

    driver.find_element_by_id('username').click()  # 点击用户名输入框
    driver.find_element_by_id('username').clear()  # 清空输入框
    driver.find_element_by_id('username').send_keys(username)  # 自动敲入用户名

    driver.find_element_by_id('password').click()  # 点击密码输入框
    driver.find_element_by_id('password').clear()  # 清空输入框
    driver.find_element_by_id('password').send_keys(password)  # 自动敲入密码

    # 采用class定位登陆按钮
    # driver.find_element_by_class_name('ant-btn').click() # 点击“登录”按钮
    # 采用xpath定位登陆按钮，
    # driver.find_element_by_xpath('//*[@id="root"]/div/div[3]/form/button').click()
    # 采用name定位登录按钮
    driver.find_element_by_name('登录').click()
    # driver.find_element_by_link_text('登录').click() # 点击“账户登录”

    time.sleep(2)

    # driver.find_element_by_id('signIn').click() # 点击“签到”

    driver.close()


if __name__ == "__main__":

    parser = argparse.ArgumentParser(description='Process some integers.')
    parser.add_argument('username', dest="username", default="2019000000", type=str,
                        help='your buct id.')
    parser.add_argument('password', dest="password", default="00000000", type=str,
                        help='your buct password.')
    parser.add_argument('weburl', dest="weburl", default='https://tree.buct.edu.cn', type=str,
                        help='BUCT weburl, Default: \"https://tree.buct.edu\".')
    parser.add_argument('times', dest="times", default='2020-02-01 00:15:00.000000', type=str,
                        help='Target Login Time.')
    parser.add_argument('step', dest="step", default=60, type=int,
                        help='Update Step Size. Default is 60 sec.')
    args = parser.parse_args()

    success = True
    i = 0
    while True:
        now = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f')
        if now > args.times:
            try:
                auto_login(args.weburl, args.username, args.password)
            except:
                print("Log in Failed.")
                success = False
            break
        else:
            i += 1
            print("Try Login {} times.".format(i))
        time.sleep(args.step)

    if success:
        print("Log in {} Success!".format(args.username))
    print("Finish Job. Progress will quit now.")