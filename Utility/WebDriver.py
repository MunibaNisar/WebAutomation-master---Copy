import os
from selenium import webdriver
from selenium.webdriver import ChromeOptions, FirefoxOptions
from selenium.webdriver.chrome.options import Options


class WebDriver:



    def browser_startup(self, browser='chrome'):
        # driver = ""
        # if browser == 'chrome':
        #
        #     driver = webdriver.Chrome(ChromeDriverManager().install())
        # if browser == 'firefox':
        #     driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())
        # return driver

        # self.root = os.getcwd()
        self.root = os.path.abspath(os.path.join(os.getcwd(), os.pardir))
        self.web_driver_folder = os.path.join(self.root, "DriverResource")
        if browser == 'chrome':
            self.web_driver_name = 'chromedriver.exe'
            self.web_driver_path = os.path.join(self.web_driver_folder, self.web_driver_name)
            # self.option = ChromeOptions()

            chrome_options = Options()
            # maximized window
            chrome_options.add_argument("--start-maximized")
            self.driver = webdriver.Chrome(executable_path=r"D:\WebAutomation-master - Copy\DriversResource\chromedriver.exe",options=chrome_options)
            # self.driver = webdriver.Chrome(executable_path=self.web_driver_path, options=chrome_options)
            self.driver.implicitly_wait(5)

        return self.driver

    def close_browser(self):
        self.driver.quit()
        return None


# if __name__ == '__main__':

