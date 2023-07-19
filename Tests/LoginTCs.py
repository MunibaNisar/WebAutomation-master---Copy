import pdb
import time
from unittest import TestCase
from Utility.SharedFunctions1 import commonFunctions
from Pages.LoginPage import Login
from Utility.InputFile import Inputs
common_function = commonFunctions()
input = Inputs()
login = Login()
sheetName = "Login"


class LoginTcs(TestCase):

    def test_case_login(self):
        driver = common_function.driver_initialization()
        # login with valid username and password
        tes_case_id = "0-01"
        url = input.cms_url
        driver.get(url)
        username = input.User
        password = input.password

        driver.find_element_by_id(login.username_id).send_keys(username)
        driver.find_element_by_id(login.password_id).send_keys(password)
        driver.find_element_by_id(login.loginbtn).click()
        # Check result
        expected_result ='https://myiconsandbox.com/QA/CMS360/Main360.aspx'
        time.sleep(1)
        actual_result = driver.current_url

        try:
            if actual_result == expected_result:
                status = "Passed"
                file_path = None

            else:
                status = 'Failed'
                # save screenshot in folder
                file_path = common_function.screenshort(tes_case_id, driver)
                print("took sc")
                assert False
        finally:
            # save in  Excel file
            print("saving file")
            common_function.UpdateExcelTestCase(sheetName, tes_case_id, status, file_path)
            print("saved in file")
            driver.quit()

    def test_case_login_1(self):
        driver = common_function.driver_initialization()
        # login with valid username and Invalid password
        tes_case_id = "0-02"
        url = input.cms_url
        driver.get(url)

        driver.find_element_by_id(login.username_id).send_keys('Muniba')
        driver.find_element_by_id(login.password_id).send_keys('123')
        driver.find_element_by_id(login.loginbtn).click()
        # Check result
        expected_result ='Invalid Username or Password'
        expected_result1='Login attempts exceeded.'
        time.sleep(2)
        actual_result = driver.find_element_by_id('lblError').text

        try:
            if actual_result == expected_result or actual_result == expected_result1 :
                status = "Passed"
                file_path = None

            else:
                status = 'Failed'
                # save screenshot in folder
                file_path = common_function.screenshort(tes_case_id, driver)
                print("took sc")
                assert False
        finally:
            # save in  Excel file
            print("saving file")
            common_function.UpdateExcelTestCase(sheetName, tes_case_id, status, file_path)
            print("saved in file")
            driver.quit()

    def test_case_login_2(self):
        driver = common_function.driver_initialization()
        # login with valid username and Invalid password
        tes_case_id = "0-02"
        url = input.cms_url
        driver.get(url)

        driver.find_element_by_id(login.username_id).send_keys('1m')
        driver.find_element_by_id(login.password_id).send_keys('Cryptocheat_123')
        driver.find_element_by_id(login.loginbtn).click()
        # Check result
        expected_result ='Invalid Username or Password'
        expected_result1='Login attempts exceeded.'
        time.sleep(2)
        actual_result = driver.find_element_by_id('lblError').text

        try:
            if actual_result == expected_result or actual_result == expected_result1 :
                status = "Passed"
                file_path = None

            else:
                status = 'Failed'
                # save screenshot in folder
                file_path = common_function.screenshort(tes_case_id, driver)
                print("took sc")
                assert False
        finally:
            # save in  Excel file
            print("saving file")
            common_function.UpdateExcelTestCase(sheetName, tes_case_id, status, file_path)
            print("saved in file")
            driver.quit()

    def test_case_login_3(self):
        driver = common_function.driver_initialization()
        # login with valid username and Invalid password
        tes_case_id = "0-02"
        url = input.cms_url
        driver.get(url)

        driver.find_element_by_id(login.username_id).send_keys('1m')
        driver.find_element_by_id(login.password_id).send_keys('Cryptoch')
        driver.find_element_by_id(login.loginbtn).click()
        # Check result
        expected_result ='Invalid Username or Password'
        expected_result1='Login attempts exceeded.'
        time.sleep(2)
        actual_result = driver.find_element_by_id('lblError').text

        try:
            if actual_result == expected_result or actual_result == expected_result1 :
                status = "Passed"
                file_path = None

            else:
                status = 'Failed'
                # save screenshot in folder
                file_path = common_function.screenshort(tes_case_id, driver)
                print("took sc")
                assert False
        finally:
            # save in  Excel file
            print("saving file")
            common_function.UpdateExcelTestCase(sheetName, tes_case_id, status, file_path)
            print("saved in file")
            driver.quit()

    def test_login(self):
        driver = common_function.driver_initialization()
        # login with valid username and password
        tes_case_id = "0-01"
        url = input.cms_url
        driver.get(url)
        username = input.User
        password = input.password

        driver.find_element_by_id(login.username_id).send_keys(username)
        driver.find_element_by_id(login.password_id).send_keys(password)
        driver.find_element_by_id(login.loginbtn).click()
        # Check result
        expected_result ='https://myiconsandbox.com/QA/CMS360/Main360.aspx'
        time.sleep(1)
        actual_result = driver.current_url

        try:
            if actual_result == expected_result:
                status = "Passed"
                file_path = None

            else:
                status = 'Failed'
                # save screenshot in folder
                file_path = common_function.screenshort(tes_case_id, driver)
                print("took sc")
                assert False
        finally:
            return driver




