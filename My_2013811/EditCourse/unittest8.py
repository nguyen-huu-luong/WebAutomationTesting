from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

def test_case_8():
    try:
        # Initialize ChromeDriver
        driver = webdriver.Chrome(service=Service('path/to/chromedriver'))
        driver.get("http://ww62.selenium.by/")

        # Find and click on the course link
        course = driver.find_element(By.CSS_SELECTOR, ".aalink")
        course.click()

        # Enter username and password
        usernameInput = driver.find_element(By.ID, "username")
        usernameInput.send_keys("teacher")
        passwordInput = driver.find_element(By.ID, "password")
        passwordInput.send_keys("sandbox")
        loginButton = driver.find_element(By.ID, "loginbtn")
        loginButton.click()

        # Find and click on the setting link
        listOpt = driver.find_elements(By.CSS_SELECTOR, ".nav-link")
        setting = listOpt[8]
        setting.click()

        # Set the fullname and shortname
        fullname = driver.find_element(By.ID, "id_fullname")
        fullname.click()
        shortname = driver.find_element(By.ID, "id_shortname")
        shortname.click()

        # Set the start date and time
        startdate = driver.find_element(By.ID, "id_startdate_day")
        startdate.click()
        select1 = Select(startdate)
        select1.select_by_visible_text("9")

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

        # Check the checkbox if it is checked
        checkbox = driver.find_element(By.ID, "id_enddate_enabled")
        if checkbox.is_selected():
            checkbox.click()

        # Click on the submit button
        submit = driver.find_element(By.ID, "id_saveanddisplay")
        submit.click()

        print("Test 8: Pass")

    except Exception as e:
        print("Test 8: Failed")
        print(e)

# Main function
if __name__ == "__main__":
    test_case_8()