import time
from unittest import TestCase
from Utility.SharedFunctions1 import commonFunctions
from Utility.CommonFunction import commonMethod
from Pages.BondsmanPage import Bondsman
from Utility.InputFile import Inputs

common_function = commonFunctions()
Shared_function = commonMethod()
input = Inputs()
bondsman = Bondsman()
sheetName = "2-Bondsman"
first_name = common_function.GenrateSimpleStringLimit10()
last_name = common_function.GenrateSimpleStringLimit10()


class BondmanTest(TestCase):

    def test_Bondsman_1(self):

        # Login into site
        driver = Shared_function.test_logincms()

        # Verify the add  option of Bondsman
        tes_case_id = "02-01"
        driver.find_element_by_xpath(bondsman.admintool).click()
        driver.find_element_by_xpath(bondsman.bondsman).click()
        # Check result
        expected_result = 'Bondsman Search:'
        time.sleep(1)
        # Switch iframe
        iframe = driver.find_element_by_xpath(bondsman.bondsmaniframe)
        driver.switch_to_frame(iframe)
        time.sleep(3)
        actual_result = driver.find_element_by_id(bondsman.bondsmanSearch)
        actual_result = actual_result.text

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

    def test_Bondsman_2(self):

        # Login into site
        driver = Shared_function.test_logincms()

        # verify the save button operation while adding bondsman
        tes_case_id = "02-02"
        driver.find_element_by_xpath(bondsman.admintool).click()
        driver.find_element_by_xpath(bondsman.bondsman).click()
        # Switch iframe
        iframe = driver.find_element_by_xpath(bondsman.bondsmaniframe)
        driver.switch_to_frame(iframe)
        # Click on  add button
        time.sleep(1)
        driver.find_element_by_id(bondsman.addBtn).click()
        time.sleep(1)
        driver.find_element_by_id(bondsman.firstName).send_keys(first_name)
        driver.find_element_by_id(bondsman.lastName).send_keys(last_name)
        driver.find_element_by_id(bondsman.save).click()

        # Check result
        expected_result = 'Bondsman Search:'
        actual_result = driver.find_element_by_id(bondsman.bondsmanSearch).text

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

    def test_Bondsman_3(self):

        # Login into site
        driver = Shared_function.test_logincms()

        # verify the Cancel button operation while adding bondsman
        tes_case_id = "02-03"
        driver.find_element_by_xpath(bondsman.admintool).click()
        driver.find_element_by_xpath(bondsman.bondsman).click()
        # Switch iframe
        iframe = driver.find_element_by_xpath(bondsman.bondsmaniframe)
        driver.switch_to_frame(iframe)
        # Click on  add button
        time.sleep(1)
        driver.find_element_by_id(bondsman.addBtn).click()
        time.sleep(1)
        driver.find_element_by_id(bondsman.cancelBtn).click()

        # Check result
        expected_result = 'Bondsman Search:'
        actual_result = driver.find_element_by_id(bondsman.bondsmanSearch).text

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

    def test_Bondsman_5(self):

        # Login into site
        driver = Shared_function.test_logincms()

        # Verify the bondsman serach by correct bondsman infromation
        tes_case_id = "02-05"
        driver.find_element_by_xpath(bondsman.admintool).click()
        driver.find_element_by_xpath(bondsman.bondsman).click()
        # Switch iframe
        iframe = driver.find_element_by_xpath(bondsman.bondsmaniframe)
        driver.switch_to_frame(iframe)
        # Click on  add button
        time.sleep(1)

        # # Search added bondsman
        driver.find_element_by_id(bondsman.bondsmanSearchField).send_keys(f"{last_name.upper()}, {first_name.upper()}")
        time.sleep(1)
        driver.find_element_by_xpath(bondsman.listBondsman)
        driver.find_element_by_id('ctl00_RadAjaxPanel1').click()

        table = driver.find_element_by_id(bondsman.table)
        target_column_index = 0  # Replace with the desired column number (0-indexed)
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
        # using list comprehension
        actual_result = ' '.join([str(elem) for elem in column_values])

        # Check result
        expected_result = f"{last_name.upper()}, {first_name.upper()}"

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

    def test_Bondsman_6(self):

        # Login into site
        driver = Shared_function.test_logincms()

        # Verify the bondsman serach by incorrect bondsman infromation
        tes_case_id = "02-06"
        driver.find_element_by_xpath(bondsman.admintool).click()
        driver.find_element_by_xpath(bondsman.bondsman).click()
        # Switch iframe
        iframe = driver.find_element_by_xpath(bondsman.bondsmaniframe)
        driver.switch_to_frame(iframe)
        # Click on  add button
        time.sleep(1)
        driver.find_element_by_id(bondsman.bondsmanSearchField).send_keys("i9")
        time.sleep(1)
        actual_result = driver.find_element_by_xpath(bondsman.matches).text

        # Check result
        expected_result = 'No matches'

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

    def test_Bondsman_7(self):

        # Login into site
        driver = Shared_function.test_logincms()

        # Verify the bondsman serach by correct bondsman infromation
        tes_case_id = "02-07"
        driver.find_element_by_xpath(bondsman.admintool).click()
        driver.find_element_by_xpath(bondsman.bondsman).click()
        # Switch iframe
        iframe = driver.find_element_by_xpath(bondsman.bondsmaniframe)
        driver.switch_to_frame(iframe)
        # Click on  add button
        time.sleep(1)
        driver.find_element_by_id(bondsman.addBtn).click()
        time.sleep(1)
        first_name1 = common_function.GenrateSimpleStringLimit10()
        last_name1 = common_function.GenrateSimpleStringLimit10()
        driver.find_element_by_id(bondsman.firstName).send_keys(first_name1)
        driver.find_element_by_id(bondsman.lastName).send_keys(last_name1)
        driver.find_element_by_id(bondsman.save).click()
        # # Search added bondsman
        driver.find_element_by_id(bondsman.bondsmanSearchField).send_keys(
            f"{last_name1.upper()}, {first_name1.upper()}")
        time.sleep(1)
        driver.find_element_by_xpath(bondsman.listBondsman)
        driver.find_element_by_id('ctl00_RadAjaxPanel1').click()
        # Edit email
        driver.find_element_by_xpath(bondsman.editBtn).click()
        driver.find_element_by_id(bondsman.email).send_keys("muniba@gmail.com")
        driver.find_element_by_id(bondsman.save)

        table = driver.find_element_by_id(bondsman.table)
        target_column_index = 0  # Replace with the desired column number (0-indexed)
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

        # using list comprehension
        actual_result = ' '.join([str(elem) for elem in column_values])

        # Check result
        expected_result = f"{last_name1.upper()}, {first_name1.upper()}"

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

    def test_Bondsman_8(self):

        # Login into site
        driver = Shared_function.test_logincms()

        # Verify the bondsman deletion
        tes_case_id = "02-08"
        driver.find_element_by_xpath(bondsman.admintool).click()
        driver.find_element_by_xpath(bondsman.bondsman).click()
        # Switch iframe
        iframe = driver.find_element_by_xpath(bondsman.bondsmaniframe)
        driver.switch_to_frame(iframe)
        # # Search added bondsman
        driver.find_element_by_id(bondsman.bondsmanSearchField).send_keys(f"{last_name.upper()}, {first_name.upper()}")
        time.sleep(1)
        driver.find_element_by_xpath(bondsman.listBondsman)
        driver.find_element_by_id('ctl00_RadAjaxPanel1').click()
        # Edit email
        driver.find_element_by_xpath(bondsman.deleteBtbn).click()
        driver.switch_to.alert.accept()

        # After deletion
        time.sleep(2)
        driver.find_element_by_id(bondsman.bondsmanSearchField).clear()
        driver.find_element_by_id(bondsman.bondsmanSearchField).send_keys(f"{last_name.upper()}, {first_name.upper()}")
        time.sleep(1)
        actual_result = driver.find_element_by_xpath(bondsman.matches).text

        # Check result
        expected_result = 'No matches'
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
