__author__ = 'admin'


class GroupHelper:
    def __init__(self, app):
        self.app = app

    def open_groups_page(self):
        wd = self.app.wd
        # open groups page
        wd.find_element_by_link_text("groups").click()

    def create(self, group):
        wd = self.app.wd
        self.open_groups_page()
        # new group creation
        wd.find_element_by_name("new").click()
        # fill fields
        self.fill_attributes(group)
        wd.find_element_by_name("submit").click()

    def modify(self, group):
        wd = self.app.wd
        self.open_groups_page()
        # modify group
        self.click_edit_button()
        # fill fields
        self.fill_attributes(group)
        wd.find_element_by_name("update").click()

    def set_field_value(self, field_name, value):
        if value is not None:
            wd = self.app.wd
            wd.find_element_by_name(field_name).click()
            wd.find_element_by_name(field_name).clear()
            wd.find_element_by_name(field_name).send_keys(value)

    def fill_attributes(self, group):
        self.set_field_value("group_name", group.name)
        self.set_field_value("group_header", group.header)
        self.set_field_value("group_footer", group.footer)

    def delete_first_group(self):
        wd = self.app.wd
        self.open_groups_page()
        wd.find_element_by_name("selected[]").click()
        wd.find_element_by_name("delete").click()

    def click_edit_button(self):
        wd = self.app.wd
        wd.find_element_by_xpath("//div[@id='content']/form/input[6]").click()

    def delete_all_groups(self):
        wd = self.app.wd
        self.open_groups_page()
        checkboxes = wd.find_elements_by_name("selected[]")
        for checkbox in checkboxes:
            if not checkbox.is_selected():
                checkbox.click()
        wd.find_element_by_name("delete").click()