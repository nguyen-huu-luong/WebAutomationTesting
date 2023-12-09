import unittest
import time
import csv
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from datetime import datetime
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class EditQuizDecisionTable(unittest.TestCase): 
    def __init__(self, arg):
        super().__init__(arg)

    def set_up_driver(self):
        options = webdriver.ChromeOptions()
        options.add_experimental_option('excludeSwitches', ['enable-logging'])
        self.driver = webdriver.Chrome(options=options)
        self.vars = {}
        self.driver.get("https://school.moodledemo.net/")

    def teardown_method(self):
        self.driver.quit()

    def login(self):
        self.driver.find_element(By.LINK_TEXT, "Log in").click()
        self.driver.find_element(By.ID, "username").send_keys("teacher") 
        self.driver.find_element(By.ID, "password").send_keys("moodle")
        self.driver.find_element(By.ID, "loginbtn").click()
        time.sleep(5)

    def format_date(self,day, month, year, hours, minutes):
    # Create a datetime object with the provided values
        date_obj = datetime(int(year), int(month), int(day), int(hours), int(minutes))

        # Format the datetime object as per your requirement
        formatted_date = date_obj.strftime("%A, %#d %B %Y, %#I:%M %p")


        return formatted_date
    
    def readData(self):
        # To Store testcase data
        data = []

        # Open file data.csv
        with open('./data.csv', 'r') as csv_file:
            csv_reader = csv.reader(csv_file)
            header = next(csv_reader)  # Read the header

            # Convert data from csv to the dictionary (object)
            for row in csv_reader:
                testcase_name = row[0]
                enable_open_day = row[1] == "True"
                open_day = { 'day': row[2], 'month': row[3], 'year': row[4],
                                'hours': row[5], 'minutes': row[6] }
                enable_close_day = row[7] == "True"
                close_day = { 'day': row[8], 'month': row[9], 'year': row[10],
                                'hours': row[11], 'minutes': row[12],
                }
                # Create a dictionary for each testcase
                testcase_data = {
                    'testcase_name': testcase_name,
                    'enable_open_day': enable_open_day,
                    'open_day': open_day,
                    'enable_close_day': enable_close_day,
                    'close_day': close_day,
                }

                # Store the data in the data array
                data.append(testcase_data)
            return data

    def set_checkbox_value(self, checkbox_id, enable):
        # Waiting for checkbox element located in the screen
        WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located((By.ID, checkbox_id)))
        # Get checkbox element
        checkbox = self.driver.find_element(By.ID, checkbox_id)
        # Verify whether the checkbox is unchecked or the opposite
        if (enable and not checkbox.is_selected()) or (not enable and checkbox.is_selected()):
            checkbox.click()

    
    def check_quiz_day_output(self, expected_close_day, nth_child=1): 
        # Waiting the time of quiz present at the screen (nth-child = 1 if open day and 2 if close day)
        actual_date = WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located(
                (By.CSS_SELECTOR, f".activity-dates > div:nth-child({nth_child})"))).text
        # Check the actual_date string at the screen contains expected_close_day string
        self.assertIn(expected_close_day, actual_date)
    

    def check_output(self, testcase):
        # Get day from testcase
        open_day = testcase['open_day']
        close_day = testcase['close_day']
        # Format the day depend on requirement
        expected_open_day = self.format_date(open_day['day'], open_day['month'], 
                                                    open_day['year'], open_day['hours'], open_day['minutes'])
        expected_close_day = self.format_date(close_day['day'], close_day['month'], 
                                                    close_day['year'], close_day['hours'], close_day['minutes'])
        # Case: open_day > close day and enable both close and open day
        if expected_open_day > expected_close_day and testcase['enable_open_day'] and testcase['enable_close_day']:
            # Error timeclose must be present
            id_error_timeclose = self.driver.find_elements(By.ID, "id_error_timeclose")
            self.assertGreater(len(id_error_timeclose), 0, f"{testcase['testcase_name']} faild")
            return
        
        # Find elements activity_dates
        activity_dates = self.driver.find_elements(By.CSS_SELECTOR, ".activity-dates > div")
    
        # Case both close day and open day enabled
        if testcase['enable_open_day'] and testcase['enable_close_day']:
            # Activity_dates must have 2 elements
            self.assertEqual(len(activity_dates), 2)
            # Verify the open day and close day match with format in screen
            self.check_quiz_day_output(expected_open_day)
            self.check_quiz_day_output(expected_close_day,2)

        # Case only open_day enabled
        elif testcase['enable_open_day']:
            # Activity_dates must have only 1 element
            self.assertEqual(len(activity_dates), 1)
            self.check_quiz_day_output(expected_open_day)

        # Case only open_day enabled
        elif testcase['enable_close_day']:
            # Activity_dates must have only 1 element
            self.assertEqual(len(activity_dates), 1)
            self.check_quiz_day_output(expected_close_day)
        # Case 
        else:
            # Activity_dates must have only 0 element
            self.assertEqual(len(activity_dates), 0)
    def test(self):
        #Set up pre-condition
        testcases = self.readData()
        self.set_up_driver()
        self.login()

        # Navigate to the first course
        WebDriverWait(self.driver,20).until(EC.element_to_be_clickable(
                                (By.CSS_SELECTOR, ".dashboard-card:nth-child(1) .aalink"))).click()
        # Navigate to the first quiz
        WebDriverWait(self.driver,20).until(EC.element_to_be_clickable(                          
                                (By.CSS_SELECTOR, ".modtype_quiz .aalink"))).click()
        # Loop through each test case in the list of testcases
        for testcase in testcases:
            # Navigate to settings quiz
            WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable(
                                            (By.XPATH, "//a[contains(text(),\'Settings\')]"))).click()
            WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable(
                                            (By.ID, "collapseElement-1"))).click()
            
            # Set up checkbox for enable open day and enable close day
            self.set_checkbox_value("id_timeopen_enabled", testcase['enable_open_day'])
            self.set_checkbox_value("id_timeclose_enabled", testcase['enable_close_day'])
            
            # Fill the select elements of open day if enable_open_day == true
            if testcase['enable_open_day']:
                open_day = testcase['open_day']
                Select(self.driver.find_element(By.ID,"id_timeopen_day")).select_by_value(open_day['day'])
                Select(self.driver.find_element(By.ID,"id_timeopen_month")).select_by_value(open_day['month'])
                Select(self.driver.find_element(By.ID,"id_timeopen_year")).select_by_value(open_day['year'])
                Select(self.driver.find_element(By.ID,"id_timeopen_hour")).select_by_value(open_day['hours'])
                Select(self.driver.find_element(By.ID,"id_timeopen_minute")).select_by_value(open_day['minutes'])
                
                
            # Fill the select elements of close day if enable_close_day == true
            if testcase['enable_close_day']:
                close_day = testcase['close_day']
                Select(self.driver.find_element(By.ID,"id_timeclose_day")).select_by_value(close_day['day'])
                Select(self.driver.find_element(By.ID,"id_timeclose_month")).select_by_value(close_day['month'])
                Select(self.driver.find_element(By.ID,"id_timeclose_year")).select_by_value(close_day['year'])
                Select(self.driver.find_element(By.ID,"id_timeclose_hour")).select_by_value(close_day['hours'])
                Select(self.driver.find_element(By.ID,"id_timeclose_minute")).select_by_value(close_day['minutes'])

            # Click submit button
            submit_btn = WebDriverWait(self.driver,20).until(EC.element_to_be_clickable((By.ID,"id_submitbutton")))
            # Scroll to submit button
            self.driver.execute_script("arguments[0].scrollIntoView();", submit_btn)
            submit_btn.click()
            try:
                # Check the output 
                self.check_output(testcase)
                # Print result
                print(testcase["testcase_name"] + " passed")
            except Exception as e:
                # Print testcase faild
                print (print(testcase["testcase_name"] + " faild"))
            
        # Quit the driver
        self.teardown_method()
    
    

            
if __name__ == "__main__":
  unittest.main(warnings='ignore')

