# import all required frameworks
import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
import os
from selenium.webdriver.chrome.options import Options
# inherit TestCase Class and create a new test class


class UserPictureTest(unittest.TestCase):

    # initialization of webdriver
    def setUp(self):
        current_directory = os.getcwd()
        self.img = [
            os.path.join(current_directory, 'gen', '3.pdf'),
            os.path.join(current_directory, 'gen', '3.pdf'),
            os.path.join(current_directory, 'gen', '4.pdf'),
            os.path.join(current_directory, 'gen', '3.pdf'),
            os.path.join(current_directory, 'gen', '3.pdf'),
            os.path.join(current_directory, 'gen', '4.pdf'),
        ]
        chrome_options = Options()
        chrome_options.add_argument("--start-maximized")
        self.driver = webdriver.Chrome(options=chrome_options)

    def test_case_1(self):
        driver = self.driver
        url = "https://school.moodledemo.net/"
        driver.get(url)
        driver.find_element(By.LINK_TEXT, "Log in").click()
        driver.find_element(By.ID, "username").send_keys("student")
        driver.find_element(By.ID, "password").send_keys("moodle")
        driver.find_element(By.ID, "loginbtn").click()
        driver.find_element(By.LINK_TEXT, "Dashboard").click()
        time.sleep(10)
        driver.find_element(
            By.LINK_TEXT, "From Concept to Reality: Trauma and Film").click()
        time.sleep(5)
        driver.find_element(
            By.XPATH, "//section[@id='region-main']/div[2]/div/div/div/div/form/button"
        ).click()
        time.sleep(20)
        driver.find_element(
            By.CSS_SELECTOR, ".dndupload-message > .dndupload-arrow"
        ).click()
        time.sleep(15)
        driver.find_element(By.NAME, "repo_upload_file").send_keys(self.img[0])
        time.sleep(10)
        driver.find_element(
            By.XPATH, "//div[2]/div/div[2]/div/div/div/button").click()
        time.sleep(5)
        driver.find_element(By.ID, "id_submitbutton").click()
        time.sleep(5)
        driver.find_element(
            By.XPATH, "//section[@id='region-main']/div[2]/div/div/div[2]/div/form/button").click()
        time.sleep(5)
        driver.find_element(
            By.XPATH, "//div[@id='modal-footer']/div/div[2]/form/button"
        ).click()
        time.sleep(5)
        driver.find_element(By.CSS_SELECTOR, ".userpicture").click()
        driver.find_element(By.LINK_TEXT, "Log out")

    def test_case_2(self):
        driver = self.driver
        url = "https://school.moodledemo.net/"
        driver.get(url)
        driver.find_element(By.LINK_TEXT, "Log in").click()
        driver.find_element(By.ID, "username").send_keys("student")
        driver.find_element(By.ID, "password").send_keys("moodle")
        driver.find_element(By.ID, "loginbtn").click()
        driver.find_element(By.LINK_TEXT, "Dashboard").click()
        time.sleep(10)
        driver.find_element(
            By.LINK_TEXT, "From Concept to Reality: Trauma and Film").click()
        time.sleep(10)
        driver.find_element(
            By.XPATH, "//section[@id='region-main']/div[2]/div/div/div/div/form/button"
        ).click()
        time.sleep(20)
        driver.find_element(
            By.XPATH, "//div[4]/div/div[2]/div/div"
        ).click()
        time.sleep(10)
        driver.find_element(By.NAME, "repo_upload_file").send_keys(self.img[1])
        time.sleep(10)
        driver.find_element(
            By.XPATH, "//div[2]/div/div[2]/div/div/div/button").click()
        time.sleep(5)
        driver.find_element(By.ID, "id_submitbutton").click()
        time.sleep(5)
        driver.find_element(By.CSS_SELECTOR, ".userpicture").click()
        driver.find_element(By.LINK_TEXT, "Log out")

    def test_case_3(self):
        driver = self.driver
        url = "https://school.moodledemo.net/"
        driver.get(url)
        driver.find_element(By.LINK_TEXT, "Log in").click()
        driver.find_element(By.ID, "username").send_keys("student")
        driver.find_element(By.ID, "password").send_keys("moodle")
        driver.find_element(By.ID, "loginbtn").click()
        driver.find_element(By.LINK_TEXT, "Dashboard").click()
        time.sleep(10)
        driver.find_element(
            By.LINK_TEXT, "Assignment 02 (16th century)").click()
        time.sleep(10)
        driver.find_element(
            By.XPATH, "//section[@id='region-main']/div[2]/div/div/div/div/form/button"
        ).click()
        time.sleep(20)
        driver.find_element(
            By.XPATH, "//div[4]/div/div[2]/div/div"
        ).click()
        time.sleep(10)
        driver.find_element(By.NAME, "repo_upload_file").send_keys(self.img[2])
        time.sleep(10)
        driver.find_element(
            By.XPATH, "//div[2]/div/div[2]/div/div/div/button").click()
        time.sleep(5)
        driver.find_element(By.ID, "id_submitbutton").click()
        time.sleep(20)
        driver.find_element(By.CSS_SELECTOR, ".userpicture").click()
        driver.find_element(By.LINK_TEXT, "Log out")

    def test_case_4(self):
        driver = self.driver
        url = "https://school.moodledemo.net/"
        driver.get(url)
        driver.find_element(By.LINK_TEXT, "Log in").click()
        driver.find_element(By.ID, "username").send_keys("student")
        driver.find_element(By.ID, "password").send_keys("moodle")
        driver.find_element(By.ID, "loginbtn").click()
        driver.find_element(By.LINK_TEXT, "Dashboard").click()
        time.sleep(10)
        driver.find_element(By.XPATH, "(//button[@type='button'])[6]").click()
        time.sleep(10)
        driver.find_element(
            By.LINK_TEXT, "(Mobile assignment) View from your window").click()
        time.sleep(10)
        driver.find_element(
            By.XPATH, "//section[@id='region-main']/div[2]/div/div/div/div/form/button"
        ).click()
        time.sleep(20)
        driver.find_element(
            By.XPATH, "//div[4]/div/div[2]/div/div"
        ).click()
        time.sleep(10)
        driver.find_element(By.NAME, "repo_upload_file").send_keys(self.img[3])
        time.sleep(10)
        driver.find_element(
            By.XPATH, "//div[2]/div/div[2]/div/div/div/button").click()
        time.sleep(5)
        driver.find_element(By.ID, "id_submitbutton").click()
        time.sleep(20)
        driver.find_element(By.CSS_SELECTOR, ".userpicture").click()
        driver.find_element(By.LINK_TEXT, "Log out")

    def test_case_5(self):
        driver = self.driver
        url = "https://school.moodledemo.net/"
        driver.get(url)
        driver.find_element(By.LINK_TEXT, "Log in").click()
        driver.find_element(By.ID, "username").send_keys("student")
        driver.find_element(By.ID, "password").send_keys("moodle")
        driver.find_element(By.ID, "loginbtn").click()
        driver.find_element(By.LINK_TEXT, "Dashboard").click()
        time.sleep(10)
        driver.find_element(
            By.LINK_TEXT, "Assignment 02 (16th century)").click()
        time.sleep(10)
        driver.find_element(
            By.XPATH, "//section[@id='region-main']/div[2]/div/div/div/div/form/button"
        ).click()
        time.sleep(20)
        driver.find_element(
            By.XPATH, "//div[4]/div/div[2]/div/div"
        ).click()
        time.sleep(15)
        driver.find_element(By.NAME, "repo_upload_file").send_keys(self.img[4])
        time.sleep(10)
        driver.find_element(
            By.XPATH, "//div[2]/div/div[2]/div/div/div/button").click()
        time.sleep(5)
        driver.find_element(By.ID, "id_submitbutton").click()
        time.sleep(5)
        driver.find_element(
            By.XPATH, "//section[@id='region-main']/div[2]/div/div/div[2]/div/form/button").click()
        time.sleep(5)
        driver.find_element(
            By.XPATH, "//div[@id='modal-footer']/div/div[2]/form/button"
        ).click()
        time.sleep(5)
        driver.find_element(By.CSS_SELECTOR, ".userpicture").click()
        driver.find_element(By.LINK_TEXT, "Log out")

    def test_case_6(self):
        driver = self.driver
        url = "https://school.moodledemo.net/"
        driver.get(url)
        driver.find_element(By.LINK_TEXT, "Log in").click()
        driver.find_element(By.ID, "username").send_keys("student")
        driver.find_element(By.ID, "password").send_keys("moodle")
        driver.find_element(By.ID, "loginbtn").click()
        driver.find_element(By.LINK_TEXT, "Dashboard").click()
        time.sleep(10)
        driver.find_element(
            By.LINK_TEXT, "From Concept to Reality: Trauma and Film").click()
        time.sleep(10)
        driver.find_element(
            By.XPATH, "//section[@id='region-main']/div[2]/div/div/div/div/form/button"
        ).click()
        time.sleep(20)
        driver.find_element(
            By.XPATH, "//div[4]/div/div[2]/div/div"
        ).click()
        time.sleep(10)
        driver.find_element(By.NAME, "repo_upload_file").send_keys(self.img[5])
        time.sleep(10)
        driver.find_element(
            By.XPATH, "//div[2]/div/div[2]/div/div/div/button").click()
        time.sleep(5)
        driver.find_element(By.ID, "id_submitbutton").click()
        time.sleep(20)
        driver.find_element(By.CSS_SELECTOR, ".userpicture").click()
        driver.find_element(By.LINK_TEXT, "Log out")

    # cleanup method called after every test performed

    def tearDown(self):
        self.driver.close()


# execute the script
if __name__ == "__main__":
    unittest.main()
