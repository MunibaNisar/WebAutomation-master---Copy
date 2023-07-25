import time
from unittest import TestCase
from Utility.SharedFunctions1 import commonFunctions
from Utility.CommonFunction import commonMethod
from Pages.attorneysPage import Attorney
from Utility.InputFile import Inputs
common_function = commonFunctions()
Shared_function = commonMethod()
input = Inputs()
attorney = Attorney()
sheetName = "1-Attorneys"
first_name = common_function.GenrateSimpleStringLimit10()
last_name = common_function.GenrateSimpleStringLimit10()


class attorneyTest(TestCase):

    def test_Attorney_1(self):

        # Login into site
        driver = Shared_function.test_logincms()

        # Verify the add  option of attorneys
        tes_case_id = "01-01"
        driver.find_element_by_xpath(attorney.admintool).click()
        driver.find_element_by_xpath(attorney.attorney).click()
        # Check result
        expected_result = 'Attorney Search'
        time.sleep(1)
        # Switch iframe
        iframe = driver.find_element_by_xpath(attorney.attorneyiframe)
        driver.switch_to_frame(iframe)
        actual_result = driver.find_element_by_id(attorney.attorneyPage)
        actual_result= actual_result.text

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

    def test_Attorney_2(self):

        # Login into site
        driver = Shared_function.test_logincms()

        # verify the save button operation while adding attorneys
        tes_case_id = "01-01"
        driver.find_element_by_xpath(attorney.admintool).click()
        driver.find_element_by_xpath(attorney.attorney).click()
        # Switch iframe
        iframe = driver.find_element_by_xpath(attorney.attorneyiframe)
        driver.switch_to_frame(iframe)
        # Click on  add button
        time.sleep(1)
        driver.find_element_by_id(attorney.add).click()
        time.sleep(4)
        driver.find_element_by_id(attorney.firstName).send_keys(first_name)
        driver.find_element_by_id(attorney.lastName).send_keys(last_name)
        driver.find_element_by_id(attorney.save).click()

        # Check result
        expected_result = 'Attorney Search'
        actual_result = driver.find_element_by_id(attorney.attorneyPage).text

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

    def test_Attorney_3(self):

        # Login into site
        driver = Shared_function.test_logincms()

        # verify the Cancel button operation while adding attorneys
        tes_case_id = "01-03"
        driver.find_element_by_xpath(attorney.admintool).click()
        driver.find_element_by_xpath(attorney.attorney).click()
        # Switch iframe
        iframe = driver.find_element_by_xpath(attorney.attorneyiframe)
        driver.switch_to_frame(iframe)
        # Click on  add button
        time.sleep(1)
        driver.find_element_by_id(attorney.add).click()
        time.sleep(4)
        driver.find_element_by_id(attorney.cancelBtn).click()

        # Check result
        expected_result = 'Attorney Search'
        actual_result = driver.find_element_by_id(attorney.attorneyPage).text

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

    def test_Attorney_4(self):

        # Login into site
        driver = Shared_function.test_logincms()

        # Verify the attorney serach by correct attorney infromation
        tes_case_id = "01-05"
        driver.find_element_by_xpath(attorney.admintool).click()
        driver.find_element_by_xpath(attorney.attorney).click()
        time.sleep(1)
        # Switch iframe
        iframe = driver.find_element_by_xpath(attorney.attorneyiframe)
        driver.switch_to_frame(iframe)
        driver.find_element_by_id(attorney.attorneySearch).send_keys('Nisar, Muniba')
        time.sleep(1)
        driver.find_element_by_xpath(attorney.list).click()
        time.sleep(1)
        driver.find_element_by_id(attorney.attorneySearch).click()

        table = driver.find_element_by_id(attorney.table)
        target_column_index = 3  # Replace with the desired column number (0-indexed)
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
        expected_result = 'Nisar, Muniba'
        try:
            if expected_result.upper() == column_values[0]:

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

    def test_Attorney_5(self):

        # Login into site
        driver = Shared_function.test_logincms()

        # Verify the attorney serach by incorrect attorney infromation
        tes_case_id = "01-06"
        driver.find_element_by_xpath(attorney.admintool).click()
        driver.find_element_by_xpath(attorney.attorney).click()
        time.sleep(1)
        # Switch iframe
        iframe = driver.find_element_by_xpath(attorney.attorneyiframe)
        driver.switch_to_frame(iframe)
        driver.find_element_by_id(attorney.attorneySearch).send_keys('*12')
        time.sleep(2)
        actual_result = driver.find_element_by_xpath(attorney.noMatch).text
        # Check result
        expected_result = 'No matches'
        try:
            if expected_result == actual_result:

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

    def test_Attorney_6(self):

        # Login into site
        driver = Shared_function.test_logincms()

        # Verify edit attorney operation by changes their email
        tes_case_id = "01-07"
        driver.find_element_by_xpath(attorney.admintool).click()
        driver.find_element_by_xpath(attorney.attorney).click()
        time.sleep(1)
        # Switch iframe
        iframe = driver.find_element_by_xpath(attorney.attorneyiframe)
        driver.switch_to_frame(iframe)
        driver.find_element_by_id(attorney.attorneySearch).send_keys('Nisar, Muniba')
        time.sleep(2)
        driver.find_element_by_xpath(attorney.list).click()
        driver.find_element_by_id(attorney.attorneySearch).click()

         # click on edit btn
        driver.find_element_by_xpath(attorney.editBtn).click()
        time.sleep(2)
        driver.find_element_by_id(attorney.email).clear()
        driver.find_element_by_id(attorney.email).send_keys("muniba@gmail.com")
        driver.find_element_by_id(attorney.save).click()
        actual_result = driver.find_element_by_id(attorney.alter).text

        expected_result = 'Highlighted records have no associated cases'
        try:
            if expected_result == actual_result:

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

