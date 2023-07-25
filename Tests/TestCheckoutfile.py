import time
from unittest import TestCase
from Utility.SharedFunctions1 import commonFunctions
from Utility.CommonFunction import commonMethod
from Pages.CheckOut_Page import CheckInOut
from Utility.InputFile import Inputs
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.keys import Keys
common_function = commonFunctions()
Shared_function = commonMethod()
input = Inputs()
check = CheckInOut()
sheetName = "4-Case File Check out"
Description = common_function.GenrateSimpleStringLimit10()


class Checkout(TestCase):

    def test_CheckInout_1(self):

        # Login into site
        driver = Shared_function.test_logincms()

        # Verify the add  Record of Book page Assignment
        tes_case_id = "04-01"
        driver.find_element_by_xpath(check.admintool).click()
        driver.find_element_by_xpath(check.checkInout).click()

        time.sleep(1)
        # Switch iframe
        iframe = driver.find_element_by_xpath(check.tooliframe)
        driver.switch_to_frame(iframe)
        actual_result = driver.find_element_by_xpath(check.containLabel).text
        # Check result
        expected_result = "Contains :"

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

    def test_CheckInout_2(self):

        # Login into site
        driver = Shared_function.test_logincms()

        # Verify check out case on base of  correct case number
        tes_case_id = "04-02"
        driver.find_element_by_xpath(check.admintool).click()
        driver.find_element_by_xpath(check.checkInout).click()

        time.sleep(1)
        # Switch iframe
        iframe = driver.find_element_by_xpath(check.tooliframe)
        driver.switch_to_frame(iframe)

        driver.find_element_by_id(check.contain).send_keys('22CR00105')
        actual_result = driver.find_element_by_xpath(check.case_verify).text
        # Check result
        expected_result = "22CR00105"

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

    def test_CheckInout_3(self):

        # Login into site
        driver = Shared_function.test_logincms()

        # Verify check out case on base of  incorrect case number
        tes_case_id = "04-03"
        driver.find_element_by_xpath(check.admintool).click()
        driver.find_element_by_xpath(check.checkInout).click()

        time.sleep(1)
        # Switch iframe
        iframe = driver.find_element_by_xpath(check.tooliframe)
        driver.switch_to_frame(iframe)

        driver.find_element_by_id(check.contain).send_keys('124*')
        actual_result = driver.find_element_by_xpath(check.case_verify).text
        # Check result
        expected_result = ""

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

    def test_CheckInout_4(self):

        # Login into site
        driver = Shared_function.test_logincms()

        # Verify check out case on base of  correct Judge
        tes_case_id = "04-04"
        driver.find_element_by_xpath(check.admintool).click()
        driver.find_element_by_xpath(check.checkInout).click()

        time.sleep(1)
        # Switch iframe
        iframe = driver.find_element_by_xpath(check.tooliframe)
        driver.switch_to_frame(iframe)

        driver.find_element_by_id(check.contain).send_keys('MUNIBA')
        select = Select(driver.find_element_by_id(check.selectOption))
        select.select_by_value('1')
        driver.find_element_by_id(check.contain).send_keys(Keys.ENTER)
        #   Verify judge name
        table = driver.find_element_by_id(check.table)
        target_column_index = 1  # Replace with the desired column number (0-indexed)
        tr_elements = table.find_elements_by_tag_name("tr")
        # Step 6: Loop through the <tr> elements and extract the text from the desired column
        column_values = []
        for tr_element in tr_elements:
            # Find the <td> elements inside each <tr>
            td_elements = tr_element.find_elements_by_tag_name("td")

            # Check if the row contains enough columns
            if target_column_index < len(td_elements):
                # Extract the text from the desired column
                column_values.append(td_elements[target_column_index].text)

        # Check result
        expected_result = "MUNIBA"

        try:
            if  expected_result or " " in column_values:
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

    def test_CheckInout_5(self):

        # Login into site
        driver = Shared_function.test_logincms()

        # Verify check out case on base of  correct Judge
        tes_case_id = "04-05"
        driver.find_element_by_xpath(check.admintool).click()
        driver.find_element_by_xpath(check.checkInout).click()

        time.sleep(1)
        # Switch iframe
        iframe = driver.find_element_by_xpath(check.tooliframe)
        driver.switch_to_frame(iframe)

        driver.find_element_by_id(check.contain).send_keys('ad')
        select = Select(driver.find_element_by_id(check.selectOption))
        select.select_by_value('1')

        actual_result = driver.find_element_by_xpath(check.case_verify).text
        # Check result
        expected_result = ""

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

    def test_CheckInout_8(self):

        # Login into site
        driver = Shared_function.test_logincms()

        # Verify check out case on base of  correct User
        tes_case_id = "04-08"
        driver.find_element_by_xpath(check.admintool).click()
        driver.find_element_by_xpath(check.checkInout).click()

        time.sleep(1)
        # Switch iframe
        iframe = driver.find_element_by_xpath(check.tooliframe)
        driver.switch_to_frame(iframe)

        driver.find_element_by_id(check.contain).send_keys('MUNIBA')
        select = Select(driver.find_element_by_id(check.selectOption))
        select.select_by_value('4')
        driver.find_element_by_id(check.contain).send_keys(Keys.ENTER)
        #   Verify judge name
        table = driver.find_element_by_id(check.table)
        target_column_index = 4  # Replace with the desired column number (0-indexed)
        tr_elements = table.find_elements_by_tag_name("tr")
        # Step 6: Loop through the <tr> elements and extract the text from the desired column
        column_values = []
        for tr_element in tr_elements:
            # Find the <td> elements inside each <tr>
            td_elements = tr_element.find_elements_by_tag_name("td")

            # Check if the row contains enough columns
            if target_column_index < len(td_elements):
                # Extract the text from the desired column
                column_values.append(td_elements[target_column_index].text)

        # Check result
        expected_result = "MUNIBA"

        try:
            if  expected_result or " " in column_values:
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

    def test_CheckInout_9(self):

        # Login into site
        driver = Shared_function.test_logincms()

        # Verify check out case on base of  incorrect  User
        tes_case_id = "04-09"
        driver.find_element_by_xpath(check.admintool).click()
        driver.find_element_by_xpath(check.checkInout).click()

        time.sleep(1)
        # Switch iframe
        iframe = driver.find_element_by_xpath(check.tooliframe)
        driver.switch_to_frame(iframe)

        driver.find_element_by_id(check.contain).send_keys('ad')
        select = Select(driver.find_element_by_id(check.selectOption))
        select.select_by_value('4')

        actual_result = driver.find_element_by_xpath(check.case_verify).text
        # Check result
        expected_result = ""

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

    def test_CheckInout_11(self):

        # Login into site
        driver = Shared_function.test_logincms()

        # Verify cancel label and validate it genrated label
        tes_case_id = "04-11"
        driver.find_element_by_xpath(check.admintool).click()
        time.sleep(1)
        driver.find_element_by_xpath(check.checkInout).click()

        time.sleep(1)
        # Switch iframe
        iframe = driver.find_element_by_xpath(check.tooliframe)
        driver.switch_to_frame(iframe)
        # click on badge
        driver.find_element_by_id(check.badge).click()
        driver.find_element_by_id(check.cancel).click()

        actual_result = driver.find_element_by_xpath(check.containLabel).text
        # Check result
        expected_result = "Contains :"

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