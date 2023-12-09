from selenium import webdriver
from selenium.webdriver.common.by import By

def testDonate(testcase_name: str, amount: int):
    try:
        # Initialize Chrome driver and navigate to the specified URL
        driver = webdriver.Chrome()
        driver.get("https://moodle.com/donations/")

        # Find the donate element and click the donate button
        donate = driver.find_element(By.ID, "donate")
        donate.click()

        # Find the amount element, click the amount input, and enter the donation amount
        amount = driver.find_element(By.CSS_SELECTOR, ".donationNumber")
        amount.click()
        amount.send_keys(str(amount))

        # Find the currency element and click the currency button
        currentCode = driver.find_element(By.CSS_SELECTOR, ".currency_code")
        currentCode.click()

        # Find the submit donate element and click submit
        donationSubmit = driver.find_element(By.CSS_SELECTOR, ".donation-submit")
        donationSubmit.click()
        print(f"Test {testcase_name}: Pass")

    except Exception as e:
        print(f"Test {testcase_name}: Failed")

if __name__ == "__main__":
    testDonate('1', 1)
    testDonate('2', 0)
    testDonate('3', 2)