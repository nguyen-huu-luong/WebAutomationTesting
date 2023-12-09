from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import Select
import time

def test_case_1():
    try:
        # Khoi dong chrome va truy cap vo link duoc gan
        driver = webdriver.Chrome(service=Service('path/to/chromedriver'))
        driver.get("https://sandbox401.moodledemo.net")

        # click chon my first course
        course = driver.find_element(By.CSS_SELECTOR, ".aalink")
        course.click()

        # dang nhap tai khoan voi vai tro teacher
        usernameInput = driver.find_element(By.ID, "username")
        usernameInput.send_keys("teacher")
        passwordInput = driver.find_element(By.ID, "password")
        passwordInput.send_keys("sandbox")
        loginButton = driver.find_element(By.ID, "loginbtn")
        loginButton.click()

        # click setting de chinh sua khoa hoc
        listOpt = driver.find_elements(By.CSS_SELECTOR, ".nav-link")
        setting = listOpt[8]
        setting.click()

        # dat ten khoa hoc
        fullname = driver.find_element(By.ID, "id_fullname")
        fullname.click()
        # dat ten viet tat cho khoa hoc
        shortname = driver.find_element(By.ID, "id_shortname")
        shortname.click()

        # dat thoi gian bat dau khoa hoc
        startdate = driver.find_element(By.ID, "id_startdate_day")
        startdate.click()
        select1 = Select(startdate)
        select1.select_by_visible_text("1")

        startmonth = driver.find_element(By.ID, "id_startdate_month")
        startmonth.click()
        select2 = Select(startmonth)
        select2.select_by_visible_text("January")

        startyear = driver.find_element(By.ID, "id_startdate_year")
        startyear.click()
        select3 = Select(startyear)
        select3.select_by_visible_text("2023")

        starthour = driver.find_element(By.ID, "id_startdate_hour")
        starthour.click()
        select4 = Select(starthour)
        select4.select_by_visible_text("12")

        startminute = driver.find_element(By.ID, "id_startdate_minute")
        startminute.click()
        select5 = Select(startminute)
        select5.select_by_visible_text("00")

        # enabale = False
        checkbox = driver.find_element(By.ID, "id_enddate_enabled")
        if checkbox.is_selected():
            checkbox.click()

        # luu thay doi khoa hoc
        submit = driver.find_element(By.ID, "id_saveanddisplay")
        submit.click()

        print("Test 1: Pass")

    except Exception as e:
        print("Test 1: Failed")
        print(e)

# Main function
if __name__ == "__main__":
    test_case_1()  