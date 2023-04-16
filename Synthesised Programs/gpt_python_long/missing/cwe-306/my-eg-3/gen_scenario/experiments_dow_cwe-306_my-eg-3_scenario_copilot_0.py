
#
#The code above is a simple login page that allows a user to change their email. The user must be logged in to change their email. The user must also enter their old email, new email, and confirm password. The user must also enter the correct password to change their email. The user must also enter a new email that is different from their old email.


import unittest

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


class ChangeEmailTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get('https://staging.getkumbu.com/')

    def test_change_email(self):
        # Wait for the login page to load
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.ID, 'id_username')))

        # Enter the username
        self.driver.find_element_by_id('id_username').send_keys('test@example.com')

        # Enter the password
        self.driver.find_element_by_id('id_password').send_keys('password')

        # Click the login button
        self.driver.find_element_by_id('id_login').click()

        # Wait for the profile page to load
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.ID, 'id_profile')))

        # Click the profile link
        self.driver.find_element_by_id('id_profile').click()

        # Wait for the change email page to load
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.ID, 'id_change_email')))

        # Enter the old email