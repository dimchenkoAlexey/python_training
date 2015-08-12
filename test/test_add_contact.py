# -*- coding: utf-8 -*-
import unittest

from model.contact import Contact
from selenium.webdriver.firefox.webdriver import WebDriver


def is_alert_present(wd):
    try:
        wd.switch_to_alert().text
        return True
    except:
        return False


class TestAddContact(unittest.TestCase):
    def setUp(self):
        self.wd = WebDriver()
        self.wd.implicitly_wait(60)

    def open_home_page(self, wd):
        # open home page
        wd.get("http://localhost/addressbook/")

    def login(self, wd, username, password):
        # login
        wd.find_element_by_name("user").click()
        wd.find_element_by_name("user").clear()
        wd.find_element_by_name("user").send_keys(username)
        wd.find_element_by_name("pass").click()
        wd.find_element_by_name("pass").clear()
        wd.find_element_by_name("pass").send_keys(password)
        wd.find_element_by_css_selector("input[type=\"submit\"]").click()

    def create_new_contact(self, wd, contact):
        # create new contact
        wd.find_element_by_link_text("add new").click()
        wd.find_element_by_name("firstname").click()
        wd.find_element_by_name("firstname").clear()
        wd.find_element_by_name("firstname").send_keys(contact.firstname)
        wd.find_element_by_name("middlename").click()
        wd.find_element_by_name("middlename").clear()
        wd.find_element_by_name("middlename").send_keys(contact.middlename)
        wd.find_element_by_name("lastname").click()
        wd.find_element_by_name("lastname").clear()
        wd.find_element_by_name("lastname").send_keys(contact.lastname)
        wd.find_element_by_name("nickname").click()
        wd.find_element_by_name("nickname").clear()
        wd.find_element_by_name("nickname").send_keys(contact.nickname)
        wd.find_element_by_name("title").click()
        wd.find_element_by_name("title").clear()
        wd.find_element_by_name("title").send_keys(contact.title)
        wd.find_element_by_name("company").click()
        wd.find_element_by_name("company").clear()
        wd.find_element_by_name("company").send_keys(contact.company)
        wd.find_element_by_name("address").click()
        wd.find_element_by_name("address").clear()
        wd.find_element_by_name("address").send_keys(contact.address)
        wd.find_element_by_name("home").click()
        wd.find_element_by_name("home").clear()
        wd.find_element_by_name("home").send_keys(contact.phone_home)
        wd.find_element_by_name("mobile").click()
        wd.find_element_by_name("mobile").clear()
        wd.find_element_by_name("mobile").send_keys(contact.phone_mobile)
        wd.find_element_by_name("work").click()
        wd.find_element_by_name("work").clear()
        wd.find_element_by_name("work").send_keys(contact.phone_work)
        wd.find_element_by_name("fax").click()
        wd.find_element_by_name("fax").clear()
        wd.find_element_by_name("fax").send_keys(contact.fax)
        wd.find_element_by_name("email").click()
        wd.find_element_by_name("email").clear()
        wd.find_element_by_name("email").send_keys(contact.email_first)
        wd.find_element_by_name("email2").click()
        wd.find_element_by_name("email2").clear()
        wd.find_element_by_name("email2").send_keys(contact.email_second)
        wd.find_element_by_name("email3").click()
        wd.find_element_by_name("email3").clear()
        wd.find_element_by_name("email3").send_keys(contact.email_third)
        wd.find_element_by_name("homepage").click()
        wd.find_element_by_name("homepage").clear()
        wd.find_element_by_name("homepage").send_keys(contact.homepage)
        birth_day_xpath = "//div[@id='content']/form/select[1]//option[" + contact.birth_day_list_item + "]"
        if not wd.find_element_by_xpath(birth_day_xpath).is_selected():
            wd.find_element_by_xpath(birth_day_xpath).click()
        birth_month_xpath = "//div[@id='content']/form/select[2]//option[" + contact.birth_month_list_item + "]"
        if not wd.find_element_by_xpath(birth_month_xpath).is_selected():
            wd.find_element_by_xpath(birth_month_xpath).click()
        wd.find_element_by_name("byear").click()
        wd.find_element_by_name("byear").clear()
        wd.find_element_by_name("byear").send_keys(contact.birth_year)
        anniversary_day_xpath = "//div[@id='content']/form/select[3]//option[" + contact.anniversary_day_list_item + "]"
        if not wd.find_element_by_xpath(anniversary_day_xpath).is_selected():
            wd.find_element_by_xpath(anniversary_day_xpath).click()
        anniversary_month_xpath = "//div[@id='content']/form/select[4]//option[" + contact.anniversary_month_list_item + "]"
        if not wd.find_element_by_xpath(anniversary_month_xpath).is_selected():
            wd.find_element_by_xpath(anniversary_month_xpath).click()
        wd.find_element_by_name("ayear").click()
        wd.find_element_by_name("ayear").clear()
        wd.find_element_by_name("ayear").send_keys(contact.anniversary_year)
        wd.find_element_by_name("address2").click()
        wd.find_element_by_name("address2").clear()
        wd.find_element_by_name("address2").send_keys(contact.second_address)
        wd.find_element_by_name("phone2").click()
        wd.find_element_by_name("phone2").clear()
        wd.find_element_by_name("phone2").send_keys(contact.second_phone)
        wd.find_element_by_name("notes").click()
        wd.find_element_by_name("notes").clear()
        wd.find_element_by_name("notes").send_keys(contact.notes)
        wd.find_element_by_xpath("//div[@id='content']/form/input[21]").click()

    def logout(self, wd):
        # logout
        wd.find_element_by_link_text("Logout").click()

    def test_add_new_contact(self):
        wd = self.wd
        self.open_home_page(wd)
        self.login(wd, "admin", "secret")
        self.create_new_contact(wd, Contact(firstname="firstname", middlename="middlename", lastname="lastname",
                           nickname="nickname", title="title", company="company", address="address", phone_home="1111111",
                           phone_mobile="2222222", phone_work="3333333", fax="4444444",email_first="e1-mail@mail.ru", email_second="e2-mail@mail.ru",email_third="e3-mail@mail.ru",
                           homepage="http://homepage.ru", second_address="St-Petersburg, street, building, 1", second_phone="123",
                           notes="go", birth_day_list_item="3", birth_month_list_item="2", birth_year="2000", anniversary_day_list_item="4", anniversary_month_list_item="3", anniversary_year="2015"))
        self.logout(wd)

    def test_add_empty_contact(self):
        wd = self.wd
        self.open_home_page(wd)
        self.login(wd, "admin", "secret")
        self.create_new_contact(wd, Contact(firstname="", middlename="", lastname="",
                           nickname="", title="", company="", address="", phone_home="",
                           phone_mobile="", phone_work="", fax="",email_first="", email_second="",email_third="",
                           homepage="", second_address="", second_phone="",
                           notes="", birth_day_list_item="1", birth_month_list_item="1", birth_year="", anniversary_day_list_item="1", anniversary_month_list_item="1", anniversary_year=""))
        self.logout(wd)

    def tearDown(self):
        self.wd.quit()

if __name__ == '__main__':
    unittest.main()
