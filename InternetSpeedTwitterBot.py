from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import sleep

class InternetSpeedTwitterbot:

    def __init__(self):
        self.chrome_options = webdriver.ChromeOptions()
        self.chrome_options.add_experimental_option("detach", True)
        self.driver = webdriver.Chrome(options=self.chrome_options)
        self.up = 0
        self.down = 0

    def get_internet_speed(self):
        self.driver.get("https://www.speedtest.net/")

        cookie_accept = self.driver.find_element(By.XPATH, '//div[contains(@class, "banner-actions-container") and .//button[@id="onetrust-accept-btn-handler"]]')
        cookie_accept.click()

        speed_button = self.driver.find_element(By.CLASS_NAME,'start-text')
        speed_button.click()
        sleep(80)

        download_speed = self.driver.find_element(By.CLASS_NAME, 'download-speed')
        upload_speed = self.driver.find_element(By.CLASS_NAME, 'upload-speed')

        print(f'download speed: {download_speed.text} Mb\nupload speed: {upload_speed.text} Mb')

        self.up = int(download_speed.text.split('.')[0])
        self.down = int(upload_speed.text.split('.')[0])

    def tweet_at_provider(self, login_name, password, download, upload):
        self.driver.get("https://x.com/")

        sleep(2)
        cookie_accept = self.driver.find_element(By.XPATH, '//span[contains(@class, "css-901oao") and text()="Accept all cookies"]')
        cookie_accept.click()

        sleep(2)
        login_button = self.driver.find_element(By.XPATH, '//div[contains(@class, "css-901oao") and .//span[text()="Inloggen"]]')
        login_button.click()

        sleep(3)
        email_field = self.driver.find_element(By.CSS_SELECTOR,'input[name="text"][autocomplete="username"]')
        email_field.send_keys(login_name)
        email_field.send_keys(Keys.ENTER)

        sleep(3)
        extra_username = self.driver.find_element(By.CSS_SELECTOR,'input[name="text"]')
        extra_username.send_keys('LKnol12326752')
        extra_username.send_keys(Keys.ENTER)

        sleep(3)
        password_field = self.driver.find_element(By.CSS_SELECTOR,'input[name="password"][autocomplete="current-password"]')
        password_field.send_keys(password)
        password_field.send_keys(Keys.ENTER)

        sleep(3)
        tweet = self.driver.find_element(By.CSS_SELECTOR, 'div.public-DraftStyleDefault-block.public-DraftStyleDefault-ltr')
        tweet.send_keys(f'hello, my upload speed is {self.up} and my download speed is {self.down}, while it should be {download} download and {upload} upload )')

        sleep(3)
        post = self.driver.find_element(By.XPATH, '//span[@class="css-901oao css-16my406 r-poiln3 r-bcqeeo r-qvutc0" and text()="Post"]')
        post.click()