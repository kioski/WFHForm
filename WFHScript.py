import unittest
import time
import datetime
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class WFHForm(unittest.TestCase):


    def setUp(self):
        self.driver = webdriver.Chrome(executable_path='D:/webdriver/chromedriver') 

    def test_InputDetails(self):

        driver = self.driver
        wait = WebDriverWait(driver, 30)
        driver.get('https://docs.google.com/forms/d/e/1FAIpQLSfghgKNZGJnGDRAnRav3MFXo5ag-_Dqr8Xrjm31txH41xqH2w/viewform')
        element = wait.until(EC.element_to_be_clickable((By.ID, 'identifierId')))
        driver.find_element_by_name('identifier').send_keys('input Email')
        driver.find_element_by_class_name('RveJvd ').click()

        element = wait.until(EC.element_to_be_clickable((By.NAME, 'password')))

        driver.find_element_by_name('password').send_keys('input Password')
        driver.find_element_by_class_name('RveJvd ').click()

        element = wait.until(EC.element_to_be_clickable((By.NAME, 'entry.1079644909')))
        element = wait.until(EC.element_to_be_clickable((By.NAME, 'entry.1657213194')))
        element = wait.until(EC.element_to_be_clickable((By.NAME, 'entry.905601746')))

        driver.find_element_by_name('entry.1079644909').send_keys('Your Name')
        driver.find_element_by_name('entry.1657213194').send_keys('QA TEAM')
        driver.find_element_by_name('entry.905601746').send_keys('QA ENGINEER')

        date = datetime.datetime.now()
        date_time = driver.find_element_by_class_name("freebirdFormviewerViewItemsDateDateInputs").find_elements_by_tag_name("input")

        # date_time[0].click()
        date_time[0].send_keys(date.strftime("%m"+"/"+"%d"+"/"+"%Y"))

        Task = input("What is your Task Today?")
        driver.find_element_by_name('entry.1486595092').send_keys(Task)

        driver.find_element_by_name('entry.1549400536').send_keys('COVID-19')
        driver.find_element_by_name('entry.754030951').send_keys('MMP')
        driver.find_element_by_name('entry.770526695').send_keys('8')
        driver.find_element_by_class_name("freebirdFormviewerViewNavigationNavControls").find_elements_by_tag_name("div")[2].click()
 
        element = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, 'isCheckedNext')))
        element2 = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, 'isUndragged')))
        driver.find_element_by_class_name("freebirdFormviewerViewNavigationNavControls").find_elements_by_tag_name("span")[0].click()

        time.sleep(3)

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()


