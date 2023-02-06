from appium import webdriver


desired_cap = {
    "platformName": "Android",
    "appium:platformVersion": "13",
    "appium:app": "C:\\Users\\dykim\\Downloads\\a19c60e8-ec35-4061-93c8-4e617482e04.apk",
    "appium:automationName": "Appium",
    "appium:udid": "127.0.0.1:62001",
    "appium:appPackage": "com.suprema.moon",
    "appium:appActivity": "com.suprema.moon.MainActivity"
}

def Apprun():
  wd = webdriver.Remote("http://localhost:4723/wd/hub", desired_cap)
  wd.implicitly_wait(10)
  return wd

