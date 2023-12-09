from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

def test_case_3():
    try:
        # Initialize ChromeDriver
        driver = webdriver.Chrome(service=Service('path/to/chromedriver'))
        driver.get("https://sandbox401.moodledemo.net")

        # Click on the course link
        course = driver.find_element(By.CSS_SELECTOR, ".aalink")
        course.click()

        # Enter username and password
        usernameInput = driver.find_element(By.ID, "username")
        usernameInput.send_keys("teacher")
        passwordInput = driver.find_element(By.ID, "password")
        passwordInput.send_keys("sandbox")
        loginButton = driver.find_element(By.ID, "loginbtn")
        loginButton.click()

        # Click on the setting link
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

        # Uncheck the checkbox if it is checked
        checkbox = driver.find_element(By.ID, "id_enddate_enabled")
        if checkbox.is_selected():
            checkbox.click()

        # Set the end date and time
        enddate = driver.find_element(By.ID, "id_enddate_day")
        enddate.click()
        select6 = Select(enddate)
        select6.select_by_visible_text("9")

        endmonth = driver.find_element(By.ID, "id_enddate_month")
        endmonth.click()
        select7 = Select(endmonth)
        select7.select_by_visible_text("May")

        endyear = driver.find_element(By.ID, "id_enddate_year")
        endyear.click()
        select8 = Select(endyear)
        select8.select_by_visible_text("2023")

        endhour = driver.find_element(By.ID, "id_enddate_hour")
        endhour.click()
        select9 = Select(endhour)
        select9.select_by_visible_text("12")

        endminute = driver.find_element(By.ID, "id_enddate_minute")
        endminute.click()
        select10 = Select(endminute)
        select10.select_by_visible_text("00")

        # Click on the submit button
        submit = driver.find_element(By.ID, "id_saveanddisplay")
        submit.click()

        print("Test 3: Pass")

    except Exception as e:
        print("Test 3: Failed")
        print(e)

# Main function
if __name__ == "__main__":
    test_case_3()