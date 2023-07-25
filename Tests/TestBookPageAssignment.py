import time
from unittest import TestCase
from Utility.SharedFunctions1 import commonFunctions
from Utility.CommonFunction import commonMethod
from Pages.Book_page_assigmentPage import bookPageAssignment
from Utility.InputFile import Inputs

common_function = commonFunctions()
Shared_function = commonMethod()
input = Inputs()
book = bookPageAssignment()
sheetName = "3-Book page Assignment"
Description = common_function.GenrateSimpleStringLimit10()


class BookPageAssignment(TestCase):

    def test_Book_page_Assignment_1(self):

        # Login into site
        driver = Shared_function.test_logincms()

        # Verify the add  Record of Book page Assignment
        tes_case_id = "03-01"
        driver.find_element_by_xpath(book.admintool).click()
        driver.find_element_by_xpath(book.bookPage).click()

        time.sleep(1)
        # Switch iframe
        iframe = driver.find_element_by_xpath(book.tooliframe)
        driver.switch_to_frame(iframe)
        actual_result = driver.find_element_by_xpath(book.assignmentpage).text
        # Check result
        expected_result = "No Records Found, Click on 'Add Record' to Add one."

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

    def test_Book_page_Assignment_2(self):

        # Login into site
        driver = Shared_function.test_logincms()

        # Verify the add  Record of Book page Assignment
        tes_case_id = "03-02"
        driver.find_element_by_xpath(book.admintool).click()
        driver.find_element_by_xpath(book.bookPage).click()

        time.sleep(1)
        # Switch iframe
        iframe = driver.find_element_by_xpath(book.tooliframe)
        driver.switch_to_frame(iframe)
        driver.find_element_by_id(book.addRecord).click()
        driver.find_element_by_id(book.description).send_keys(Description)
        driver.find_element_by_id(book.book).send_keys(2)
        driver.find_element_by_id(book.page).send_keys(4)
        driver.find_element_by_id(book.maximumPage).send_keys(6)
        driver.find_element_by_id(book.overFlow).send_keys(1)

        # Insert Record
        driver.find_element_by_xpath(book.Insert).click()
        time.sleep(2)
        table = driver.find_element_by_id(book.table)
        target_column_index = 2  # Replace with the desired column number (0-indexed)
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
        expected_result = Description

        try:
            if column_values[0] == expected_result:
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

    def test_Book_page_Assignment_3(self):

        # Login into site
        driver = Shared_function.test_logincms()

        # Verify the add  Record of Book page Assignment
        tes_case_id = "03-03"
        driver.find_element_by_xpath(book.admintool).click()
        driver.find_element_by_xpath(book.bookPage).click()

        time.sleep(1)
        # Switch iframe
        iframe = driver.find_element_by_xpath(book.tooliframe)
        driver.switch_to_frame(iframe)
        driver.find_element_by_id(book.addRecord).click()
        driver.find_element_by_id(book.description).send_keys(Description)
        driver.find_element_by_id(book.book).send_keys(2)
        driver.find_element_by_id(book.page).send_keys(4)
        driver.find_element_by_id(book.maximumPage).send_keys(6)
        driver.find_element_by_id(book.overFlow).send_keys(1)

        # Insert Record
        driver.find_element_by_xpath(book.cancel).click()
        time.sleep(1)
        # Find input text field
        input_text_fname = driver.find_element_by_id(book.description)

        # Get the value in the input text field
        actual_result = input_text_fname.get_attribute('value')

        # Check result
        expected_result = ''

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

    def test_Book_page_Assignment_5(self):

        # Login into site
        driver = Shared_function.test_logincms()

        # Verify edit Book page Assignment operation by changes their name
        tes_case_id = "03-05"
        driver.find_element_by_xpath(book.admintool).click()
        driver.find_element_by_xpath(book.bookPage).click()

        time.sleep(1)
        # Switch iframe
        iframe = driver.find_element_by_xpath(book.tooliframe)
        driver.switch_to_frame(iframe)

        # Click on Edit
        driver.find_element_by_xpath(book.edit).click()
        driver.find_element_by_xpath(book.updated_description).clear()
        driver.find_element_by_xpath(book.updated_description).send_keys("Civil_updated")
        driver.find_element_by_xpath(book.update).click()

        table = driver.find_element_by_id(book.table)
        target_column_index = 2  # Replace with the desired column number (0-indexed)
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

        expected_result = 'Civil_updated'

        try:
            if column_values[0] == expected_result:
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

    def test_Book_page_Assignment_6(self):

        # Login into site
        driver = Shared_function.test_logincms()

        # Verify deletion Book page Assignment operation by changes their name
        tes_case_id = "03-06"
        driver.find_element_by_xpath(book.admintool).click()
        driver.find_element_by_xpath(book.bookPage).click()

        time.sleep(1)
        # Switch iframe
        iframe = driver.find_element_by_xpath(book.tooliframe)
        driver.switch_to_frame(iframe)

        # Click on Edit
        driver.find_element_by_xpath(book.deletion).click()

        actual_result = ''
        expected_result = ''

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
