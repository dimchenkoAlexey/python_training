__author__ = 'admin'

class ContactHelper:
    def __init__(self, app):
        self.app = app

    def create(self, contact):
        self.fill_contact_fields(contact)

    def modify(self, contact):
        # modify contact
        self.click_edit_button()
        self.fill_contact_fields(contact)

    def fill_contact_fields(self, contact):
        wd = self.app.wd
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

    def delete_first_contact(self):
        wd = self.app.wd
        wd.find_element_by_name("selected[]").click()
        wd.find_element_by_xpath("//div[@id='content']/form[2]/div[2]/input").click()

    def delete_all_contacts(self):
        wd = self.app.wd
        mass_checkbox = wd.find_element_by_id("MassCB")
        if not mass_checkbox.is_selected():
            mass_checkbox.click()
        wd.find_element_by_xpath("//div[@id='content']/form[2]/div[2]/input").click()

    def click_edit_button(self):
        wd = self.app.wd
        wd.find_element_by_css_selector("img[alt=\"Edit\"]").click()