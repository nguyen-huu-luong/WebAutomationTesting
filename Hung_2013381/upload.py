# import all required frameworks
import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
import os

# inherit TestCase Class and create a new test class


class UserPictureTest(unittest.TestCase):

    # initialization of webdriver
    def setUp(self):
        current_directory = os.getcwd()
        self.img = [
            os.path.join(current_directory, 'img', '1.png'),
        ]
        self.driver = webdriver.Chrome()

    def test_case_1(self):
        driver = self.driver
        url = "https://school.moodledemo.net/user/edit.php?id=13&returnto=profile"
        driver.get(url)
        driver.find_element(By.ID, "username").send_keys("teacher")
        driver.find_element(By.ID, "password").send_keys("moodle")
        driver.find_element(By.ID, "loginbtn").click()
        driver.find_element(By.ID, "collapseElement-0").click()
        time.sleep(3)
        driver.find_element(
            By.CSS_SELECTOR, ".dndupload-message").find_element(By.XPATH, "div[1]").click()
        time.sleep(3)
        driver.find_element(By.NAME, "repo_upload_file").send_keys(self.img[0])
        time.sleep(3)
        driver.find_element(
            By.XPATH, "//button[contains(text(), 'Upload this file')]").click()
        time.sleep(3)
        driver.find_element(
            By.XPATH, "//input[contains(@value, 'Update profile')]").click()

        assert "Changes saved" in driver.page_source

    def test_case_2(self):
        driver = self.driver
        url = "https://school.moodledemo.net/user/edit.php?id=13&returnto=profile"
        driver.get(url)
        driver.find_element(By.ID, "username").send_keys("teacher")
        driver.find_element(By.ID, "password").send_keys("moodle")
        driver.find_element(By.ID, "loginbtn").click()
        driver.find_element(By.ID, "collapseElement-0").click()
        time.sleep(3)
        driver.find_element(
            By.CSS_SELECTOR, ".dndupload-message").find_element(By.XPATH, "div[1]").click()
        time.sleep(3)
        driver.find_element(By.NAME, "repo_upload_file").send_keys(self.img[0])
        time.sleep(3)
        driver.find_element(
            By.XPATH, "//button[contains(text(), 'Upload this file')]").click()
        time.sleep(3)
        driver.find_element(
            By.XPATH, "//input[contains(@value, 'Update profile')]").click()

        assert "Changes saved" in driver.page_source

    def test_case_3(self):
        driver = self.driver
        url = "https://school.moodledemo.net/user/edit.php?id=13&returnto=profile"
        driver.get(url)
        driver.find_element(By.ID, "username").send_keys("teacher")
        driver.find_element(By.ID, "password").send_keys("moodle")
        driver.find_element(By.ID, "loginbtn").click()
        driver.find_element(By.ID, "collapseElement-0").click()
        time.sleep(3)
        driver.find_element(
            By.CSS_SELECTOR, ".dndupload-message").find_element(By.XPATH, "div[1]").click()
        time.sleep(3)
        driver.find_element(By.NAME, "repo_upload_file").send_keys(self.img[0])
        time.sleep(3)
        driver.find_element(
            By.XPATH, "//button[contains(text(), 'Upload this file')]").click()
        time.sleep(3)
        driver.find_element(
            By.XPATH, "//input[contains(@value, 'Update profile')]").click()

        assert "Changes saved" in driver.page_source

    def test_case_4(self):
        driver = self.driver
        url = "https://school.moodledemo.net/user/edit.php?id=13&returnto=profile"
        driver.get(url)
        driver.find_element(By.ID, "username").send_keys("teacher")
        driver.find_element(By.ID, "password").send_keys("moodle")
        driver.find_element(By.ID, "loginbtn").click()
        driver.find_element(By.ID, "collapseElement-0").click()
        time.sleep(3)
        driver.find_element(
            By.CSS_SELECTOR, ".dndupload-message").find_element(By.XPATH, "div[1]").click()
        time.sleep(3)
        driver.find_element(By.NAME, "repo_upload_file").send_keys(self.img[0])
        time.sleep(3)
        driver.find_element(
            By.XPATH, "//button[contains(text(), 'Upload this file')]").click()
        time.sleep(3)
        driver.find_element(
            By.XPATH, "//input[contains(@value, 'Update profile')]").click()

        assert "Changes saved" in driver.page_source

    def test_case_5(self):
        driver = self.driver
        url = "https://school.moodledemo.net/user/edit.php?id=13&returnto=profile"
        driver.get(url)
        driver.find_element(By.ID, "username").send_keys("teacher")
        driver.find_element(By.ID, "password").send_keys("moodle")
        driver.find_element(By.ID, "loginbtn").click()
        driver.find_element(By.ID, "collapseElement-0").click()
        time.sleep(3)
        driver.find_element(
            By.CSS_SELECTOR, ".dndupload-message").find_element(By.XPATH, "div[1]").click()
        time.sleep(3)
        driver.find_element(By.NAME, "repo_upload_file").send_keys(self.img[0])
        time.sleep(3)
        driver.find_element(
            By.XPATH, "//button[contains(text(), 'Upload this file')]").click()
        time.sleep(3)
        driver.find_element(
            By.XPATH, "//input[contains(@value, 'Update profile')]").click()

        assert "Changes saved" in driver.page_source

    # cleanup method called after every test performed

    def tearDown(self):
        self.driver.close()


# execute the script
if __name__ == "__main__":
    unittest.main()
