import unittest
import time
import csv
import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class UploadFileToCourseEquivalenceClass(unittest.TestCase): 
    
    def __init__(self, arg):
        super().__init__(arg)

    def set_up_driver(self):
        options = webdriver.ChromeOptions()
        options.add_experimental_option('excludeSwitches', ['enable-logging'])
        options.add_argument("--disable-popup-blocking")
        self.driver = webdriver.Chrome(options=options)
        self.vars = {}
        self.base_url = "https://school.moodledemo.net/"
        self.max_file_size_mb = 10
        self.driver.get(self.base_url)

    def teardown_method(self):
        self.driver.quit()
        self.clear_files_in_directory(os.path.join(os.getcwd(), 'test_files'))

    def login(self):
        self.driver.find_element(By.LINK_TEXT, "Log in").click()
        self.driver.find_element(By.ID, "username").send_keys("teacher") 
        self.driver.find_element(By.ID, "password").send_keys("moodle")
        self.driver.find_element(By.ID, "loginbtn").click()
        time.sleep(5)

    def edit_maximum_file(self):
        # Navigate to the first course
        WebDriverWait(self.driver,20).until(EC.visibility_of_element_located(
                                            (By.CSS_SELECTOR, ".dashboard-card:nth-child(1) .aalink"))).click()
        #Navigate to course setting
        WebDriverWait(self.driver,20).until(EC.element_to_be_clickable((By.LINK_TEXT, "Settings"))).click()
        #Expand the setting of file and resources
        WebDriverWait(self.driver,20).until(EC.element_to_be_clickable((By.ID, "collapseElement-4"))).click()
        #Wait the maxbytes input clickable
        WebDriverWait(self.driver,20).until(EC.element_to_be_clickable((By.ID, "id_maxbytes"))).click()
        # Select id_maxbytes input
        dropdown = Select(self.driver.find_element(By.ID, "id_maxbytes"))
        # Send value 
        dropdown.select_by_value(str(1024*1024*self.max_file_size_mb)) # covert 10MB to bytes
        # submit change
        WebDriverWait(self.driver,20).until(EC.element_to_be_clickable((By.ID, "id_saveanddisplay"))).click()
        # Navigate to home page
        self.driver.get(self.base_url) 
    def set_up_files(self):
        #Create sub folder test_files at current directory
        self.test_files_subfolder = os.path.join(os.getcwd(), 'test_files')
        if not os.path.exists(self.test_files_subfolder):
            os.makedirs(self.test_files_subfolder)
    
    def clear_files_in_directory(self, directory_path):
        try:
            # Get the list of files in the directory
            files = os.listdir(directory_path)

            # Iterate over each file and remove it
            for file_name in files:
                file_path = os.path.join(directory_path, file_name)
                os.remove(file_path)

            print(f"Files in '{directory_path}' have been cleared.")
        except Exception as e:
            print(f"Error clearing files: {str(e)}")

    def create_file(self, file_name, file_size_mb):
        if file_name and file_size_mb:
            file_path = os.path.join(self.test_files_subfolder, file_name)
            file_size_mb = int(file_size_mb)
            file_size_bytes = file_size_mb * 1024 * 1024  # Convert MB to bytes

            with open(file_path, 'wb') as file:
                # Generate random data and write to the file
                file.write(os.urandom(file_size_bytes))

    def check_output(self, testcase):
        # Case not provide file_name
        if not testcase['file_name']:
            # File element of error_name
            WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located((By.ID, "id_error_name")))
            error_element = self.driver.find_elements(By.ID, "id_error_name")
            # Expect the error name element must be present in the screen 
            self.assertGreater(len(error_element), 0)
        
        # Case not upload file
        elif  int(testcase['file_size_mb']) == 0:
            # File element of id_error_files:
            WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located((By.ID, "id_error_files")))
            error_element = self.driver.find_elements(By.ID, "id_error_files")
            # Expect the error files element must be present in the screen 
            self.assertGreater(len(error_element), 0)
        # Case upload file successfully
        else: 
            link_to_file = WebDriverWait(self.driver, 20).until(EC.presence_of_element_located(
                                            (By.LINK_TEXT, f"file_{testcase['file_size_mb']}mb.txt"))).text
            #Expect the file show at the screen equal the file uploaded
            self.assertEqual(f"file_{testcase['file_size_mb']}mb.txt", link_to_file)

    def test(self):
        # Set up pre-condition
        self.set_up_driver()
        self.login()
        # Create folder to store test_files
        self.set_up_files()
        # Edit maximum of upload file
        self.edit_maximum_file()

        # Read testcase data from data.csv
        with open('data.csv', newline='', encoding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                testcase_name = row['testcase_name']
                file_name = row['file_name']
                file_size_mb = row['file_size_mb']

                # Go to course
                WebDriverWait(self.driver,20).until(EC.visibility_of_element_located(
                                            (By.CSS_SELECTOR, ".dashboard-card:nth-child(1) .aalink"))).click()

                # Set up Edit mode
                setmode_element = self.driver.find_element(By.NAME, "setmode")
                if not setmode_element.is_selected():
                    setmode_element.click()
                
                # Click "Add activity or resource to course"
                WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable(
                    (By.CSS_SELECTOR, "#coursecontentcollapse0 > .btn"))).click()
                
                # Navigate to upload file page
                WebDriverWait(self.driver,20).until(EC.element_to_be_clickable((By.LINK_TEXT, "File"))).click()

                # Check the testcase has file_name or not
                if file_name:
                    # Fill the file_name if has file_name
                    WebDriverWait(self.driver,20).until(EC.visibility_of_element_located(
                                                            (By.ID, "id_name"))).send_keys(file_name)
                # Upload file if testcase has file_size_mb > 0
                if (int(file_size_mb) > 0):
                    # Create file to test
                    self.create_file(f"file_{file_size_mb}mb.txt", file_size_mb)

                    # Click file button to upload
                    WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable(
                        (By.CSS_SELECTOR, ".fp-btn-add .btn"))).click()
                    # Click "Upload a file" to upload the file in the computer
                    WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable(
                        (By.XPATH, "//span[contains(.,\'Upload a file\')]"))).click()
                    
                    # upload created test file
                    WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located(
                                                    (By.NAME, "repo_upload_file"))).send_keys(
                                                            os.getcwd() + f"/test_files/file_{file_size_mb}mb.txt")
                    
                    # Click Upload this file to complete the file upload process
                    WebDriverWait(self.driver, 200).until(EC.element_to_be_clickable(
                        (By.XPATH, "//button[contains(.,'Upload this file')]"))).click()
                    
                    # Check expected output if upload the overload file
                    if (int(file_size_mb) > self.max_file_size_mb):
                        # Wait the file upload to website (maximum = 50s)
                        WebDriverWait(self.driver, 50).until(EC.visibility_of_element_located(
                                                            (By.CLASS_NAME, "moodle-exception-message")))
                        # Expect moodle-exception-message must be present
                        exception_messages = self.driver.find_elements(By.CLASS_NAME, "moodle-exception-message")
                        self.assertGreater(len(exception_messages), 0)
                        # Print result after check
                        print(f"{testcase_name} passed")

                        # Go to home page
                        self.driver.get(self.base_url) 
                        # handle the comfirmation alert if it presents
                        try:
                            WebDriverWait(self.driver, 5).until (EC.alert_is_present())
                            alert  = self.driver.switch_to.alert
                            alert.accept()
                        finally: 
                            # Go to next testcase
                            continue

                # submit
                # Click submit button
                submit_btn = WebDriverWait(self.driver,20).until(EC.element_to_be_clickable((By.ID,"id_submitbutton")))
                # Scroll to submit button
                self.driver.execute_script("arguments[0].scrollIntoView();", submit_btn)
                submit_btn.click()
                
                # Check output
                self.check_output(row)
                time.sleep(5)
                print(f"{testcase_name} passed")

                # Go to home page
                self.driver.get(self.base_url) 
        # Quiz driver
        self.teardown_method()
if __name__ == "__main__":
    unittest.main(warnings='ignore')
