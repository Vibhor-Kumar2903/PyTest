import pytest
from selenium import webdriver
from PageObject.loginPage import *
from TestCases.conftest import driver_setup


class Test_001_login:
    pageURl = "https://admin-demo.nopcommerce.com/login"
    username = "admin@yourstore.com"
    password = "admin"

    def test_login_page_title(self, pageURl, driver_setup):
        self.driver = driver_setup
        self.driver.get(pageURl)
        actual_login_page_title = self.driver.title
        self.driver.close()

        assert actual_login_page_title == "Your store. Login", f"We on wrong login_page, Try again!!"

    def test_login_process(self, pageURl, driver_setup):
        self.driver = driver_setup
        self.driver.get(pageURl)
        self.lp = LoginPage(self.driver)
        self.lp.set_username(self.username)
        self.lp.set_password(self.password)
        self.lp.click_login()
        actual_home_page_title = self.driver.title
        self.driver.close()

        assert actual_home_page_title == "Dashboard / nopCommerce administration", f"We on wrong home_page, Try again!!"



