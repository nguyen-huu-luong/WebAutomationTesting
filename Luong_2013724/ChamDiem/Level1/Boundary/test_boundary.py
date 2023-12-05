from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
import os 
import unittest
import csv
import time

class TestTest4(unittest.TestCase):
  def __init__(self, arg):
    super().__init__(arg)
    
  def set_up_drive(self):
    options = webdriver.ChromeOptions()
    options.add_experimental_option('excludeSwitches', ['enable-logging'])
    self.driver = webdriver.Chrome(options=options)
    self.vars = {}
    self.driver.get("https://school.moodledemo.net/mod/assign/view.php?id=775")
    self.driver.find_element(By.LINK_TEXT, "Log in").click()
    self.driver.find_element(By.ID, "username").send_keys("teacher") 
    self.driver.find_element(By.ID, "password").send_keys("moodle")
    self.driver.find_element(By.ID, "loginbtn").click()
    time.sleep(10)
    
  def teardown_method(self):
    self.driver.quit()
  
  def test_level1_boundary(self):
    count = 0
    
    with open("./boundary.csv", 'r') as file:
        csvreader = csv.reader(file)
        for row in csvreader:
            if count != 0:
                self.set_up_drive()
                self.driver.find_element(By.LINK_TEXT, "Assignment: Languages of Love").click()
                self.driver.find_element(By.LINK_TEXT, "View all submissions").click()
                self.driver.find_element(By.LINK_TEXT, "Grade").click()
                self.driver.find_element(By.XPATH, "//section/div[2]/div[3]").click()
                time.sleep(10)
                self.driver.find_element(By.ID, "id_grade").clear()
                self.driver.find_element(By.ID, "id_grade").send_keys(f"{row[1]}")
                time.sleep(10)
                self.driver.find_element(By.XPATH, "//button[contains(.,\'Save changes\')]").click()
                time.sleep(10)
                self.teardown_method()
                print(f"Test {count}: Pass")
                time.sleep(5)
            count += 1

  
if __name__ == "__main__":
  unittest.main(warnings='ignore')
