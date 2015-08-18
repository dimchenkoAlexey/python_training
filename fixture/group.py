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

    def fill_attributes(self, group):
        wd = self.app.wd
        wd.find_element_by_name("group_name").click()
        wd.find_element_by_name("group_name").clear()
        wd.find_element_by_name("group_name").send_keys(group.name)
        wd.find_element_by_name("group_header").click()
        wd.find_element_by_name("group_header").clear()
        wd.find_element_by_name("group_header").send_keys(group.header)
        wd.find_element_by_name("group_footer").click()
        wd.find_element_by_name("group_footer").clear()
        wd.find_element_by_name("group_footer").send_keys(group.footer)

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