from lib2to3.pgen2 import driver
from unittest import TestCase

from mobileTest import BeforeTest
from selenium.webdriver.common.by import By
from appium.webdriver.common.mobileby import AppiumBy
from appium import *
from appium.webdriver.common.touch_action import TouchAction
from appium_flutter_finder.flutter_finder import FlutterElement
import time
import unittest
import os
from appium import webdriver
from time import sleep
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
import cv2
import numpy as np
import time, datetime

wd = BeforeTest.Apprun()

wd.find_element(AppiumBy.XPATH,
                '//android.widget.Button[@content-desc="로그인"]').click()
print('Login View 진입')

LoginID = wd.find_element(AppiumBy.XPATH,
                          '//android.widget.EditText[1]')
LoginID.click()
time.sleep(2)
LoginID.send_keys('01055559999')
time.sleep(2)
print('휴대폰 번호 입력 완료')

LoginPassword = wd.find_element(AppiumBy.XPATH,
                                '//android.widget.EditText[2]')
time.sleep(2)
LoginPassword.click()
time.sleep(2)
LoginPassword.send_keys('Rlaehdus100!')
print('Password 입력 완료')
print('Login Test : Pass')

LoginButton = wd.find_element(AppiumBy.ACCESSIBILITY_ID, '로그인')
LoginButton.click()

# Mobile 의 Notification 창을 열어준다
# wd.open_notifications()









