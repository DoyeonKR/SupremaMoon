'''
Kakao Game SDK Test App
Device: V10 (LGF600Kb1134738)
'''
import unittest
import os
from appium import webdriver
from time import sleep
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException

# opencv를 사용하기 위해 아래 모듈을 import합니다.
import cv2
import numpy as np
import time, datetime


class Matching():

    def detectimage(self, screenshotPath, detectImagePath):
        sourceimage = cv2.imread(screenshotPath, 0)
        template = cv2.imread(detectImagePath, 0)
        w, h = template.shape[::-1]

        method = eval('cv2.TM_CCOEFF')
        res = cv2.matchTemplate(sourceimage, template, method)
        min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)

        print('\nmax_val: %d' % max_val)

        top_left = max_loc
        bottom_right = (top_left[0] + w, top_left[1] + h)
        center = (top_left[0] + int(w / 2), top_left[1] + int(h / 2))

        color = (0, 0, 255)
        cv2.rectangle(sourceimage, top_left, bottom_right, color, thickness=8)

        detectshotPath = screenshotPath[:-4] + '-detect.png'
        cv2.imwrite(detectshotPath, sourceimage)

        return center


class GrandchaseLoginOutTest(unittest.TestCase):

    def makeTS(self):
        return str(int(datetime.datetime.now().timestamp()))

    def strDatetime(self):
        return str(datetime.datetime.now().strftime("%Y%m%d%H%M"))

    def setUp(self):

        # Kakao Game SDK Test App 경로
        app = os.path.join(os.path.dirname(__file__), 'D:/Test_Appium/Grand', 'resigned_com.kakaogames.grdchase_1.8.4_qa.apk')
        app = os.path.abspath(app)

        # Set up appium
        # Appium 서버의 포트는 4001로 지정합니다.
        # 그리고 desired_capabilities에 연결하려는 디바이스(V10)의 정보를 넣습니다.
        self.driver = webdriver.Remote(
            command_executor='http://127.0.0.1:4001/wd/hub',
            desired_capabilities={
                'app': app,
                'platformName': 'Android',
                'platformVersion': '8.0.0',
                'deviceName': 'LG V30',
                'automationName': 'Appium',
                'newCommandTimeout': 500,
                'appPackage': 'com.kakaogames.grdchase',
                'appActivity': 'com.kog.grandchase.Main',
                'udid': 'LGMV300L664ed5e8',
                'noReset': True
            })

    def test_search_field(self):

        matching = Matching()

        # 스크린샷을 저장할 폴더를 생성합니다.
        test_folder_name = self.strDatetime()
        currentPath = '%s/' % os.getcwd()
        test_Directory = currentPath + test_folder_name + '/'

        if not os.path.exists(test_Directory):
            os.makedirs(test_Directory)

        driver = self.driver
        wait = WebDriverWait(driver, 20)

        # Asset을 로딩하는 동안 기다립니다.
        sleep(50)

        # '카카오계정으로 로그인' 이미지 찾아 중앙을 tap 합니다.
        screenshotPath = test_Directory + '%s-screenshot.png' % self.makeTS()
        detectImagePath = currentPath + 'searchimages/kakaologin.png'
        driver.save_screenshot(screenshotPath)
        center = matching.detectimage(screenshotPath, detectImagePath)
        driver.tap([center])

        # 5초 동안 기다립니다.
        sleep(5)

        try:
            # 카카오 계정을 입력합니다.
            account = wait.until(EC.element_to_be_clickable((By.XPATH,
                                                             '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.webkit.WebView/android.webkit.WebView/android.view.View/android.view.View[2]/android.view.View[1]/android.view.View[1]/android.widget.EditText')))
            account.click()
            account.send_keys('dejavuwing@gmail.com')

            # 비밀번호를 입력합니다.
            password = wait.until(EC.element_to_be_clickable((By.XPATH,
                                                              '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.webkit.WebView/android.webkit.WebView/android.view.View/android.view.View[2]/android.view.View[1]/android.view.View[3]/android.widget.EditText')))
            password.click()
            password.send_keys('1234ngle')

            # 로그인 버튼을 클릭(탭)합니다.
            signin = wait.until(EC.element_to_be_clickable((By.XPATH,
                                                            '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.webkit.WebView/android.webkit.WebView/android.view.View/android.view.View[2]/android.view.View[2]')))
            signin.click()

            # 10초 동안 기다립니다.
            sleep(10)
        except:
            print('you have been login.')

        # 5초 동안 기다립니다.
        sleep(5)

        # '터치하여 시작하기'에서 중앙을 클릭합니다..
        screenshotPath = test_Directory + '%s-screenshot.png' % self.makeTS()
        detectImagePath = currentPath + 'searchimages/touchTostart.png'
        driver.save_screenshot(screenshotPath)
        center = matching.detectimage(screenshotPath, detectImagePath)
        driver.tap([center])

        # 5초 동안 기다립니다.
        sleep(5)

        # '옵션' 이미지 찾아 중앙을 tap 합니다.
        screenshotPath = test_Directory + '%s-screenshot.png' % self.makeTS()
        detectImagePath = currentPath + 'searchimages/option-button.png'
        driver.save_screenshot(screenshotPath)
        center = matching.detectimage(screenshotPath, detectImagePath)
        driver.tap([center])

        # 5초 동안 기다립니다.
        sleep(5)

        # '로그아웃' 이미지 찾아 중앙을 tap 합니다.
        screenshotPath = test_Directory + '%s-screenshot.png' % self.makeTS()
        detectImagePath = currentPath + 'searchimages/logout.png'
        driver.save_screenshot(screenshotPath)
        center = matching.detectimage(screenshotPath, detectImagePath)
        driver.tap([center])

        # 5초 동안 기다립니다.
        sleep(5)

        # '로그아웃 확인' 이미지 찾아 중앙을 tap 합니다.
        screenshotPath = test_Directory + '%s-screenshot.png' % self.makeTS()
        detectImagePath = currentPath + 'searchimages/logout-conform.png'
        driver.save_screenshot(screenshotPath)
        center = matching.detectimage(screenshotPath, detectImagePath)
        driver.tap([center])

        # 30초 동안 기다립니다.
        sleep(30)

    def tearDown(self):
        self.driver.quit()


if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(GrandchaseLoginOutTest)
    unittest.TextTestRunner(verbosity=2).run(suite)