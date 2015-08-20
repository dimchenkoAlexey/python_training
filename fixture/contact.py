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

    def set_field_value(self, field_name, value):
        if value is not None:
            wd = self.app.wd
            wd.find_element_by_name(field_name).click()
            wd.find_element_by_name(field_name).clear()
            wd.find_element_by_name(field_name).send_keys(value)

    def select_list_item(self, list_id, value):
        if value is not None:
            wd = self.app.wd
            xpath = "//div[@id='content']/form/select[" + list_id + "]//option[" + value + "]"
            if not wd.find_element_by_xpath(xpath).is_selected():
                wd.find_element_by_xpath(xpath).click()


    def fill_contact_fields(self, contact):
        wd = self.app.wd
        wd.find_element_by_link_text("add new").click()

        self.set_field_value("firstname", contact.firstname)
        self.set_field_value("middlename", contact.middlename)
        self.set_field_value("lastname", contact.lastname)
        self.set_field_value("nickname", contact.nickname)
        self.set_field_value("title", contact.title)
        self.set_field_value("company", contact.company)
        self.set_field_value("address", contact.address)
        self.set_field_value("home", contact.phone_home)
        self.set_field_value("mobile", contact.phone_mobile)
        self.set_field_value("work", contact.phone_work)
        self.set_field_value("fax", contact.fax)
        self.set_field_value("email", contact.email_first)
        self.set_field_value("email2", contact.email_second)
        self.set_field_value("email3", contact.email_third)
        self.set_field_value("homepage", contact.homepage)
        self.set_field_value("homepage", contact.homepage)

        self.select_list_item("1", contact.birth_day_list_item)
        self.select_list_item("2", contact.birth_month_list_item)
        self.set_field_value("byear", contact.birth_year)

        self.select_list_item("3", contact.anniversary_day_list_item)
        self.select_list_item("4", contact.anniversary_month_list_item)
        self.set_field_value("ayear", contact.anniversary_year)

        self.set_field_value("address2", contact.second_address)
        self.set_field_value("phone2", contact.second_phone)
        self.set_field_value("notes", contact.notes)

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

    def count(self):
        wd = self.app.wd
        return len(wd.find_elements_by_name("selected[]"))

