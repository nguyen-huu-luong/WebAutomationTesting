import unittest
import time
import csv
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from datetime import datetime
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class EditQuizBoundaryValue(unittest.TestCase): 
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
    
    def test(self):
        #Set up pre-condition
        self.set_up_driver()
        self.login()

        # navigate to the first course
        WebDriverWait(self.driver,20).until(EC.element_to_be_clickable(
                                        (By.CSS_SELECTOR, ".dashboard-card:nth-child(1) .aalink"))).click()
        #navigate to the first quiz
        WebDriverWait(self.driver,20).until(EC.element_to_be_clickable(
                                        (By.CSS_SELECTOR, ".modtype_quiz .aalink"))).click()
        # Read data from file csv
        with open("./boundary.csv", 'r') as file:
            csvreader = csv.reader(file)
            header = next(csvreader)  # Read the header
            for row in csvreader:
                # Navigate to settings 
                WebDriverWait(self.driver,20).until(EC.element_to_be_clickable(
                                                (By.XPATH, "//a[contains(text(),\'Settings\')]"))).click()

                # Waiting for page load and click to the collapse Element 
                WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable(
                                                        (By.ID, "collapseElement-1"))).click()
                
                # Waiting for id_timeopen_enabled to be visible 
                WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located(
                                                        (By.ID, "id_timeopen_enabled")))
                # Ensure enabled openday checkbox to be check
                enabled_checkbox = self.driver.find_element(By.ID, "id_timeopen_enabled")
                if not enabled_checkbox.is_selected(): 
                    enabled_checkbox.click()
                
                # Send the value in testcase to the input correspondingly
                day_element =Select( self.driver.find_element(By.ID, "id_timeopen_day"))
                month_element =Select( self.driver.find_element(By.ID, "id_timeopen_month"))
                year_element =Select( self.driver.find_element(By.ID, "id_timeopen_year"))
                hours_element =Select( self.driver.find_element(By.ID, "id_timeopen_hour"))
                minutes_element =Select( self.driver.find_element(By.ID, "id_timeopen_minute"))
                day_element.select_by_value(row[1])
                month_element.select_by_value(row[2])
                year_element.select_by_value(row[3])
                hours_element.select_by_value(row[4])
                minutes_element.select_by_value(row[5])

                # Waiting to the submit button can be clicked and click to submit 
                WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((
                                                        By.ID, "id_submitbutton"))).click()

                # Check output after submit
                ## Format testcase as expected output
                expected_output = self.format_date(row[1], row[2], row[3], row[4], row[5])
                ## Find the time open quiz element at quiz page
                WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located(
                                                (By.CSS_SELECTOR, ".activity-dates > div:nth-child(1)")))
                
                ## Get text of the time open quiz showing in the screen
                actual_date = self.driver.find_element(By.CSS_SELECTOR, 
                                                        ".activity-dates > div:nth-child(1)").text

                ## Assert that this text contain the expected output
                self.assertIn(expected_output, actual_date, f"{row[0]} faild")

                ## Print result
                print(f"{row[0]} passed")
                time.sleep(2)

        # Quit the driver    
        self.teardown_method()

if __name__ == "__main__":
  unittest.main(warnings='ignore')