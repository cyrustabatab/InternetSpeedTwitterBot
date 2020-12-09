from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

PROMISED_DOWN = 300
PROMISED_UP = 50

CHROME_DRIVER_PATH = "C:\Development\chromedriver.exe"

TWITTER_EMAIL = "test@example.com" # replace with your twitter email
TWITTER_PASSWORD = "password" # replace with password

SPEEDTEST_URL ="https://www.speedtest.net/"

TWITTER_URL = "https://www.twitter.com"
class InternetSpeedTwitterBot:

    def __init__(self):

        self.driver = webdriver.Chrome(CHROME_DRIVER_PATH)
        self.up = PROMISED_UP
        self.down = PROMISED_DOWN
    

    def get_internet_speed(self):
        self.driver.get(SPEEDTEST_URL)
        go_button = self.driver.find_element_by_css_selector('.js-start-test.test-mode-multi')
        go_button.click()
        time.sleep(60)

        download_element = self.driver.find_element_by_css_selector(".result-data-large.number.result-data-value.download-speed")
        self.download_speed = float(download_element.text)
        upload_element = self.driver.find_element_by_css_selector(".result-data-large.number.result-data-value.upload-speed")
        self.upload_speed = float(upload_element.text)
        print(self.download_speed,self.upload_speed)
        

        if self.download_speed < self.down or self.upload_speed < self.up:
            self.tweet_at_provider()







    def tweet_at_provider(self):
        self.driver.get(TWITTER_URL)
        time.sleep(2)

        button = self.driver.find_element_by_link_text('Log in')
        button.click()
        time.sleep(2)
        form = self.driver.find_element_by_xpath('//*[@id="react-root"]/div/div/div[2]/main/div/div/div[1]/form/div/div[1]/label/div/div[2]/div/input')
        form.send_keys(TWITTER_EMAIL)
        form = self.driver.find_element_by_xpath('//*[@id="react-root"]/div/div/div[2]/main/div/div/div[1]/form/div/div[2]/label/div/div[2]/div/input')
        form.send_keys(TWITTER_PASSWORD)

        body = self.driver.find_element_by_tag_name("body")
        button = self.driver.find_element_by_xpath('//*[@id="react-root"]/div/div/div[2]/main/div/div/div[1]/form/div/div[3]/div')
        button.click()
        time.sleep(3)

        tweet = self.driver.find_element_by_xpath('//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div[2]/div/div[2]/div[1]/div/div/div/div[2]/div[1]/div/div/div/div/div/div/div/div/div/div[1]/div/div/div/div[2]/div')
        tweet.send_keys(f"Hey Internet Providers, why is my internet speed {self.download_speed}down/{self.upload_speed}up when I pay for {self.down}down/{self.up}up?") #change message to @ your ISP's twitter


        button = self.driver.find_element_by_xpath('//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div[2]/div/div[2]/div[1]/div/div/div/div[2]/div[4]/div/div/div[2]/div[3]')
        button.click()















speed_bot = InternetSpeedTwitterBot()
speed_bot.get_internet_speed()
#speed_bot.tweet_at_provider()


