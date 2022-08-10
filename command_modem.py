"""
Module functions automate execution of the web interface actions in D-Link DIR-651 web manager application
(which is found at http://192.168.0.1)

use parameters (specified in config.py):
-r to restart modem
-w to toggle Wi-Fi

change login and password consts in config.p to pass login in
"""
import sys, time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service as BraveService
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.core.utils import ChromeType
from config import *


def login_modem(driver, path):
    """Pass login dilaog with login/password specified in config.py"""
    driver.get(path)
    elem_username = driver.find_element(By.ID, FIELD_LOGIN_NAME)
    elem_username.send_keys(LOGIN_NAME)
    elem_password = driver.find_element(By.ID, FIELD_LOGIN_PWD)
    elem_password.send_keys(LOGIN_PWD)
    elem_password.send_keys(Keys.RETURN)


def restart_modem(driver):
    """Click on Restart modem and accept the action in alert window"""
    button_reboot = driver.find_element(By.XPATH, BUTTON_RESTART)
    button_reboot.click()
    driver.switch_to.alert.accept()


def toggle_wifi(driver):
    """Click on Wi-Fi checkbox and Apply button"""
    time.sleep(8)
    checkbox_wifi = WebDriverWait(driver, 3).until(EC.element_to_be_clickable((By.XPATH, CHECKBOX_WIFI)))
    checkbox_wifi.click()
    button_apply = driver.find_element(By.XPATH, BUTTON_APPLY_WIFI)
    button_apply.click()


def main():
    driver = webdriver.Chrome(service=BraveService(ChromeDriverManager(chrome_type=ChromeType.BRAVE).install()))
    driver.implicitly_wait(10)

    if len(sys.argv) == 2 and sys.argv[1] == PARAM_RESTART:
        login_modem(driver, URL_RESTART_MODEM)
        restart_modem(driver)
    elif len(sys.argv) == 2 and sys.argv[1] == PARAM_TOGGLE_WIFI:
        login_modem(driver, URL_TOGGLE_WIFI)
        toggle_wifi(driver)

    driver.close()


if __name__ == '__main__':
    main()
