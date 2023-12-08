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
    
  def teardown_method(self):
    self.driver.quit()
  
  def test_level1_boundary(self):
    count = 0
    
    with open("./equivalence.csv", 'r') as file:
        csvreader = csv.reader(file)
        for row in csvreader:
            if count != 0:
                self.set_up_drive()
                self.driver.get(f"{row[2]}")
                self.driver.find_element(By.LINK_TEXT, f"{row[3]}").click()
                self.driver.find_element(By.ID, f"{row[9]}").send_keys(f"{row[13]}") 
                self.driver.find_element(By.ID, f"{row[10]}").send_keys(f"{row[14]}")
                self.driver.find_element(By.ID, f"{row[11]}").click()
                time.sleep(10)
                self.driver.find_element(By.LINK_TEXT, f"{row[4]}").click()
                self.driver.find_element(By.LINK_TEXT, f"{row[5]}").click()
                self.driver.find_element(By.LINK_TEXT, f"{row[6]}").click()
                self.driver.find_element(By.XPATH, f"{row[7]}").click()
                time.sleep(10)
                self.driver.find_element(By.ID, f"{row[12]}").clear()
                self.driver.find_element(By.ID, f"{row[12]}").send_keys(f"{row[1]}")
                time.sleep(10)
                self.driver.find_element(By.XPATH, f"{row[8]}").click()
                time.sleep(10)
                self.teardown_method()
                print(f"Test {count}: Pass")
                time.sleep(5)
            count += 1

  
if __name__ == "__main__":
  unittest.main(warnings='ignore')
